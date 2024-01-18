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

def upload_files_ftp(server, username, password, local_dir, remote_dir, exclude_list):
    # Установка соединения с FTP-сервером
    ftp = FTP(server)
    ftp.login(username, password)

    # Переход в удаленный каталог
    ftp.cwd(remote_dir)

    # Получение списка файлов в локальном каталоге
    local_files = os.listdir(local_dir)

    # Фильтрация файлов с учетом исключений
    files_to_upload = [file for file in local_files if file not in exclude_list]

    # Отправка файлов на FTP-сервер
    for file in files_to_upload:
        with open(os.path.join(local_dir, file), 'rb') as f:
            ftp.storbinary('STOR ' + file, f)

    # Закрытие соединения
    ftp.quit()

# Чтение конфигурации из файла config.ini
config = read_config()

# Чтение списка исключений из файла
exclude_list_file = config['exclude_list_file']
exclude_list = read_exclude_list(exclude_list_file)

# Пример использования
server = config['server']
username = config['username']
password = config['password']
local_directory = config['local_directory']
remote_directory = config['remote_directory']

upload_files_ftp(server, username, password, local_directory, remote_directory, exclude_list)
