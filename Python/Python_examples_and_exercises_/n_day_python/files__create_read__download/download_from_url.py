import os
import shutil  # https://docs.python.org/3/library/shutil.html

import requests
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "download")

print(f"THIS_FILE_PATH --> {THIS_FILE_PATH}")
print(f"BASE_DIR --> {BASE_DIR}")
print(f"DOWNLOADS_DIR --> {DOWNLOADS_DIR}")


os.makedirs(DOWNLOADS_DIR, exist_ok=True)

DOWNLOADED_IMG_PATH = os.path.join(DOWNLOADS_DIR, "1.jpg")

url = "https://live.staticflickr.com/34/73385061_b64065d91f_b.jpg"

""" r = requests.get(url, stream=True)
r.raise_for_status()  # 200
with open(DOWNLOADED_IMG_PATH, 'wb') as f:
    f.write(r.content) """

# DOWNLOAD IMAGE IN ANOTHER BETTER WAY
""" 
dl_filename = os.path.basename(url)  # THE NAME OF THE FILE
print(dl_filename)
new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)

with requests.get(url, stream=True) as r:
    with open(new_dl_path, 'wb') as file_obj:
        shutil.copyfileobj(r.raw, file_obj)
 """

download_file(url, DOWNLOADS_DIR)
