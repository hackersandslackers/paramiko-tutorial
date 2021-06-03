"""Find local files to be uploaded to remote host."""
from os import walk
from typing import List

from config import LOCAL_FILE_DIRECTORY


def fetch_local_files(local_file_dir: str) -> List[str]:
    """
    Create list of file paths.

    :param local_file_dir: Local filepath of assets to SCP to host.
    :type local_file_dir: List[str]
    """
    local_files = walk(local_file_dir)
    for root, dirs, files in local_files:
        return [f"{LOCAL_FILE_DIRECTORY}/{file}" for file in files]
