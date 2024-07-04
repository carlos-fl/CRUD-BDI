import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from app.logic.conection import Connection

class DatabaseForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Size of window
        self.resize(700, 400)

        # Create widgets
        self.server_label = QLabel('Server:', self)
        self.server_input = QLineEdit(self)

        self.database_label = QLabel('Database:', self)
        self.database_input = QLineEdit(self)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit_data)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.server_label)
        layout.addWidget(self.server_input)
        layout.addWidget(self.database_label)
        layout.addWidget(self.database_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.setWindowTitle('Database Connection Form')
        self.show()

    def submit_data(self):
        server = self.server_input.text()
        database = self.database_input.text()

        if server and database:
            try:
                con = Connection()
                con.connect_to_database(server, database)
                QMessageBox.information(self, 'Success', f'Server: {server}\nDatabase: {database}')
            except Exception as e:
                QMessageBox.critical(self, 'Connection Error', f'Error al conectar a la base de datos. Intenta poner otro servidor')
        else:
            QMessageBox.warning(self, 'Input Error', f'Se necesitan los datos del servidor y el nombre que se le quiere dar a la base de datos.')