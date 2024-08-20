import PyInstaller.__main__

PyInstaller.__main__.run([
    '--onefile',
    '--optimize=2',
    '--noconfirm',
    '-s',
    'filetoimage.py'
])
