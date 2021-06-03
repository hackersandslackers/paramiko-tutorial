"""Script entry point."""
from config import (
    SCP_DESTINATION_FOLDER,
    SSH_KEY_FILEPATH,
    SSH_PASSWORD,
    SSH_REMOTE_HOST,
    SSH_USERNAME,
)
from paramiko_tutorial import initiate_client
from paramiko_tutorial.client import RemoteClient

# Create SSH remote client connection
ssh_remote_client = RemoteClient(
    SSH_REMOTE_HOST,
    SSH_USERNAME,
    SSH_PASSWORD,
    SSH_KEY_FILEPATH,
    SCP_DESTINATION_FOLDER,
)

if __name__ == "__main__":
    initiate_client(ssh_remote_client)
