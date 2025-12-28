# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Collect selected kivy submodules and explicit small imports (avoid scanning whole package)
hidden_imports = (
    collect_submodules('kivy.uix')
    + collect_submodules('kivy.graphics')
    + collect_submodules('kivy.core')
    + ['kivy.weakmethod', 'kivy.core.window.window_sdl2', 'kivy.core.image.img_sdl2', 'kivy.core.text.text_sdl2']
)

jaraco_datas = collect_data_files('jaraco.text')
raw_kivy_datas = collect_data_files('kivy')
# Remap kivy data files into the Frameworks/kivy_install directory inside the .app bundle
kivy_datas = []
for src, dest in raw_kivy_datas:
    kivy_datas.append((src, os.path.join('Frameworks', 'kivy_install', dest)))

a = Analysis(
    ['main.py'],
    pathex=[os.path.abspath('.')],
    binaries=[],
    datas=[('ui', 'ui'), ('notes.json', '.')] + jaraco_datas + kivy_datas,
    hiddenimports=hidden_imports,
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['gi', 'kivy.lib.gstplayer', 'kivy.tools.packaging.pyinstaller_hooks'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MinhasNotas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MinhasNotas',
)

app = BUNDLE(
    coll,
    name='MinhasNotas.app',
    icon=None,
    bundle_identifier=None,
)

