"""Client to handle connections and actions executed against a remote host."""
from os import system

from log import LOGGER
from paramiko import AutoAddPolicy, RSAKey, SSHClient
from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException


class RemoteClient:
    """Client to interact with a remote host via SSH & SCP."""

    def __init__(self, host, user, ssh_key_filepath, remote_path):
        self.host = host
        self.user = user
        self.ssh_key_filepath = ssh_key_filepath
        self.remote_path = remote_path
        self.client = None
        self.scp = None
        self.conn = None
        self._upload_ssh_key()

    @LOGGER.catch
    def _get_ssh_key(self):
        """ Fetch locally stored SSH key."""
        try:
            self.ssh_key = RSAKey.from_private_key_file(self.ssh_key_filepath)
            LOGGER.info(f"Found SSH key at self {self.ssh_key_filepath}")
        except SSHException as error:
            LOGGER.error(error)
        return self.ssh_key

    @LOGGER.catch
    def _upload_ssh_key(self):
        try:
            system(
                f"ssh-copy-id -i {self.ssh_key_filepath}.pub {self.user}@{self.host}>/dev/null 2>&1"
            )
            LOGGER.info(f"{self.ssh_key_filepath} uploaded to {self.host}")
        except FileNotFoundError as error:
            LOGGER.error(error)

    @LOGGER.catch
    def _connect(self):
        """Open connection to remote host. """
        if self.conn is None:
            try:
                self.client = SSHClient()
                self.client.load_system_host_keys()
                self.client.set_missing_host_key_policy(AutoAddPolicy())
                self.client.connect(
                    self.host,
                    username=self.user,
                    key_filename=self.ssh_key_filepath,
                    look_for_keys=True,
                    timeout=5000,
                )
                self.scp = SCPClient(self.client.get_transport())
            except AuthenticationException as error:
                LOGGER.error(
                    f"Authentication failed: did you remember to create an SSH key? {error}"
                )
                raise error
        return self.client

    def disconnect(self):
        """Close SSH & SCP connection."""
        if self.client:
            self.client.close()
        if self.scp:
            self.scp.close()

    @LOGGER.catch
    def bulk_upload(self, files):
        """
        Upload multiple files to a remote directory.

        :param files: List of local files to be uploaded.
        :type files: List[str]
        """
        self.conn = self._connect()
        uploads = [self._upload_single_file(file) for file in files]
        LOGGER.info(
            f"Finished uploading {len(uploads)} files to {self.remote_path} on {self.host}"
        )

    def _upload_single_file(self, file):
        """Upload a single file to a remote directory."""
        try:
            self.scp.put(file, recursive=True, remote_path=self.remote_path)
            LOGGER.info(f"Uploaded {file} to {self.remote_path}")
            return file
        except SCPException as error:
            LOGGER.error(error)
            raise error

    def download_file(self, file):
        """Download file from remote host."""
        self.conn = self._connect()
        self.scp.get(file)

    @LOGGER.catch
    def execute_commands(self, commands):
        """
        Execute multiple commands in succession.

        :param commands: List of unix commands as strings.
        :type commands: List[str]
        """
        self.conn = self._connect()
        for cmd in commands:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            for line in response:
                LOGGER.info(f"INPUT: {cmd} | OUTPUT: {line}")
