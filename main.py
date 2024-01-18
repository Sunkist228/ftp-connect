from ftplib import FTP
import os
import configparser

def read_config(filename='config.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    return config['FTP']

def read_exclude_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def upload_files_ftp(server, port, username, password, local_dir, remote_dir, exclude_list):
    # Establish connection to the FTP server
    ftp = FTP()
    ftp.connect(server, port)
    ftp.login(username, password)

    # Change to the remote directory
    ftp.cwd(remote_dir)

    # Get the list of files in the local directory
    local_files = os.listdir(local_dir)

    # Filter files based on exclusions
    files_to_upload = [file for file in local_files if file not in exclude_list]

    # Upload files to the FTP server
    for file in files_to_upload:
        with open(os.path.join(local_dir, file), 'rb') as f:
            ftp.storbinary('STOR ' + file, f)

    # Close the connection
    ftp.quit()

# Read configuration from config.ini file
config = read_config()

# Read the list of exclusions from the file
exclude_list_file = config['exclude_list_file']
exclude_list = read_exclude_list(exclude_list_file)

# Example usage
server = config['server']
port = int(config['port'])
username = config['username']
password = config['password']
local_directory = config['local_directory']
remote_directory = config['remote_directory']

upload_files_ftp(server, port, username, password, local_directory, remote_directory, exclude_list)
