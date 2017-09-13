# -*- mode: python -*-

block_cipher = None


a = Analysis(['E:\\PyQt\\PyQt_project\\control\\main_control.py'],
             pathex=['C:\\Users\\heygo\\Anaconda3\\envs\\python36_pyqt\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'E:\\PyQt\\PyQt_project\\control'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_control',
          debug=False,
          strip=False,
          upx=True,
          console=False )
