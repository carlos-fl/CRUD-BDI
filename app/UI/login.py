# login.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from app.logic.conection import Connection

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle('Crear Usuarios')
        self.setGeometry(100, 100, 280, 170)
        
        # Creación de widgets
        self.label_user = QLabel('Usuario:', self)
        self.input_user = QLineEdit(self)

        self.label_password = QLabel('Contraseña:', self)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)  # Ocultar texto de la contraseña

        self.button_login = QPushButton('Crear', self)
        self.button_login.clicked.connect(self.check_credentials)

        # Layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_credentials(self):
        from app.UI.conection_form import INFO

        username = self.input_user.text()
        password = self.input_password.text()

        server, port, database = INFO['server'], INFO['port'], INFO['database'] 

        try:
            con = Connection().connect_to_database(server, database, port)
            cursor = con.cursor()
            
            #query = f"CREATE LOGIN {username} WITH PASSWORD = '{password}', DEFAULT_DATABASE = {database}"
            #cursor.execute(f'USE {database}')
            #cursor.execute(f'ALTER USER {username} WITH LOGIN ')
            #print('QUERY', query)
            #cursor.execute(query)
            query = f"CREATE LOGIN {username} WITH PASSWORD = '{password}'"
            cursor.execute(query)
            grant_permissions_sql = f"USE {database}; ALTER ROLE db_datareader ADD MEMBER {username}; ALTER ROLE db_datawriter ADD MEMBER {username};"
            cursor.execute(grant_permissions_sql)
            grant_permissions_sql = f'CREATE USER {username} FOR LOGIN {username};'
            cursor.execute(grant_permissions_sql)
            cursor.commit()
            QMessageBox.information(self, 'Usuario creado exitosamente', f'Usuario {username} fue creado')
        except Exception as e:
            QMessageBox.warning(self, 'Usuario no pudo ser creado')
            print(e)
