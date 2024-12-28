from os import environ, rename, remove
from os.path import exists
from shutil import copy
import requests
import filetype
image_path_temp='static/img/background_image_temp'
image_url=environ.get("BACKGROUND_IMAGE_URL", "")

def file_is_image(file) -> bool:
    kind = filetype.guess(file).mime
    if not "image" in kind:
        print('%s no is image file type!' % image_url)
        print('File extension: %s' % kind.extension)
        print('File MIME type: %s' % kind.mime)
        remove(file)
        return False
    else:
        return True

def download_image():
    filedownload = requests.get(image_url)
    open(image_path_temp, 'wb').write(filedownload.content)


def define_background_image():
    if exists("static/img/background_image_use"):
        remove("static/img/background_image_use")
    if image_url != "":
        download_image()
        if exists(image_path_temp) and file_is_image(image_path_temp):
            rename(image_path_temp, "static/img/background_image_use")
            return
        
    copy('static/img/background_image_original', 'static/img/background_image_use')
