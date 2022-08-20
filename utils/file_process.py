import os
from pathlib import Path

temp_folder = Path("tmp/")

def clear_files_in_folder():
    """create and clear any files in a folder"""
    if not os.path.isdir(temp_folder):
        os.mkdir(temp_folder)

    for f in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, f))
