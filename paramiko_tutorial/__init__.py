"""Perform tasks against a remote host."""
from typing import List

from config import LOCAL_FILE_DIRECTORY

from .client import RemoteClient
from .files import fetch_local_files


def initiate_client(ssh_remote_client: RemoteClient):
    """
    Initialize remote host client and execute actions.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    """
    upload_files_to_remote(ssh_remote_client)
    execute_command_on_remote(
        ssh_remote_client,
        commands=[
            "mkdir /uploads",
            "cd /uploads/ && ls",
        ],
    )


def upload_files_to_remote(ssh_remote_client: RemoteClient):
    """
    Upload files to remote via SCP.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    """
    local_files = fetch_local_files(LOCAL_FILE_DIRECTORY)
    ssh_remote_client.bulk_upload(local_files)


def execute_command_on_remote(
    ssh_remote_client: RemoteClient, commands: List[str] = None
):
    """
    Execute UNIX command on the remote host.

    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    :param commands: List of commands to run on remote host.
    :type commands: List[str]
    """
    ssh_remote_client.execute_commands(commands)
