#!/usr/bin/env python3
import PyInstaller.__main__
from shutil import copyfile
from distutils.dir_util import copy_tree

MY_VIRTUAL_ENV_NAME = "virtual_env"

print(f"\n{'#'*15} BUILDING TRAY APP {'#'*15}\n")
PyInstaller.__main__.run([
    'trayapp/trayapp.py',
    '--onefile',
    '--icon=./trayapp/art/icons/pink-pig.ico',
    # '--windowed', # uncomment to get rid of console window when trayapp.exe is ran
    f'--paths=./{MY_VIRTUAL_ENV_NAME}/Lib/site-packages',
    '--paths=./trayapp'

])
print(f"\n{'#'*15} BUILDING TRAY APP to /dist FINISHED {'#'*15}\n")

print(f"{'#'*15} COPYING ART TO /dist DIRECTORY {'#'*15}")
copy_tree("./trayapp/art", "dist/art")

print(f"{'#'*15} COPYING AUXILIARY FILES TO /dist DIRECTORY {'#'*15}")

print(f"{'#'*15} BUILD FINISHED! {'#'*15}")
