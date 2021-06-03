"""Remote host configuration."""
from os import getenv, path

from dotenv import load_dotenv

from log import LOGGER

# Load environment variables from .env
BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# SSH Connection Variables
ENVIRONMENT = getenv("ENVIRONMENT")
SSH_REMOTE_HOST = getenv("SSH_REMOTE_HOST")
SSH_USERNAME = getenv("SSH_USERNAME")
SSH_PASSWORD = getenv("SSH_PASSWORD")
SSH_KEY_FILEPATH = getenv("SSH_KEY_FILEPATH")
SCP_DESTINATION_FOLDER = getenv("SCP_DESTINATION_FOLDER")
SSH_CONFIG_VALUES = [
    {"host": SSH_REMOTE_HOST},
    {"user": SSH_USERNAME},
    {"password": SSH_PASSWORD},
    {"ssh": SSH_KEY_FILEPATH},
    {"path": SCP_DESTINATION_FOLDER},
]

# Kerberos
KERBEROS_USER = getenv("KERBEROS_USER")

# Database config
DATABASE_HOSTS = [
    {"hdprod": getenv("DATABASE_HDPROD_URI")},
    {"sdprod": getenv("DATABASE_SDPROD_URI")},
    {"gamedata": getenv("DATABASE_GAMEDATA_URI")},
    {"gameentry": getenv("DATABASE_GAMEENTRY_URI")},
    {"boxfile": getenv("DATABASE_BOXFILE_URI")},
]

# EC2 instances in a devstack
DEVSTACK_BOXES = ["web", "api", "app", "state", ""]

# Verify all config values are present
for config in SSH_CONFIG_VALUES + SSH_CONFIG_VALUES:
    if None in config.values():
        LOGGER.warning(f"Config value not set: {config.popitem()}")
        raise Exception("Please set your environment variables via a `.env` file.")

# Local file directory (no trailing slashes)
LOCAL_FILE_DIRECTORY = f"{BASE_DIR}/files"
