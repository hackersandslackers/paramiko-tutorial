"""Perform tasks against a remote host."""
from config import local_file_directory

from .client import RemoteClient
from .files import fetch_local_files


def main(ssh_remote_client: RemoteClient):
    """
    Initialize remote host client and execute actions.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    """
    upload_files_to_remote(ssh_remote_client)
    execute_command_on_remote(ssh_remote_client)


def upload_files_to_remote(ssh_remote_client: RemoteClient):
    """
    Upload files to remote via SCP.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    """
    local_files = fetch_local_files(local_file_directory)
    ssh_remote_client.bulk_upload(local_files)


def execute_command_on_remote(ssh_remote_client: RemoteClient):
    """
    Execute UNIX command on the remote host.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    """
    ssh_remote_client.execute_commands(
        [
            "cd /var/www/ && ls",
            "tail /var/log/nginx/access.log",
            "ps aux | grep node",
            "cd /uploads/ && ls",
        ]
    )
