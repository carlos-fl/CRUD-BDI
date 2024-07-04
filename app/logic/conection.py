import pyodbc

class Connection:
  def __init__(self):
    pass
  # Establishing a connection to the SQL Server
  def connect_to_database(self, server, database):
    try:
      cnxn = pyodbc.connect(
        Trusted_Connection='Yes',
        Driver='{ODBC Driver 17 for SQL Server}',
        Server= server, #TODO debe ser el nombre especificado
         #TODO debería poder crear la base de datos no conectar a una.
      )
      cnxn.autocommit = True
      cursor = cnxn.cursor()
      cursor.execute(f'CREATE DATABASE {database}')
      cursor.close()
      print('connected. Database was created')
    except Exception as e:
      raise Exception(e)
