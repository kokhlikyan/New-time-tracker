from __future__ import annotations

import logging
import threading
from abc import ABC, abstractmethod

from PySide6.QtWidgets import QFrame, QLabel

from storage.models import Session
from storage.queries.selects import select_session
from typing import List, Optional

from ui.main_ui import Ui_MainWindow


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def add_or_update_project(self, project: QFrame) -> None:
        pass

    @abstractmethod
    def get_project(self) -> QFrame:
        pass

    @abstractmethod
    def get_project_name(self) -> str:
        pass

    @abstractmethod
    def get_last_project(self) -> Optional[QFrame]:
        pass

    @abstractmethod
    def get_last_project_name(self) -> Optional[str]:
        pass

    @abstractmethod
    def set_status(self, ) -> None:
        pass

    @abstractmethod
    def stop(self, ) -> None:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass

    @abstractmethod
    def get_app(self) -> Ui_MainWindow:
        pass

    @abstractmethod
    def get_session(self) -> Session:
        pass

    @abstractmethod
    def monitor(self) -> str:
        pass

    @abstractmethod
    def set_monitor(self, monitor_type: str) -> None:
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer] = []
    _app = None
    _session = None
    _project = None
    _last_project = None
    _project_name = None
    _status = False
    _last_project_name = None
    _monitor = 'active'

    def __init__(self, app):
        self._app = app
        self._session = select_session()

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def add_or_update_project(self, project: QFrame) -> None:
        tmp_project_name = project.parent().findChild(QLabel, 'project_name').text()
        if self._last_project_name is None:
            self._project = project
            self._project_name = tmp_project_name
            self._last_project = project
            self._last_project_name = tmp_project_name
        else:
            self._last_project = self._project
            self._last_project_name = self._project_name
            self._project = project
            self._project_name = tmp_project_name
        self.notify()

    def get_project(self) -> QFrame:
        return self._project

    def get_project_name(self) -> str:
        return self._project_name

    def get_last_project(self) -> Optional[QFrame]:
        return self._last_project

    def get_last_project_name(self) -> Optional[str]:
        return self._last_project_name

    def get_app(self) -> Ui_MainWindow:
        return self._app

    def set_status(self) -> None:
        self._status = not self._status

    def stop(self) -> None:
        self._status = False
        self.notify()

    def get_status(self) -> bool:

        return self._status

    def get_session(self) -> Session:
        return self._session

    def monitor(self) -> str:
        return self._monitor

    def set_monitor(self, monitor_type) -> None:
        self._monitor = monitor_type
