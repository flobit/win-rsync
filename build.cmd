@echo off
pyinstaller --clean -c -F rsync.py
move  /Y dist\rsync.exe .\
rmdir /S /Q __pycache__
rmdir /S /Q build
rmdir /S /Q dist
del /S /Q rsync.spec