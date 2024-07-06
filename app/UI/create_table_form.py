from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QComboBox
from app.logic.conection import Connection
#from app.UI.table_fields import TableFields
from app.logic.table import Table
from app.logic.field import Field



class TableForm(QWidget):
    def __init__(self,connection,db_name):
        super().__init__()
        self.connection = connection
        self.db_name = db_name
        self.initUI()
    
    def initUI(self):
        self.resize(700, 400)
        
        #self.label_table_name = QLabel('Nombre de Tabla:', self)
        #self.input_table_name = QLineEdit(self)

        layout = QVBoxLayout()

        # Campo para el nombre de la tabla
        label_table_name = QLabel("Nombre de la tabla:")
        self.table_name_edit = QLineEdit()
        layout.addWidget(label_table_name)
        layout.addWidget(self.table_name_edit)

        self.column_widgets = []
        for i in range(5):  # número de columnas máximas
            column_widget = QWidget()
            column_layout = QVBoxLayout()
            column_widget.setLayout(column_layout)

            label_column_name = QLabel(f"Columna {i+1}:")
            column_name_edit = QLineEdit()
            column_layout.addWidget(label_column_name)
            column_layout.addWidget(column_name_edit)

            label_data_type = QLabel("Tipo de datos:")
            data_type_combo = QComboBox()
            data_type_combo.addItem("INT")
            data_type_combo.addItem("VARCHAR")
            data_type_combo.addItem("DATE")
            column_layout.addWidget(label_data_type)
            column_layout.addWidget(data_type_combo)

            self.column_widgets.append((column_widget, column_name_edit, data_type_combo))

            layout.addWidget(column_widget)

        self.submit_button = QPushButton('Siguiente', self)
        self.submit_button.clicked.connect(self.next)


        # Set layout
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.setWindowTitle('Table Creation Form')
        self.show()

    def next(self):
            self.fields = []
            for i in range(5):
                column_widget, column_name_edit, data_type_combo = self.column_widgets[i]
                column_name = column_name_edit.text()
                data_type = data_type_combo.currentText()
                field = Field(column_name, data_type)
                self.fields.append(field)
            table = Table()
            table.create(self.db_name,self.table_name_edit.text(),self.connection,self.fields)






