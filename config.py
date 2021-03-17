"""Remote host configuration."""
from os import getenv, path

from dotenv import load_dotenv
from log import LOGGER

# Load environment variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Read environment variables
host = getenv("REMOTE_HOST")
user = getenv("REMOTE_USERNAME")
ssh_key_filepath = getenv("SSH_KEY")
remote_path = getenv("REMOTE_PATH")
config_values = [
    {"host": host},
    {"user": user},
    {"ssh": ssh_key_filepath},
    {"path": remote_path},
]


for config in config_values:
    if None in config.values():
        LOGGER.warning(f"Config value not set: {config.popitem()}")
        raise Exception("Set your environment variables via a .env file.")


local_file_directory = "files"
