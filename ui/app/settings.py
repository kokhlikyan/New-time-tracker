from PySide6.QtCore import QObject
from ui.settings_dialog import SettingsDialog


class Settings(QObject):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.dialog = SettingsDialog()
        self.app.settings.clicked.connect(self.open)
        self.dialog.screen_capture_active.setFocus()

    def open(self):
        self.dialog.exec()

    def switcher(self):
        sender = self.sender()
        parent = sender.parent()
        print(parent.isEnabled())
