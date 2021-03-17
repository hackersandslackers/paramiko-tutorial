"""Find local files to be uploaded to remote host."""
from os import walk


def fetch_local_files(local_file_dir: str):
    """Create list of file paths."""
    local_files = walk(local_file_dir)
    for root, dirs, files in local_files:
        return [f"{root}/{file}" for file in files]
