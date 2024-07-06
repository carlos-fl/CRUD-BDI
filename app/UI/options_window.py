from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from app.UI.create_table_form import TableForm

class SecondWindow(QWidget):
    def __init__(self,connection,db_name):
        super().__init__()
        self.connection = connection
        self.db_name = db_name
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.create_tables_button = QPushButton('CREAR TABLAS', self)
        self.create_tables_button.clicked.connect(self.open_create_tables_window)

        self.manage_users_button = QPushButton('MANEJAR PERMISOS DE USUARIOS', self)
        self.manage_users_button.clicked.connect(self.open_manage_users_window)

        self.join_user_button = QPushButton('UNIRSE COMO USUARIO', self)
        self.join_user_button.clicked.connect(self.open_join_user_window)

        self.fill_tables_button = QPushButton('SELECCIONAR REGISTROS', self)
        self.fill_tables_button.clicked.connect(self.open_select_registries_window)

        self.fill_tables_button = QPushButton('ELIMINAR REGISTROS', self)
        self.fill_tables_button.clicked.connect(self.open_delete_registries_window)

        self.fill_tables_button = QPushButton('INSERTAR REGISTROS', self)
        self.fill_tables_button.clicked.connect(self.open_insert_registries_window)

        layout = QVBoxLayout()
        layout.addWidget(self.create_tables_button)
        layout.addWidget(self.manage_users_button)
        layout.addWidget(self.join_user_button)
        layout.addWidget(self.fill_tables_button)

        self.setLayout(layout)
        self.setWindowTitle('Main Menu')

    def open_create_tables_window(self):
<<<<<<< HEAD
<<<<<<< HEAD
        pass
=======
      self.table_form = TableForm(self.connection);
=======
      self.table_form = TableForm(self.connection,self.db_name);
>>>>>>> e630179 (Includes selection button in options)
      self.table_form.show();

>>>>>>> 345f277 (Includes table creation form)

    def open_manage_users_window(self):
        from app.UI.conceder_permisos import ManagePermissionsWindow
        self.manage_permissions_window = ManagePermissionsWindow()
        self.manage_permissions_window.show()

    def open_join_user_window(self):
        pass

<<<<<<< HEAD
    def open_fill_tables_window(self):
        from app.UI.llenar_tablas import FillTablesWindow
        self.fill_table_window = FillTablesWindow()
        self.fill_table_window.show()
=======
    def open_select_registries_window(self):
        pass

    def open_delete_registries_window(self):
        pass

    def open_insert_registries_window(self):
        pass
>>>>>>> e630179 (Includes selection button in options)
