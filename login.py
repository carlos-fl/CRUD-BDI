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
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 280, 170)
        
        # Creación de widgets
        self.label_user = QLabel('Usuario:', self)
        self.input_user = QLineEdit(self)

        self.label_password = QLabel('Contraseña:', self)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)  # Ocultar texto de la contraseña

        self.button_login = QPushButton('Login', self)
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
        username = self.input_user.text()
        password = self.input_password.text()

        server = 'LAPTOP-T4LHCLML\SQLEXPRESS'
        database = 'BDCRUD2'
        port = '1433'

        conn = Connection()
        is_valid = conn.validate_user(server, database, port, username, password)

        if is_valid:
            QMessageBox.information(self, 'Login exitoso', 'Bienvenido, admin!')
        else:
            QMessageBox.warning(self, 'Error de login', 'Usuario o contraseña incorrectos')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
