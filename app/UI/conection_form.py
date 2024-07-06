from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

INFO = dict()

class DatabaseForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(700, 400)

        self.server_label = QLabel('Servidor:', self)
        self.server_input = QLineEdit(self)

        self.port_label = QLabel('Puerto:', self)
        self.port_input = QLineEdit(self)

        self.database_label = QLabel('Nombre base de datos:', self)
        self.database_input = QLineEdit(self)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit_data)

        layout = QVBoxLayout()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)
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
        database_name = self.database_input.text()
        port = self.port_input.text()

        if server and database_name and port:
            try:
                from app.logic.conection import Connection
                con = Connection()
                con.connect_to_database(server, database, port)
                QMessageBox.information(self, 'Success', f'Server: {server}\nDatabase: {database}')
                self.open_options_window(con)
            except Exception as e:
                QMessageBox.critical(self, 'Connection Error', f'Error al conectar a la base de datos. Intenta poner otro servidor u otro puerto: {e}')
        else:
            QMessageBox.warning(self, 'Input Error', 'Se necesitan los datos del servidor y el nombre que se le quiere dar a la base de datos.')

        
    def open_options_window(self,con):
        self.second_window = SecondWindow(con)
        self.second_window.show()
