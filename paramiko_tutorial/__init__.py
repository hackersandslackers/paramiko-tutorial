"""Perform tasks against a remote host."""
from typing import List

from config import (
    LOCAL_FILE_DIRECTORY,
    SCP_DESTINATION_FOLDER,
    SSH_KEY_FILEPATH,
    SSH_PASSWORD,
    SSH_REMOTE_HOST,
    SSH_USERNAME,
)
from paramiko_tutorial.server import RemoteClient

from .files import fetch_local_files
from .server import RemoteClient


def run():
    """Initialize remote host client and execute actions."""
    client = RemoteClient(
        SSH_REMOTE_HOST,
        SSH_USERNAME,
        SSH_PASSWORD,
        SSH_KEY_FILEPATH,
        SCP_DESTINATION_FOLDER,
    )
    upload_files_to_remote(client)
    execute_command_on_remote(
        client,
        commands=[
            "mkdir /uploads",
            "cd /uploads/ && ls",
        ],
    )


def upload_files_to_remote(client: RemoteClient):
    """
    Upload files to remote via SCP.

    :param RemoteClient client: Remote server client.
    """
    local_files = fetch_local_files(LOCAL_FILE_DIRECTORY)
    client.bulk_upload(local_files)


def execute_command_on_remote(client: RemoteClient, commands: List[str] = None):
    """
    Execute a UNIX command remotely on a given host.

    :param RemoteClient client: Remote server client.
    :param List[str] commands: List of commands to run on remote host.
    """
    client.execute_commands(commands)
