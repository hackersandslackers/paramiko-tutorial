from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException
from scp import SCPClient, SCPException
from io import StringIO


class Client:
    """SSH Client class."""

    def __init__(self, config):
        self.remote_url = config.remote_url
        self.remote_user = config.remote_user
        self.remote_ssh_key = config.remote_ssh_key
        self.pkey = self.__get_ssh_key()
        self.client = None

    def __get_ssh_key(self):
        """Get our SSH key."""
        f = open(self.remote_ssh_key, 'r')
        s = f.read()
        keyfile = StringIO(s)
        pkey = RSAKey.from_private_key(keyfile)
        return pkey

    def __connect(self):
        """Connect to remote."""
        if self.client is None:
            try:
                client = SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(AutoAddPolicy())
                client.connect(self.remote_url,
                               username=self.remote_user,
                               pkey=self.pkey)
            except AuthenticationException:
                raise AuthenticationException('Authentication failed: did you remember to create an SSH key?')
            finally:
                return client
        return self.client

    def upload(self, file, remote_directory):
        """Upload a single file to a remote directory"""
        self.client = self.__connect()
        scp = SCPClient(self.client.get_transport())
        try:
            scp.put(file,
                    recursive=True,
                    remote_path=remote_directory)
        except SCPException:
            raise SCPException.message
        finally:
            scp.close()

    def execute(self, cmd):
        """Executes a single unix command."""
        self.client = self.__connect()
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.readlines()

    def disconnect(self):
        """Close ssh connection."""
        self.client.close()
