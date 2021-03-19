"""Find local files to be uploaded to remote host."""
from os import walk
from typing import List

from config import basedir


def fetch_local_files(local_file_dir: str) -> List[str]:
    """Create list of file paths."""
    local_files = walk(local_file_dir)
    for root, dirs, files in local_files:
        return [f"{basedir}/{root}/{file}" for file in files]
