import json
import os
import sqlite3

from const import *

connection = sqlite3.connect("database.db")
cursor1 = connection.cursor()


CONFIG_PROPERTIES={}

try:
	with open(JSON_CONFIG_FILE_PATH, 'r', encoding="utf8") as data_file:
		CONFIG_PROPERTIES=json.load(data_file)
except IOError as e:
	print (e)
	print("Error: can not open the file")

cont = CONFIG_PROPERTIES

for item,value in cont.items() :
	print(item,"-->",value)
	cursor1.execute(f'INSERT INTO {item} VALUES (?,?)',(item,value,))
connection.commit()
connection.close()