from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QCheckBox, QMessageBox
import pyodbc

class ManagePermissionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 400)
        self.setWindowTitle('Manage Permissions')

        self.username_label = QLabel('Username:', self)
        self.username_input = QComboBox(self)

        self.database_label = QLabel('Database:', self)
        self.database_combo = QComboBox(self)
        self.database_combo.currentIndexChanged.connect(self.load_tables)

        self.table_label = QLabel('Table:', self)
        self.table_combo = QComboBox(self)

        self.permission_label = QLabel('Permission:', self)
        self.permission_combo = QComboBox(self)
        self.permission_combo.addItems(['GRANT', 'DENY', 'REVOKE'])

        self.select_checkbox = QCheckBox('SELECT', self)
        self.insert_checkbox = QCheckBox('INSERT', self)
        self.update_checkbox = QCheckBox('UPDATE', self)
        self.delete_checkbox = QCheckBox('DELETE', self)

        self.apply_button = QPushButton('Apply', self)
        self.apply_button.clicked.connect(self.apply_permissions)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.apply_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)
        main_layout.addWidget(self.database_label)
        main_layout.addWidget(self.database_combo)
        main_layout.addWidget(self.table_label)
        main_layout.addWidget(self.table_combo)
        main_layout.addWidget(self.permission_label)
        main_layout.addWidget(self.permission_combo)
        main_layout.addWidget(self.select_checkbox)
        main_layout.addWidget(self.insert_checkbox)
        main_layout.addWidget(self.update_checkbox)
        main_layout.addWidget(self.delete_checkbox)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.load_databases_and_users()

    def load_databases_and_users(self):
        from app.UI.conection_form import INFO
        server, database = INFO['server'], INFO['database']
        try:
            conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
            cursor = conn.cursor()

            cursor.execute('SELECT name FROM sys.databases')
            databases = cursor.fetchall()
            self.database_combo.addItems([name[0] for name in databases])

            cursor.execute("SELECT name FROM sys.sql_logins")
            users = cursor.fetchall()
            self.username_input.addItems([user[0] for user in users])

            conn.close()
        except Exception as e:
            self.show_error_message(f"Error loading databases and users: {str(e)}")

    def load_tables(self):
        from app.UI.conection_form import INFO
        self.table_combo.clear()
        database = self.database_combo.currentText()
        server = INFO['server']
        if database:
            try:
                conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
                cursor = conn.cursor()

                cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
                tables = cursor.fetchall()
                self.table_combo.addItems([table[0] for table in tables])

                conn.close()
            except Exception as e:
                self.show_error_message(f"Error loading tables: {str(e)}")

    def apply_permissions(self):
        username = self.username_input.currentText()
        database = self.database_combo.currentText()
        table = self.table_combo.currentText()
        permission_type = self.permission_combo.currentText()
        permissions = self.get_selected_permissions()

        if username and permission_type and permissions and database and table:
            try:
                permission_sql = self.construct_permission_sql(permission_type, permissions, database, table)
                print(f"SQL command to execute: {permission_sql}")
                self.execute_sql(permission_sql)
                self.show_result_message(f"Permissions {permission_type}ed to user: {username} on table: {table} in database: {database}")
            except Exception as e:
                self.show_error_message(f"Error: {str(e)}")
        else:
            self.show_error_message("Please enter a username, select a database, table, and permissions")

    def get_selected_permissions(self):
        permissions = []
        if self.select_checkbox.isChecked():
            permissions.append('SELECT')
        if self.insert_checkbox.isChecked():
            permissions.append('INSERT')
        if self.update_checkbox.isChecked():
            permissions.append('UPDATE')
        if self.delete_checkbox.isChecked():
            permissions.append('DELETE')
        return permissions

    def construct_permission_sql(self, permission_type, permissions, database, table):
        permission_sql = f"USE [{database}];\n"
        if permission_type == 'REVOKE':
            permission_sql += f"{permission_type} {', '.join(permissions)} ON {table} FROM {self.username_input.currentText()};"
        else:
            permission_sql += f"{permission_type} {', '.join(permissions)} ON {table} TO {self.username_input.currentText()};"
        return permission_sql

    def execute_sql(self, sql_command):
        from app.UI.conection_form import INFO
        server = INFO['server']
        try:
            conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Trusted_Connection=yes')
            cursor = conn.cursor()
            cursor.execute(sql_command)
            conn.commit()
            conn.close()
        except Exception as e:
            self.show_error_message(f"Error executing SQL: {str(e)}")

    def show_result_message(self, message):
        QMessageBox.information(self, 'Success', message)

    def show_error_message(self, message):
        QMessageBox.critical(self, 'Error', message)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ManagePermissionsWindow()
    window.show()
    sys.exit(app.exec_())
