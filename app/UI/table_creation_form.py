from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QComboBox, QGridLayout, QMessageBox
from app.logic.conection import Connection
import pyodbc
from app.UI.conection_form import INFO
class TableCreationForm (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Create Table")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        table_name_label = QLabel("Nombre de Tabla:")
        self.table_name_edit = QLineEdit()
        layout.addWidget(table_name_label)
        layout.addWidget(self.table_name_edit)

        self.column_grid = QGridLayout()
        layout.addLayout(self.column_grid)

        column1_label = QLabel("Columna:")
        self.column1_name_edit = QLineEdit()
        self.column1_type_combo = QComboBox()
        self.column1_type_combo.addItem("INT")
        self.column1_type_combo.addItem("VARCHAR")
        self.column1_type_combo.addItem("DATETIME")
        self.column_grid.addWidget(column1_label, 0, 0)
        self.column_grid.addWidget(self.column1_name_edit, 0, 1)
        self.column_grid.addWidget(self.column1_type_combo, 0, 2)

        column2_label = QLabel("Columna:")
        self.column2_name_edit = QLineEdit()
        self.column2_type_combo = QComboBox()
        self.column2_type_combo.addItem("INT")
        self.column2_type_combo.addItem("VARCHAR")
        self.column2_type_combo.addItem("DATETIME")
        self.column_grid.addWidget(column2_label, 1, 0)
        self.column_grid.addWidget(self.column2_name_edit, 1, 1)
        self.column_grid.addWidget(self.column2_type_combo, 1, 2)

        add_column_button = QPushButton("Agregar Columna")
        add_column_button.clicked.connect(self.addColumn)
        self.column_grid.addWidget(add_column_button, 2, 0, 1, 3)

        create_table_button = QPushButton("Crear Tabla")
        create_table_button.clicked.connect(self.createTable)
        layout.addWidget(create_table_button)
        self.show()

    def addColumn(self):
        column_num = self.column_grid.rowCount()
        column_label = QLabel("Columna:")
        column_name_edit = QLineEdit()
        column_type_combo = QComboBox()
        column_type_combo.addItem("INT")
        column_type_combo.addItem("VARCHAR")
        column_type_combo.addItem("DATETIME")
        
        widget = self.column_grid.itemAtPosition(column_num-1,0).widget()
        self.column_grid.removeWidget(widget)

        self.column_grid.addWidget(column_label, column_num, 0)
        self.column_grid.addWidget(column_name_edit, column_num, 1)
        self.column_grid.addWidget(column_type_combo, column_num, 2)

        add_column_button = QPushButton("Agregar Columna")
        add_column_button.clicked.connect(self.addColumn)
        self.column_grid.addWidget(add_column_button, column_num+1, 0, 1, 3)

    def createTable(self):
        try:
            tableName = self.table_name_edit.text()
            SERVER, DATABASE, PORT = INFO['server'], INFO['database'], INFO['port']
            conn = Connection().connect_to_database(SERVER, DATABASE, PORT)
            cursor = conn.cursor()

            columns = []
            for row in range(self.column_grid.rowCount()-1):
                column_name = self.column_grid.itemAtPosition(row, 1).widget().text()
                column_type = self.column_grid.itemAtPosition(row, 2).widget().currentText()
                columns.append((column_name, column_type))

            print(columns)
            column_definition = ''
            for column in columns:
                if column[1] == "VARCHAR":
                    column_definition += f"{column[0]} {column[1]}(30), "
                elif column[1] == "INT":
                    column_definition += f"{column[0]} {column[1]}(3), "
            column_definition = column_definition[:-2]

            print(column_definition)
            cursor.execute(f'USE {DATABASE};')
            print(f'CREATE TABLE {tableName} (id INT PRIMARY KEY, {column_definition});')
            cursor.execute(f'CREATE TABLE {tableName} (id INT PRIMARY KEY, {column_definition});')
            conn.commit()
            cursor.close()
            print(f'Tabla {tableName} creada exitosamente')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Error al crear la tabla: {e}')