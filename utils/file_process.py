import os
from pathlib import Path

temp_folder = Path("tmp/")
source_folder = Path("src/")
target_folder = Path("output/")


def clear_files_in_folder(path):
    """create and clear any files in a folder"""
    if not os.path.isdir(path):
        os.mkdir(path)

    for f in os.listdir(path):
        os.remove(os.path.join(path, f))


def process_clean_all_folders():
    """clear all folders"""
    for folder in [temp_folder, source_folder, target_folder]:
        clear_files_in_folder(folder)
