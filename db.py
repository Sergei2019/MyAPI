import json

from typing import Any, Union

import os

import pandas as pd

from sqlalchemy import create_engine

class DatabaseEngine:
    """
    It's a database implementation based on json
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.db = {

        }
        self.load_db()
    
    def save_func(self):
        json.dump(self.db, open(self.filename, 'w'))

    def load_db(self):
        if os.path.isfile(self.filename):
            self.db = json.load(open(self.filename))

    def create_table(self, table_name: Union[str, int, float]) -> None:
        self.db[table_name] = {

        }
        self.save_func()

    def delete_table(self, table_name: Union[str, int, float]) -> bool:
        if table_name in self.db.keys():
            del self.db[table_name]
            self.save_func()
            return True
        return False

    def insert(self, table_name: Union[str, int, float],
               key: Union[str, int, float, list],
               val: Any)->None:
        if not table_name in self.db.keys():
            self.db[table_name] = {}
        self.db[table_name][key] = val
        self.save_func()
    
    def get(self, table_name: Union[str, int, float], key: Union[str, int, float])->Any:
        if table_name in self.db.keys():
            return self.db[table_name][key]
        return None

    def delete(self, table_name: Union[str, int, float], key: Union[str, int, float])->Any:
        if table_name in self.db.keys():
            table = self.db[table_name][key]
            if key in table.keys():
                del table[key]
                self.save_func()
                return True
        return False


if __name__=='__main__':
    db = DatabaseEngine("db.json")
    db.create_table("Test_table")
    db.insert("Test_table", "test_COLUMN1", [2323])
    db.insert("Test_table", "test_COLUMN2", ["aAJDAD"])
    db.insert("Test_table", "test_COLUMN3", [111])
    db.insert("Test_table", "test_COLUMN4", ["AASAAS"])
    print(db.db)
    with open('db.json') as dbfile:
        kk = json.load(dbfile)['Test_table']
        v = pd.DataFrame(kk)
    print(kk)
    print(v)
    engine = create_engine("sqlite:///database.db")
    v.to_sql('Test_table', engine)

