from os import environ, rename, remove
from os.path import exists
from shutil import copy
import requests
import filetype
from lib.utils import resolve_path


image_url=environ.get('BACKGROUND_IMAGE_URL', '')
image_path_temp=f'{resolve_path()}/static/img/background_image_temp'

def file_is_image(file) -> bool:
    kind = filetype.guess(file).mime
    if not "image" in kind:
        print(f'{image_url} no is image file type!')
        print(f'File extension: {kind.extension}')
        print(f'File MIME type: {kind.mime}')
        remove(file)
        return False
    else:
        return True

def download_image():
    filedownload = requests.get(image_url)
    open(image_path_temp, 'wb').write(filedownload.content)


def define_background_image():
    if exists(f'{resolve_path()}/static/img/background_image_use'):
        remove(f'{resolve_path()}/static/img/background_image_use')
    if image_url != '':
        download_image()
        if exists(image_path_temp) and file_is_image(image_path_temp):
            rename(image_path_temp, f'{resolve_path()}/static/img/background_image_use')
            print('Set background image!')
            return
        
    copy(f'{resolve_path()}/static/img/background_image_original.png', f'{resolve_path()}/static/img/background_image_use')
