import pyodbc

class Connection:
  def __init__(self):
    pass
  # Establishing a connection to the SQL Server
  def connect_to_database(self, server, database, port):
    try:
      connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server},{port};"
        "Trusted_Connection=yes;"
      ) 
      cnxn = pyodbc.connect(connection_string)
      cnxn.autocommit = True
      cursor = cnxn.cursor()
      cursor.execute(f'CREATE DATABASE {database}')
      cursor.close()
      print('connected. Database was created')
    except Exception as e:
      raise Exception(e)

