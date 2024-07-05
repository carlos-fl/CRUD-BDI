import sys
from PyQt5.QtWidgets import QApplication
from app.UI.conection_form import DatabaseForm 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DatabaseForm()
    sys.exit(app.exec_())
