import os
import requests
import shutil  # https://docs.python.org/3/library/shutil.html

# DOWNLOAD LARGE FILE WITH PYTHON


def download_file(url, directory, file_name=None):
    if file_name == None:
        file_name = os.path.basename(url)  # THE NAME OF THE FILE
    print(f"Name image -> {file_name}")
    dl_path = os.path.join(directory, file_name)

    with requests.get(url, stream=True) as r:
        with open(dl_path, "wb") as file_obj:
            shutil.copyfileobj(r.raw, file_obj)
    return dl_path


def download_file_slower(url):
    local_filename = url.split('/')[-1]
    # NOTEs the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename
