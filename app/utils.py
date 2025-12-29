import sys
import os


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_data_dir():
    from kivy.utils import platform

    if platform == "macosx":
        from os.path import expanduser

        return os.path.join(
            expanduser("~"), "Library", "Application Support", "MinhasNotas"
        )
    return "."
