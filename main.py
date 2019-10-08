import os
from config import Config
from client import Client


def main():
    client = Client(Config)
    local_files = os.walk(os.path.abspath(Config.local_files))
    for root, dirs, files in local_files:
        for file in files:
            local_file = root + '/' + file
            client.upload(local_file, '/uploads')
            filename = file.split('/')[-1]
            print(f'Uploaded {filename} to {Config.remote_url}:/uploads.')
    client.disconnect()


main()
