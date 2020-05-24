"""Local files to be uploaded."""
import os


def fetch_local_files(local_file_dir):
    """Upload local files to remote host."""
    local_files = os.walk(local_file_dir)
    for root, dirs, files in local_files:
        return [f'{root}/{file}' for file in files]
