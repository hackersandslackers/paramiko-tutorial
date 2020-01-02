"""Perform tasks against a remote host."""
from config import (host,
                    user,
                    ssh_key_filepath,
                    local_file_directory,
                    remote_path)
from .files import fetch_local_files
from .client import RemoteClient


def main():
    """Initialize remote host client and execute actions."""
    remote = RemoteClient(host, user, ssh_key_filepath, remote_path)
    upload_files_to_remote(remote)
    execute_command_on_remote(remote)
    remote.disconnect()


def upload_files_to_remote(remote):
    """Upload files to remote via SCP."""
    files = fetch_local_files(local_file_directory)
    remote.bulk_upload(files)


def execute_command_on_remote(remote):
    """Execute UNIX command on the remote host."""
    remote.execute_cmd('cd /var/www/ghost ls')

