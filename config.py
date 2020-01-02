"""Configuration module."""
from os import environ

host = environ.get('REMOTE_HOST')
user = environ.get('REMOTE_USERNAME')
ssh_key_filepath = environ.get('SSH_KEY')
remote_path = environ.get('REMOTE_PATH')

local_file_directory = 'data'
