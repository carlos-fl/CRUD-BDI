from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.create_tables_button = QPushButton('CREAR TABLAS', self)
        self.create_tables_button.clicked.connect(self.open_create_tables_window)

        self.create_users_button = QPushButton('CREAR USUARIOS', self)
        self.create_users_button.clicked.connect(self.open_create_users_window)

        self.join_user_button = QPushButton('UNIRSE COMO USUARIO', self)
        self.join_user_button.clicked.connect(self.open_join_user_window)

        self.fill_tables_button = QPushButton('LLENAR TABLAS', self)
        self.fill_tables_button.clicked.connect(self.open_fill_tables_window)

        layout = QVBoxLayout()
        layout.addWidget(self.create_tables_button)
        layout.addWidget(self.create_users_button)
        layout.addWidget(self.join_user_button)
        layout.addWidget(self.fill_tables_button)

        self.setLayout(layout)
        self.setWindowTitle('Main Menu')

    def open_create_tables_window(self):
        pass

    def open_create_users_window(self):
        pass

    def open_join_user_window(self):
        pass

    def open_fill_tables_window(self):
        from app.UI.llenar_tablas import FillTablesWindow
        self.fill_table_window = FillTablesWindow()
        self.fill_table_window.show()
