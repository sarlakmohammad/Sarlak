import shutil
from tkinter.filedialog import askdirectory

def back_up():
    _path = askdirectory(title="choose a directory")
    try:
        shutil.copy('Data/sarlak1404.db',_path)
    except FileNotFoundError:
        pass