from setuptools import setup

# Главный скрипт — main.py, находится в той же папке
APP = ['main.py']

# Дополнительные файлы (если нужны) — можно оставить пустым
DATA_FILES = []

OPTIONS = {
    'argv_emulation': False,          # отключаем эмуляцию аргументов командной строки
    'packages': ['plotext', 'termcolor'],  # явно подключаем эти модули
    'iconfile': 'icon.icns',          # иконка в той же папке
    'plist': {                        # информация о приложении
        'CFBundleName': 'Ballistics Calc',
        'CFBundleDisplayName': 'Ballistics Calc',
        'CFBundleIdentifier': 'com.superded.ballistics',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0',
    },
    'excludes': ['tkinter'],          # исключаем ненужные библиотеки (уменьшает размер)
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
