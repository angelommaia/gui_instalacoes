@ECHO OFF

pyinstaller  --onefile --windowed --add-data "tulum.exe;." --add-data "bolt.ico;." --icon=bolt.ico gui_instalacao.py


PAUSE
