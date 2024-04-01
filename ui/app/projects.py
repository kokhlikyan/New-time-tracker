import time

from PySide6.QtCore import QSize, Qt, QCoreApplication, QObject, QTimer
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QPlainTextEdit, QMessageBox
from observer.main import Observer, Subject
from storage.queries.selects import get_project
from storage.queries.inserts import create_or_update
from helpers.time import format_time
from ui.success_alert import SuccessAlert


class Projects(QObject):
    def __init__(self, subject, app):
        super().__init__()
        self.subject = subject
        self.app = app
        self.projects = []
        self.project = None
        self.app.header_btn.clicked.connect(self.play_from_header_button)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.unblock_button)

    def render(self):
        for i in range(1, 5):
            self.project = QFrame(self.app.scrollAreaWidgetContents)
            self.project.setObjectName(u"project")
            self.project.setMaximumSize(QSize(16777215, 16777215))
            self.project.setAutoFillBackground(False)
            self.project.setStyleSheet(u"#project_frame{\n"
                                       "	border-radius: 0;\n"
                                       "}")
            self.project.setFrameShape(QFrame.StyledPanel)
            self.project.setFrameShadow(QFrame.Raised)
            self.verticalLayout_9 = QVBoxLayout(self.project)
            self.verticalLayout_9.setObjectName(u"verticalLayout_9")
            self.verticalLayout_9.setContentsMargins(-1, 12, -1, 12)
            self.project_frame = QFrame(self.project)
            self.project_frame.setObjectName(u"project_frame")
            self.project_frame.setStyleSheet(u"")
            self.project_frame.setFrameShape(QFrame.StyledPanel)
            self.project_frame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_5 = QVBoxLayout(self.project_frame)
            self.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.project_frame_top = QFrame(self.project_frame)
            self.project_frame_top.setObjectName(u"project_frame_top")
            self.project_frame_top.setMinimumSize(QSize(0, 28))
            self.project_frame_top.setMaximumSize(QSize(16777215, 28))
            self.project_frame_top.setStyleSheet(u"background: none;")
            self.project_frame_top.setFrameShape(QFrame.StyledPanel)
            self.project_frame_top.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_5 = QHBoxLayout(self.project_frame_top)
            self.horizontalLayout_5.setSpacing(0)
            self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
            self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.project_control_frame = QFrame(self.project_frame_top)
            self.project_control_frame.setObjectName(u"project_control_frame")
            self.project_control_frame.setFrameShape(QFrame.StyledPanel)
            self.project_control_frame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_6 = QHBoxLayout(self.project_control_frame)
            # ifndef Q_OS_MAC
            self.horizontalLayout_6.setSpacing(-1)
            # endif
            self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
            self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.project_btn = QPushButton(self.project_control_frame)
            self.project_btn.setObjectName(u"project_btn")
            self.project_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.project_btn.setStyleSheet(u"border: none;")
            icon1 = QIcon()
            icon1.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
            icon1.addFile(u":/icons/icons/stop.svg", QSize(), QIcon.Active, QIcon.On)
            self.project_btn.setIcon(icon1)
            self.project_btn.setIconSize(QSize(28, 28))
            self.project_btn.setCheckable(True)
            self.project_btn.setChecked(False)

            self.horizontalLayout_6.addWidget(self.project_btn)

            self.project_name = QLabel(self.project_control_frame)
            self.project_name.setObjectName(u"project_name")
            self.project_name.setStyleSheet(u"color: #111111;\n"
                                            "font-size: 16px;\n"
                                            "font-weight: 600;")

            self.horizontalLayout_6.addWidget(self.project_name)

            self.horizontalLayout_5.addWidget(self.project_control_frame, 0, Qt.AlignLeft)

            self.project_time = QLabel(self.project_frame_top)
            self.project_time.setObjectName(u"project_time")
            self.project_time.setStyleSheet(u"color: #AAAAAA;\n"
                                            "	font-size: 14px;\n"
                                            "	font-weight: 500;")

            self.horizontalLayout_5.addWidget(self.project_time, 0, Qt.AlignRight)

            self.verticalLayout_5.addWidget(self.project_frame_top)

            self.project_frame_bottom = QFrame(self.project_frame)
            self.project_frame_bottom.setObjectName(u"project_frame_bottom")
            self.project_frame_bottom.setEnabled(True)
            self.project_frame_bottom.setStyleSheet(u"")
            self.project_frame_bottom.setFrameShape(QFrame.StyledPanel)
            self.project_frame_bottom.setFrameShadow(QFrame.Raised)
            self.verticalLayout_6 = QVBoxLayout(self.project_frame_bottom)
            self.verticalLayout_6.setSpacing(16)
            self.verticalLayout_6.setObjectName(u"verticalLayout_6")
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.project_description_toggle = QPushButton(self.project_frame_bottom)
            self.project_description_toggle.setObjectName(u"project_description_toggle")
            self.project_description_toggle.setLayoutDirection(Qt.RightToLeft)
            self.project_description_toggle.setStyleSheet(u"border:none;\n"
                                                          "color: #111111;\n"
                                                          "font-size: 14px;\n"
                                                          "font-weight: 500;\n"
                                                          "background: none;")
            icon2 = QIcon()
            icon2.addFile(u":/icons/icons/top.svg", QSize(), QIcon.Normal, QIcon.Off)
            icon2.addFile(u":/icons/icons/bottom.svg", QSize(), QIcon.Active, QIcon.On)
            self.project_description_toggle.setIcon(icon2)
            self.project_description_toggle.setCheckable(True)

            self.verticalLayout_6.addWidget(self.project_description_toggle, 0, Qt.AlignRight)

            self.project_description = QPlainTextEdit(self.project_frame_bottom)
            self.project_description.setObjectName(u"project_description")
            self.project_description.setMinimumSize(QSize(0, 100))
            self.project_description.setMaximumSize(QSize(16777215, 100))
            self.project_description.setStyleSheet(u"color: #AAAAAA;\n"
                                                   "font-size: 14px;\n"
                                                   "font-weight: 400;\n"
                                                   "border: 1px solid #AAAAAA;\n"
                                                   "border-radius: 5px;\n"
                                                   "padding: 12px;")

            self.verticalLayout_6.addWidget(self.project_description)

            self.project_description_save = QPushButton(self.project_frame_bottom)
            self.project_description_save.setObjectName(u"project_description_save")
            self.project_description_save.setCursor(QCursor(Qt.PointingHandCursor))
            self.project_description_save.setMouseTracking(False)
            self.project_description_save.setStyleSheet(u"border: none;\n"
                                                        "color: #000080;\n"
                                                        "font-size: 14px;\n"
                                                        "font-weight: 700;\n"
                                                        "text-decoration: underline;\n"
                                                        "background: none;")
            self.project_description_save.setCheckable(True)

            self.verticalLayout_6.addWidget(self.project_description_save, 0, Qt.AlignLeft)

            self.verticalLayout_5.addWidget(self.project_frame_bottom, 0, Qt.AlignTop)

            self.verticalLayout_9.addWidget(self.project_frame)

            self.project_line_5 = QFrame(self.app.scrollAreaWidgetContents)
            self.project_line_5.setObjectName(u"project_line_5")
            self.project_line_5.setMinimumSize(QSize(0, 2))
            self.project_line_5.setStyleSheet(u"border:none;")
            self.project_line_5.setFrameShape(QFrame.StyledPanel)
            self.project_line_5.setFrameShadow(QFrame.Raised)
            self.verticalLayout_28 = QVBoxLayout(self.project_line_5)
            self.verticalLayout_28.setObjectName(u"verticalLayout_28")
            self.verticalLayout_28.setContentsMargins(12, 0, 12, 0)
            self.line_9 = QLabel(self.project_line_5)
            self.line_9.setObjectName(u"line_9")
            self.line_9.setMinimumSize(QSize(0, 2))
            self.line_9.setMaximumSize(QSize(16777215, 2))
            self.line_9.setStyleSheet(u"background-color: #EDEEFF;")

            self.verticalLayout_28.addWidget(self.line_9)

            self.app.verticalLayout_4.addWidget(self.project_line_5)

            self.app.verticalLayout_4.addWidget(self.project)
            self.project_description_toggle.toggle()
            self.project_description.hide()
            self.project_description_save.hide()
            self.project_description_toggle.toggled.connect(self.project_description.setHidden)
            self.project_description_toggle.toggled.connect(self.project_description_save.setHidden)
            self.project_btn.setText("")
            self.project_name.setText(QCoreApplication.translate("MainWindow", f"Project {i}", None))
            self.project_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
            self.project_description_toggle.setText(QCoreApplication.translate("MainWindow", u"Description ", None))
            self.project_description.setPlainText("")
            self.project_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
            self.project_description_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
            self.projects.append(self.project)
            self.project_btn.toggled.connect(self.play)
            self.project_description_save.clicked.connect(self.save_description)

    def play(self):
        sender = self.sender()

        self.subject.set_status()
        self.subject.add_or_update_project(sender.parent().parent().parent())
        self.switch_enabled(sender)
        self.block_button()
        if sender.isChecked() is False:
            self.subject.stop()

    def block_button(self):
        self.sender().setEnabled(False)
        self.timer.start(500)

    def unblock_button(self):
        btn = self.subject.get_project().findChild(QPushButton, "project_btn")
        btn.setEnabled(True)

    def play_from_header_button(self):
        btn = self.subject.get_project().findChild(QPushButton, "project_btn")
        btn.toggle()
        self.switch_enabled(btn)

    def save_description(self):
        project_name = self.sender().parent().parent().findChild(QLabel, 'project_name').text()
        project = get_project(project_name)
        current_time = 0
        if project is not None:
            current_time = project.time
        description = self.sender().parent().findChild(QPlainTextEdit, 'project_description')
        create_or_update(project_name, time=current_time, description=description.toPlainText())
        alert = SuccessAlert()
        alert.exec_()


    def switch_enabled(self, sender):
        for project in self.projects:
            for child_btn in project.findChildren(QPushButton, "project_btn"):
                if child_btn != sender:
                    project.setEnabled(not sender.isChecked())

    def update_projects(self):
        for project in self.projects:
            for project_name in project.findChildren(QLabel, "project_name"):
                saved_project = get_project(project_name.text())
                if saved_project is not None:
                    project_time = project.findChild(QLabel, "project_time")
                    project_description = project.findChild(QPlainTextEdit, "project_description")
                    track_time = format_time(saved_project.time)
                    project_time.setText(QCoreApplication.translate("MainWindow", track_time, None))
                    project_description.setPlainText(saved_project.description)

    def update(self, subject: Subject) -> None:
        self.subject = subject
        if subject.get_project_name() is None:
            self.update_projects()
            self.app.header_btn.setEnabled(False)
        else:
            self.app.header_btn.setEnabled(True)
            project = subject.get_project()
            if subject.get_status():
                self.app.header_btn.setChecked(True)
                project.parent().setStyleSheet('background-color: #EDEEFF')
            else:
                self.app.header_btn.setChecked(False)
                project.parent().setStyleSheet('background-color: #FFFFFF')
