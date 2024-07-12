from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.create_tables_button = QPushButton('CREAR TABLAS', self)
        self.create_tables_button.clicked.connect(self.open_create_tables_window)

        self.manage_users_button = QPushButton('MANEJAR PERMISOS DE USUARIOS', self)
        self.manage_users_button.clicked.connect(self.open_manage_users_window)

        self.join_user_button = QPushButton('UNIRSE COMO USUARIO', self)
        self.join_user_button.clicked.connect(self.open_join_user_window)

        self.fill_tables_button = QPushButton('LLENAR TABLAS', self)
        self.fill_tables_button.clicked.connect(self.open_fill_tables_window)

        layout = QVBoxLayout()
        layout.addWidget(self.create_tables_button)
        layout.addWidget(self.manage_users_button)
        layout.addWidget(self.join_user_button)
        layout.addWidget(self.fill_tables_button)

        self.setLayout(layout)
        self.setWindowTitle('Main Menu')

    def open_create_tables_window(self):
        from app.UI.table_creation_form import TableCreationForm
        self.table_creation_form = TableCreationForm()
        self.table_creation_form.show()
        pass

    def open_manage_users_window(self):
        from app.UI.conceder_permisos import ManagePermissionsWindow
        self.manage_permissions_window = ManagePermissionsWindow()
        self.manage_permissions_window.show()

    def open_join_user_window(self):
        pass

    def open_fill_tables_window(self):
        from app.UI.llenar_tablas import FillTablesWindow
        self.fill_table_window = FillTablesWindow()
        self.fill_table_window.show()

    # Función para abrir la ventana de login
    def open_join_user_window(self):
        from login import LoginWindow  # Importa la clase LoginWindow desde login.py
        self.login_window = LoginWindow()  # Crea una instancia de la ventana de login
        self.login_window.show()  # Muestra la ventana de login