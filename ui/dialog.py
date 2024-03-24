import time

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from .auth_ui import Ui_Auth
from storage.queries.inserts import auth

class AuthDialog(QDialog, Ui_Auth):
    def __init__(self):
        super(AuthDialog, self).__init__()
        self.setupUi(self)

        self.login.clicked.connect(self.auth)

    def auth(self):
        username = self.username.text()
        password = self.password.text()
        if username == 'admin' and password == 'admin':
            auth()
            self.accept()
            self.close()


