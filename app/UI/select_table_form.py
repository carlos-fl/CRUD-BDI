from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout,QTextEdit,QLabel, QLineEdit, QPushButton
from app.logic.table import Table

class SelectTable(QWidget):
    def __init__(self,connection,db_name):
        super().__init__()
        self.connection = connection
        self.db_name = db_name
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.textLabel = QLabel("Nombre de Tabla: ")
        self.table_name = QLineEdit()
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        self.select_rows_button = QPushButton('SELECCIONAR', self)
        self.select_rows_button.clicked.connect(self.select)

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.setLayout(self.textLabel)
        #self.setLayout(self.lineEdit)
        self.setLayout(self.textEdit)
        self.layout()
        self.setWindowTitle('Select Registries')

    def select(self):
        table = Table()
        table.select_all(self.database_input.text(),self.connection,self.table_name)
        pass