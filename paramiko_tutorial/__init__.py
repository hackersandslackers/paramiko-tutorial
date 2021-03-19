"""Perform tasks against a remote host."""
from config import (
    host,
    local_file_directory,
    password,
    remote_path,
    ssh_key_filepath,
    username,
)

from .client import RemoteClient
from .files import fetch_local_files


def main():
    """Initialize remote host client and execute actions."""
    remote = RemoteClient(host, username, password, ssh_key_filepath, remote_path)
    upload_files_to_remote(remote)
    execute_command_on_remote(remote)


def upload_files_to_remote(remote):
    """Upload files to remote via SCP."""
    local_files = fetch_local_files(local_file_directory)
    remote.bulk_upload(local_files)


def execute_command_on_remote(remote):
    """Execute UNIX command on the remote host."""
    remote.execute_commands(
        [
            "cd /var/www/ && ls",
            "tail /var/log/nginx/access.log",
            "ps aux | grep node",
            "cd /uploads/ && ls",
        ]
    )
