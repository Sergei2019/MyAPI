import pathlib
import os

DIR_NAME = str(pathlib.Path().resolve())

JSON_CONFIG_FILE_PATH = os.path.join(DIR_NAME, 'db.json')

print(JSON_CONFIG_FILE_PATH)