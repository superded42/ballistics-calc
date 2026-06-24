from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['plotext', 'termcolor'],
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': 'Ballistics Calc',
        'CFBundleDisplayName': 'Ballistics Calc',
        'CFBundleIdentifier': 'com.superded.ballistics',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
