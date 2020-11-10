# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui_instalacao.py'],
             pathex=['C:\\Users\\Eu\\Documents\\UFF\\Periodos\\2020.1\\Bagunça\\projeto_instalacoes\\tkinter'],
             binaries=[],
             datas=[('tulum.exe', '.'), ('bolt.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui_instalacao',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='bolt.ico')
