from PySide6.QtCore import QObject

from observer.main import Observer, Subject
from ui.settings_dialog import SettingsDialog


class Settings(QObject):
    def __init__(self, app):
        super().__init__()
        self.subject = None
        self.app = app
        self.dialog = SettingsDialog()
        self.app.settings.clicked.connect(self.open)
        self.dialog.screen_capture_active.setFocus()
        self.dialog.screen_capture_active_btn.toggled.connect(self.set_active)
        self.dialog.screen_capture_all_btn.toggled.connect(self.set_active)

    def open(self):
        self.dialog.exec()

    def set_active(self):
        if self.sender().isChecked():
            if self.sender().parent().objectName() == 'screen_capture_all':
                self.subject.set_monitor('all')
            elif self.sender().parent().objectName() == 'screen_capture_active':
                self.subject.set_monitor('active')

    def switcher(self):
        sender = self.sender()
        parent = sender.parent()

    def update(self, subject: Subject) -> None:
        self.subject = subject

