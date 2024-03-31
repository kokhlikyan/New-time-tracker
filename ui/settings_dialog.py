import time

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from .settings_ui import Ui_Dialog
from storage.queries.inserts import auth


class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setupUi(self)

