from app.logic.conection import Connection
from app.logic.field import Field

class Table:
    def __init__(self):
        pass

    def create(self,name,connection,fields):
        cursor = connection.cursor()
        sql = f"CREATE TABLE {name} (id int PRIMARY KEY, "
        for field in fields:
            sql += f"{field.name} {field.type},"
            print(field.name,field.type)
        sqlString = sql[:-1]
        sqlString += " )"
        cursor.execute(sqlString)

    def select():
        pass

    def insert():
        pass

    def update():
        pass

    def delete():
        pass


