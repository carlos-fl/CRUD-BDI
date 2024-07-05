from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit

class FillTablesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Fill Tables')

        from app.UI.conection_form import INFO
        from app.logic.conection import Connection

        try:
            SERVER, DATABASE, PORT = INFO['server'], INFO['database'], INFO['port']
            con = Connection().connect_to_database(SERVER, DATABASE, PORT)
            cursor = con.cursor()
            tables = cursor.execute('SELECT * FROM INFORMATION_SCHEMA.TABLES').fetchmany()
            print(tables)
        except Exception as e:
            print(e)
            tables = []

        self.table_label = QLabel('Select Table:', self)
        self.table_dropdown = QComboBox(self)
        self.table_dropdown.addItems(tables)

        self.create_button = QPushButton('CREAR', self)
        self.update_button = QPushButton('ACTUALIZAR', self)
        self.delete_button = QPushButton('BORRAR', self)
        self.view_button = QPushButton('VER', self)

        layout = QVBoxLayout()
        layout.addWidget(self.table_label)
        layout.addWidget(self.table_dropdown)
        layout.addWidget(self.view_button)
        layout.addWidget(self.create_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

        self.view_button.clicked.connect(self.show_view_layout)
        self.create_button.clicked.connect(self.show_create_layout)
        self.update_button.clicked.connect(self.show_update_layout)
        self.delete_button.clicked.connect(self.show_delete_layout)

    def show_view_layout(self):
        self.clear_layout()
        self.result_label = QLabel('Aquí se verá "SELECT * FROM table"', self)
        self.layout().addWidget(self.result_label)

    def show_create_layout(self):
        self.clear_layout()
        self.fields_label = QLabel('Mostrar campos para crear entrada', self)
        self.fields_input = QLineEdit(self)
        self.save_button = QPushButton('Guardar', self)

        self.layout().addWidget(self.fields_label)
        self.layout().addWidget(self.fields_input)
        self.layout().addWidget(self.save_button)

    def show_update_layout(self):
        self.clear_layout()
        self.id_label = QLabel('Mostrar input de ID', self)
        self.id_input = QLineEdit(self)
        self.fields_label = QLabel('Mostrar campos para actualizar entrada', self)
        self.fields_input = QLineEdit(self)
        self.save_button = QPushButton('Guardar', self)

        self.layout().addWidget(self.id_label)
        self.layout().addWidget(self.id_input)
        self.layout().addWidget(self.fields_label)
        self.layout().addWidget(self.fields_input)
        self.layout().addWidget(self.save_button)

    def show_delete_layout(self):
        self.clear_layout()
        self.id_label = QLabel('Campo ID', self)
        self.id_input = QLineEdit(self)
        self.delete_button = QPushButton('Borrar', self)

        self.layout().addWidget(self.id_label)
        self.layout().addWidget(self.id_input)
        self.layout().addWidget(self.delete_button)

    def clear_layout(self):
        for i in reversed(range(self.layout().count())):
            widget = self.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
