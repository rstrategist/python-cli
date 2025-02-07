import os
import click

def list_files(directory, recursive=False, extension=None):
    """List files in a directory with options to list recursively and filter by extension."""
    files_list = []
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                if extension is None or file.endswith(extension):
                    files_list.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            if extension is None or file.endswith(extension):
                files_list.append(os.path.join(directory, file))
    return files_list