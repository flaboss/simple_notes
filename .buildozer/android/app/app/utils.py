import sys
import os


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller/Android"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # On Android, the current working directory is the app folder usually
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_path, relative_path)


def get_data_dir():
    from kivy.utils import platform

    if platform == "macosx":
        from os.path import expanduser

        return os.path.join(
            expanduser("~"), "Library", "Application Support", "MinhasNotas"
        )
    elif platform == "android":
        from kivy.app import App

        app = App.get_running_app()
        if app:
            return app.user_data_dir

    return "."
