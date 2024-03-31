import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from .screeshot_modal_ui import Ui_Screenshot
from storage.queries.inserts import auth


class ScreenshotDialog(QDialog, Ui_Screenshot):
    def __init__(self):
        super(ScreenshotDialog, self).__init__()
        # self.setModal(True)
        self.setupUi(self)

