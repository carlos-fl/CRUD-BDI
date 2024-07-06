from app.logic.conection import Connection
from app.logic.field import Field

class Table:
    def __init__(self):
        pass

    def create(self, db_name, name, connection, fields):
        cursor = connection.cursor()
        sqlDB = f"USE {db_name};"
        cursor.execute(sqlDB)
        sql = f"CREATE TABLE {name} (id INT PRIMARY KEY, "
        for field in fields:
            sql += f"{field.name} {field.type},"
            print(field.name,field.type)
        sqlString = sql[:-1]
        sqlString += " );"
        print(sqlString)
        cursor.execute(sqlString)
        connection.commit()

    def select_all(self, db_name, table_name, connection):  #select sin condicion
        cursor = connection.cursor()
        sqlDB = f"USE {db_name};"
        cursor.execute(sqlDB)
        sql = f"SELECT * FROM {table_name};"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()

    def insert(self, db_name, table_name, connection):
        cursor = connection.cursor()
        sqlDB = f"USE {db_name};"
        cursor.execute(sqlDB)
        sql = f"INSERT INTO {table_name} VALUES "
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()

    def update(self, db_name, name, connection):
        pass

    def delete_all_rows(self, db_name, table_name, connection):
        cursor = connection.cursor()
        sqlDB = f"USE {db_name};"
        cursor.execute(sqlDB)
        sql = f"DELETE FROM {table_name};"
        cursor.execute(sql)
        connection.commit()

    def delete_row(self):
        pass

