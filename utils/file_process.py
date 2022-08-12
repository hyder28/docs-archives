import os
from pathlib import Path

temp_folder = Path("tmp/")
source_folder = Path("src/")
target_folder = Path("tar/")

def clear_folder(path):
    """create and clear paths"""
    if not os.path.isdir(path):
        os.mkdir(path)

    for f in os.listdir(path):
        os.remove(os.path.join(path, f))