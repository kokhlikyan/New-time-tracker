import time

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from .succes_alert_ui import Ui_Dialog
from storage.queries.inserts import auth


class SuccessAlert(QDialog, Ui_Dialog):
    def __init__(self):
        super(SuccessAlert, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi(self)
        QTimer.singleShot(1500, self.close)
