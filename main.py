"""Script entry point."""
from config import (
    SCP_DESTINATION_FOLDER,
    SSH_KEY_FILEPATH,
    SSH_PASSWORD,
    SSH_REMOTE_HOST,
    SSH_USERNAME,
)
from paramiko_tutorial import main
from paramiko_tutorial.client import RemoteClient

ssh_remote_client = RemoteClient(
    SSH_REMOTE_HOST,
    SSH_USERNAME,
    SSH_PASSWORD,
    SSH_KEY_FILEPATH,
    SCP_DESTINATION_FOLDER,
)

if __name__ == "__main__":
    main(ssh_remote_client)
