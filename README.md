# FTP File Uploader

This Python script allows you to upload files to an FTP server, excluding specified files from the upload. It uses the `ftplib` library for FTP communication and the `tqdm` library for a visual progress bar.

## Features

- Uploads files from a local directory to a remote FTP server.
- Excludes specified files from the upload.
- Visual progress bar for monitoring the upload process.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sunkist228/ftp-connect.git
   cd ftp-connect

2. **Install the required libraries:**

   ```bash
   pip install ftplib configparser tqdm

3. **Configure 'config.ini'**

   ```ini
   [FTP]
   server = ftp.example.com
   port = 21  # Replace with your desired port
   username = your_username
   password = your_password
   local_directory = /path/to/local/files
   remote_directory = /path/to/remote/files
   exclude_list_file = exclude_list.txt
   
4. **Configure in exclude_list.txt filenames to be excluded, one per line.**
5. **Run the script:**
   ```bash
   python main.py

 ## Notes
   - Make sure to replace placeholders in the config.ini file with your actual FTP server details.
   - The script will upload all files from the local directory to the remote directory, excluding those listed in the exclude_list.txt file.
     
   ***Feel free to customize and modify the script to suit your specific use case.***
