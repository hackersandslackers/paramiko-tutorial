"""Configuration module."""
from os import environ


class Config:
    """Class-based config."""

    remote_url = environ.get('REMOTE_HOST')
    remote_user = environ.get('REMOTE_USERNAME')
    remote_passphrase = environ.get('REMOTE_PASSPHRASE')
    remote_ssh_key = environ.get('REMOTE_SSH_KEY')
    local_files = 'data'
