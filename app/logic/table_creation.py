import pyodbc
from app.UI.conection_form import INFO

class TableCreation:
    def __init__(self):
        pass

    def createTable(self,tableName):
        server, database = INFO['server'], INFO['database']
        try:
            conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
            cursor = conn.cursor()
            sqlString = f'CREATE TABLE {tableName} (id INT PRIMARY KEY,'
            
            cursor.execute(f'USE {database};')
            cursor.execute(sqlString)

            conn.close()
        except Exception as e:
            self.show_error_message(f"Error al crear la tabla: {str(e)}")
        pass

