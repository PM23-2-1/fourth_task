import os
class DB_names():
    def __init__(self,):
        self._name = input('Имя бд: ')
        self._name_table = input('Имя таблицы: ')

    def get_name(self, ):
        return self._name
    
    def get_name_table(self, ):
        return self._name_table

os.system('cls||clear')
db_names = DB_names()