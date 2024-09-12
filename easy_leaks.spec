# -*- mode: python ; coding: utf-8 -*-
import PyInstaller.__main__

block_cipher = None

a = Analysis(
    ['main.py'],  # Entry point of your application
    pathex=['.'],  # Path where to search for your dependencies
    binaries=[],  # Any extra binaries that should be bundled
    datas=[
        ('app_icon.ico', '.'),  # Ensure this points to the icon path
        ('easy_leaks.spec', '.'),  # Spec file itself, for completeness
        ('components\\functions\\get_song_info.py', '.'),  # Include necessary Python files
        ('components\\fonts\\KGHAPPY.ttf', '.'),  # Custom font
        ('components\\functions\\properties.py', '.'),  # Another Python function file
        ('requirements.txt', '.'),  # Requirements file if needed
    ],
    hiddenimports=[],  # Hidden imports if any
    hookspath=[],  # Hooks if necessary
    hooksconfig={},
    runtime_hooks=[],  # Custom runtime hooks if applicable
    excludes=[],  # Modules to exclude
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,  # Don't archive if you want to inspect files
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,  # Scripts that are bundled
    a.binaries,  # Binaries to bundle
    a.zipfiles,  # Zip files if any
    a.datas,  # Data files including icons, fonts, etc.
    [],
    name='EasyLeaks',  # Name of the generated exe file
    debug=False,  # No debug info in final executable
    bootloader_ignore_signals=False,
    strip=False,  # Whether to strip the executable
    upx=True,  # Compress with UPX
    console=True,  # Show console window, can be set to False if not needed
    icon='app_icon.ico',  # Path to the icon
)
