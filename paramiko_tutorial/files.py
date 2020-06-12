"""Find local files to be uploaded to remote host."""
import os


def fetch_local_files(local_file_dir):
    """Create list of file paths."""
    local_files = os.walk(local_file_dir)
    for root, dirs, files in local_files:
        return [f'{root}/{file}' for file in files]
