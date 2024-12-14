import sqlite3
from typing import List, Tuple

class DataBase:
    def _init_(self):  
        self.conn = sqlite3.connect('.th')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Main (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                 quest_1 TEXT,
                 quest_2 TEXT,
                 quest_3 BOOL,
                 quest_4 BOOL,
                 quest_5 TEXT,
                 quest_6 TEXT,
                 quest_7 TEXT,
                 quest_8 TEXT,
                 quest_9 TEXT,
                 quest_10 BOOL,
            )
        """)
        self.conn.commit()

    def insert_quest_data(self, data_list: Tuple):
        self.cursor.execute(""" 
            INSERT INTO Main (full_name, quest_1, quest_2, quest_3, quest_4, quest_5, quest_6, quest_7, quest_8, quest_9, quest_10)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data_list)
        self.conn.commit()

    def select_data(self):
        self.cursor.execute("SELECT * FROM Main")
        return self.cursor.fetchall()

    def check_id(self, id):
        self.cursor.execute("SELECT * FROM Main WHERE id = ?", (id,))
        data = self.cursor.fetchone()
        if data is None:
            return False
        else:
            return True

    def close(self):  
        self.conn.close()

DB = DataBase()

Dict_raw_data_user = dict()


#пример
import sqlite3
from typing import List, Tuple

class DataBase:
    def __init__(self, db_name: str):
        """Инициализация базы данных с указанием имени базы"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def close(self):
        """Закрытие соединения с базой данных"""
        self.conn.close()

    # пример метода для выполнения запроса
    def execute_query(self, query: str, params: Tuple = ()) -> List[Tuple]:
        """Выполнение SQL запроса и возврат результата"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

DB = DataBase('your_database.db')

Dict_raw_data_user = dict()
