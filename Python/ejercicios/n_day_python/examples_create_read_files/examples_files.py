import os
import datetime
# https://docs.python.org/3/library/os.path.html
# https://docs.python.org/3/library/os.html

this_file_path = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(this_file_path)
# OR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

print(f"this_file_path -> {this_file_path}")
print(f"BASE_DIR -> -{BASE_DIR}")
print(f"ENTIRE_PROJECT_DIR -> {ENTIRE_PROJECT_DIR}")

# CREATE DIRECTORY templates IN folder_dir_path
folder_dir_path = os.path.join(BASE_DIR, "templates")
print(f"folder_dir_path -> -{folder_dir_path}")
if not os.path.exists(folder_dir_path):
    os.makedirs(folder_dir_path, exist_ok=True)
if os.path.exists(folder_dir_path):
    # CREATE FILE IN FOLDER templates
    file_dir_path = os.path.join(BASE_DIR, "templates", "file.txt")
    with open(file_dir_path, 'w') as f:
        f.write(f"{datetime.datetime.now()}")
