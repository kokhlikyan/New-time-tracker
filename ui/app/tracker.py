import logging
import threading
import time

from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton

from events.screenshot_taker import ScreenshotTaker
from events.timer import Timer
from observer.main import ConcreteSubject, Subject
from ui.app.projects import Projects
from ui.app.settings import Settings
from ui.dialog import AuthDialog
from ui.main_ui import Ui_MainWindow
from events.mouse_events import MouseListener
from events.keyboard_events import KeyboardMonitor
from storage.queries.deletes import delete_session
from storage.queries.selects import select_session


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        # UI

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.logout.clicked.connect(self.logout)
        self.subject = ConcreteSubject(self.ui)

        self.projects = Projects(self.subject, self.ui)
        self.projects.render()

        self.settings = Settings(self.ui)

        self.timer = Timer(self.subject)
        self.mouse_thread = MouseListener()
        self.screenshot_taker = ScreenshotTaker(self)
        self.subject.attach(self.projects)
        self.subject.attach(self.settings)
        self.subject.attach(self.timer)
        self.subject.attach(self.mouse_thread)
        self.subject.attach(self.screenshot_taker)
        self.subject.notify()



    def __del__(self):
        print('deleted')

    def closeEvent(self, event):
        super().closeEvent(event)
        self.subject.stop()
        self.mouse_thread.stop_listener()

    def logout(self):
        session = select_session()
        delete_session(session.id)
        auth_dialog = AuthDialog()
        self.close()

        if auth_dialog.exec() == QDialog.Accepted:
            self.show()
