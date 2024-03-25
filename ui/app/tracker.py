from PySide6.QtWidgets import QMainWindow, QDialog

from events.timer import Timer
from observer.main import ConcreteSubject
from ui.app.projects import Projects
from ui.app.settings import Settings
from ui.dialog import AuthDialog
from ui.main_ui import Ui_MainWindow
from events.keyboard_events import KeyboardMonitorThread
from events.mouse_events import MouseListener

from storage.queries.deletes import delete_session
from storage.queries.selects import select_session


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        # UI

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.logout.clicked.connect(self.logout)
        self.keyboard_monitor_thread = KeyboardMonitorThread()
        self.subject = ConcreteSubject(self.ui)
        self.projects = Projects(self.subject, self.ui)
        self.projects.render()
        self.settings = Settings(self.ui)

        self.timer = Timer(self.subject)
        self.mouse_thrade = MouseListener()

        self.subject.attach(self.projects)
        self.subject.attach(self.timer)
        self.subject.attach(self.mouse_thrade)
        self.subject.notify()

    def closeEvent(self, event):
        self.subject.set_status()
        self.subject.notify()
        super().closeEvent(event)


    def logout(self):
        session = select_session()
        delete_session(session.id)
        auth_dialog = AuthDialog()
        self.close()

        if auth_dialog.exec() == QDialog.Accepted:
            self.show()
