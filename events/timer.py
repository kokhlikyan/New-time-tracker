import threading
import time

from PySide6.QtCore import QTime, QCoreApplication
from PySide6.QtWidgets import QLabel, QFrame

from observer.main import Observer, Subject
from storage.queries.inserts import create_or_update
from storage.queries.selects import get_project
from helpers.time import format_time, format_qtime, qtime_to_seconds


class Timer(threading.Thread, Observer):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Timer.__instance = None
        print('Timer deleted')

    def __init__(self, subject):
        super(Timer, self).__init__()

        self.last_project_name = None
        self.last_project = None
        self.current_project = None
        self.project = None
        self.subject = subject
        self.app = subject.get_app()
        self.second = 0
        self.formatted_time = '00:00:00'
        self.stop_flag = threading.Event()
        self.elapsed_time = QTime(0, 0)
        if self.last_project:
            self.elapsed_time = qtime_to_seconds(self.last_project.time)

    def run(self):
        self.stop_flag.clear()
        thr = threading.Thread(target=self.run_timer, daemon=True, name='Timer runner')
        thr.start()

    def run_timer(self):
        while not self.stop_flag.is_set():
            self.formatted_time = format_time(self.second)
            self.update_time()
            time.sleep(1)

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        project_time = self.project.findChild(QLabel, "project_time")
        project_time.setText(format_time(qtime_to_seconds(self.elapsed_time)))
        self.app.header_time.setText(format_time(qtime_to_seconds(self.elapsed_time)))

    def stop(self):
        self.stop_flag.set()

    def update(self, subject: Subject) -> None:
        self.current_project = subject.get_project_name()
        self.last_project_name = subject.get_last_project_name()
        self.project = subject.get_project()
        if self.current_project is not None:
            if subject.get_status():
                active_project = get_project(self.current_project)
                self.elapsed_time = format_qtime(active_project.time if active_project else 0)
                self.run()
            else:
                self.stop()
                create_or_update(
                    project_name=self.current_project,
                    time=qtime_to_seconds(self.elapsed_time),
                )
                project = get_project(self.current_project)
                project_time = self.project.findChild(QLabel, "project_time")
                project_time.setText(format_time(project.time))
