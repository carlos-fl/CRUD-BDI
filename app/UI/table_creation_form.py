from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QComboBox, QGridLayout

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

        column1_label = QLabel("Columna 1:")
        self.column1_name_edit = QLineEdit()
        self.column1_type_combo = QComboBox()
        self.column1_type_combo.addItem("int")
        self.column1_type_combo.addItem("varchar")
        self.column1_type_combo.addItem("datetime")
        self.column_grid.addWidget(column1_label, 0, 0)
        self.column_grid.addWidget(self.column1_name_edit, 0, 1)
        self.column_grid.addWidget(self.column1_type_combo, 0, 2)

        column2_label = QLabel("Columna 2:")
        self.column2_name_edit = QLineEdit()
        self.column2_type_combo = QComboBox()
        self.column2_type_combo.addItem("int")
        self.column2_type_combo.addItem("varchar")
        self.column2_type_combo.addItem("datetime")
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
        column_label = QLabel(f"Columna {column_num}:")
        column_name_edit = QLineEdit()
        column_type_combo = QComboBox()
        column_type_combo.addItem("int")
        column_type_combo.addItem("varchar")
        column_type_combo.addItem("datetime")
        # Antes de poder insertar los nuevos campos y de columnas se deben quitar los botones
        # de agregar campo y crear tabla
        # Luego agregar los los widgets de los nuevos campos 
        # Y finalmente volver a ubicar los botones de agregar campo y crear tabla.
        widget = self.column_grid.itemAtPosition(column_num-1,0).widget()
        self.column_grid.removeWidget(widget)

        self.column_grid.addWidget(column_label, column_num, 0)
        self.column_grid.addWidget(column_name_edit, column_num, 1)
        self.column_grid.addWidget(column_type_combo, column_num, 2)

        add_column_button = QPushButton("Agregar Columna")
        add_column_button.clicked.connect(self.addColumn)
        self.column_grid.addWidget(add_column_button, column_num+1, 0, 1, 3)

    def createTable(self):
        pass

