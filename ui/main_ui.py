# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QMainWindow, QPlainTextEdit, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QLayout)
import ui.resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(591, 699)
        MainWindow.setStyleSheet(u"*{\n"
                                 "	background-color: #FFFFFF;\n"
                                 "}\n"
                                 "")
        self.content = QWidget(MainWindow)
        self.content.setObjectName(u"content")
        self.verticalLayout_10 = QVBoxLayout(self.content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.content_frame = QWidget(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.verticalLayout = QVBoxLayout(self.content_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.content_frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 200))
        self.header.setMaximumSize(QSize(16777215, 16777215))
        self.header.setStyleSheet(u"#header{\n"
                                  "	border-radius: 5px;\n"
                                  "	border-image: url(:/icons/icons/bg.png);\n"
                                  "}\n"
                                  "\n"
                                  "#frame{\n"
                                  "	border-radius: 5px;\n"
                                  "	background-color: rgba(0, 0, 0, 102);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton{\n"
                                  "	border: none;\n"
                                  "	background-color: none;\n"
                                  "}")
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setToolTipDuration(1)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(12, 32, 0, 32)
        self.header_time = QLabel(self.frame)
        self.header_time.setObjectName(u"header_time")
        self.header_time.setMaximumSize(QSize(16777215, 42))
        self.header_time.setStyleSheet(u"font-size: 32px;\n"
                                       "color: #FFFFFF;\n"
                                       "font-weight: 900;\n"
                                       "background: none;\n"
                                       "")

        self.verticalLayout_3.addWidget(self.header_time, 0, Qt.AlignHCenter)

        self.header_btn = QPushButton(self.frame)
        self.header_btn.setObjectName(u"header_btn")
        self.header_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.header_btn.setStyleSheet(u"background:none;\n"
                                      "")
        icon = QIcon()
        icon.addFile(u":/icons/icons/light_play.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/light_stop.svg", QSize(), QIcon.Active, QIcon.On)
        self.header_btn.setIcon(icon)
        self.header_btn.setIconSize(QSize(56, 56))
        self.header_btn.setCheckable(True)
        self.header_btn.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.header_btn, 0, Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.header)

        self.projects = QWidget(self.content_frame)
        self.projects.setObjectName(u"projects")
        self.projects.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.projects)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 12, 0, 0)
        self.projects_header = QFrame(self.projects)
        self.projects_header.setObjectName(u"projects_header")
        self.projects_header.setMinimumSize(QSize(0, 0))
        self.projects_header.setStyleSheet(u"QLabel{\n"
                                           "	color: #111111;\n"
                                           "}\n"
                                           "\n"
                                           "#projects_header{\n"
                                           "	border: none;\n"
                                           "}\n"
                                           "")
        self.projects_header.setFrameShape(QFrame.StyledPanel)
        self.projects_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.projects_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.projects_title = QWidget(self.projects_header)
        self.projects_title.setObjectName(u"projects_title")
        self.projects_title.setMinimumSize(QSize(0, 0))
        self.projects_title.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.projects_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 16, 0, 0)
        self.projects_header_title = QLabel(self.projects_title)
        self.projects_header_title.setObjectName(u"projects_header_title")
        self.projects_header_title.setStyleSheet(u"font-size: 20px;\n"
                                                 "font-weight: 700;")

        self.horizontalLayout.addWidget(self.projects_header_title)

        self.time_spent_today = QLabel(self.projects_title)
        self.time_spent_today.setObjectName(u"time_spent_today")

        self.horizontalLayout.addWidget(self.time_spent_today, 0, Qt.AlignRight)

        self.horizontalLayout_2.addWidget(self.projects_title)

        self.verticalLayout_2.addWidget(self.projects_header)

        self.projects_frame = QScrollArea(self.projects)
        self.projects_frame.setObjectName(u"projects_frame")
        self.projects_frame.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.projects_frame.setStyleSheet(u"QScrollArea{\n"
                                          "	border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:vertical{\n"
                                          "	background-color: #EDEEFF;\n"
                                          "	width: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:handle{\n"
                                          "	background-color:  #000080;\n"
                                          "\n"
                                          "}\n"
                                          "QScrollBar:handle:hover,\n"
                                          "QScrollBar:handle:pressed{\n"
                                          "	background-color:  #000180;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical,\n"
                                          "QScrollBar::add-line:vertical{\n"
                                          "	border: none;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "")
        self.projects_frame.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 567, 351))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet(u"QFrame{\n"
                                                    "border-radius: 5px;\n"
                                                    "border: none;\n"
                                                    "}")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.projects_frame.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.projects_frame)

        self.verticalLayout.addWidget(self.projects)

        self.verticalLayout_10.addWidget(self.content_frame)

        self.footer = QWidget(self.content)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 50))
        self.footer.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.footer_frame = QWidget(self.footer)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"border-top: 2px solid #EDEEFF;")
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.footer_frame)
        self.settings.setObjectName(u"settings")
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings.setStyleSheet(u"color: #111111;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: 500;\n"
                                    "border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.settings, 0, Qt.AlignLeft)

        self.logout = QPushButton(self.footer_frame)
        self.logout.setObjectName(u"logout")
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout.setStyleSheet(u"color: #AAAAAA;\n"
                                  "font-size: 16px;\n"
                                  "font-weight: 500;\n"
                                  "border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon4)
        self.logout.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.logout, 0, Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.footer_frame)

        self.verticalLayout_10.addWidget(self.footer)

        MainWindow.setCentralWidget(self.content)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.header_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.header_btn.setText("")
        self.projects_header_title.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.time_spent_today.setText(QCoreApplication.translate("MainWindow", u"Time spent today", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"  Log out", None))
