# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(880, 425)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: #FFFFFF;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #111111;\n"
"}\n"
"\n"
"QScrollArea{\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"	background-color: #EDEEFF;\n"
"	width: 3px;\n"
"}\n"
"QScrollBar:horizontal{\n"
"	height: 3px;\n"
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
"	disply: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-right: 2px solid #EDEEFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: #111111;\n"
"	border:none;\n"
"	background:none;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	color: #000080;\n"
"	padding: 10px 20px;\n"
"}\n"
"QPushButton:active,\n"
"QPushButton:hover,\n"
"QPushButton:checked{\n"
"	border-right: 3px solid #000080;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settings_btn = QPushButton(self.frame)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 0))
        self.settings_btn.setStyleSheet(u"")
        self.settings_btn.setCheckable(True)
        self.settings_btn.setChecked(True)

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.settings_content = QFrame(Dialog)
        self.settings_content.setObjectName(u"settings_content")
        self.settings_content.setStyleSheet(u"#screen_capture_title{\n"
"	font-size:24px;\n"
"	font-weight: 700;\n"
"}")
        self.settings_content.setFrameShape(QFrame.StyledPanel)
        self.settings_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.settings_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, -1, -1, -1)
        self.screen_capture_title = QLabel(self.settings_content)
        self.screen_capture_title.setObjectName(u"screen_capture_title")

        self.verticalLayout.addWidget(self.screen_capture_title)

        self.scrollArea_2 = QScrollArea(self.settings_content)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.scrollArea_2.setFocusPolicy(Qt.ClickFocus)
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(False)
        self.items = QWidget()
        self.items.setObjectName(u"items")
        self.items.setGeometry(QRect(0, 0, 639, 438))
        self.items.setStyleSheet(u"QWidget{\n"
"	border: 2px solid #EDEEFF;\n"
"	border-radius:  5px;\n"
"}\n"
"#items{\n"
"	border: none\n"
"}\n"
"QWidget:focus{\n"
"	border: 2px solid #000080;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.items)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 12, 0, -1)
        self.screen_capture_active = QWidget(self.items)
        self.screen_capture_active.setObjectName(u"screen_capture_active")
        self.screen_capture_active.setEnabled(True)
        self.screen_capture_active.setMinimumSize(QSize(263, 163))
        self.screen_capture_active.setMaximumSize(QSize(263, 16777215))
        self.screen_capture_active.setMouseTracking(False)
        self.screen_capture_active.setTabletTracking(False)
        self.screen_capture_active.setFocusPolicy(Qt.NoFocus)
        self.screen_capture_active.setAcceptDrops(False)
        self.screen_capture_active.setAutoFillBackground(False)
        self.screen_capture_active.setStyleSheet(u"QLabel,\n"
"QRadioButton{\n"
"	border: none;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.screen_capture_active)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(24, 24, 24, 24)
        self.screen_capture_active_btn = QRadioButton(self.screen_capture_active)
        self.buttonGroup = QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.screen_capture_active_btn)
        self.screen_capture_active_btn.setObjectName(u"screen_capture_active_btn")
        self.screen_capture_active_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.screen_capture_active_btn.setChecked(True)

        self.verticalLayout_7.addWidget(self.screen_capture_active_btn)

        self.screen_capture_active_title = QLabel(self.screen_capture_active)
        self.screen_capture_active_title.setObjectName(u"screen_capture_active_title")
        self.screen_capture_active_title.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;")

        self.verticalLayout_7.addWidget(self.screen_capture_active_title)

        self.screen_capture_active_desc = QLabel(self.screen_capture_active)
        self.screen_capture_active_desc.setObjectName(u"screen_capture_active_desc")
        self.screen_capture_active_desc.setStyleSheet(u"font-size: 14px;\n"
"")
        self.screen_capture_active_desc.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.screen_capture_active_desc)


        self.horizontalLayout_2.addWidget(self.screen_capture_active, 0, Qt.AlignTop)

        self.screen_capture_all = QWidget(self.items)
        self.screen_capture_all.setObjectName(u"screen_capture_all")
        self.screen_capture_all.setEnabled(True)
        self.screen_capture_all.setMinimumSize(QSize(263, 163))
        self.screen_capture_all.setMaximumSize(QSize(263, 16777215))
        self.screen_capture_all.setStyleSheet(u"\n"
"QLabel,\n"
"QRadioButton{\n"
"	border: none;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.screen_capture_all)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(24, 24, 24, 24)
        self.screen_capture_all_btn = QRadioButton(self.screen_capture_all)
        self.buttonGroup.addButton(self.screen_capture_all_btn)
        self.screen_capture_all_btn.setObjectName(u"screen_capture_all_btn")

        self.verticalLayout_6.addWidget(self.screen_capture_all_btn)

        self.screen_capture_all_title = QLabel(self.screen_capture_all)
        self.screen_capture_all_title.setObjectName(u"screen_capture_all_title")
        self.screen_capture_all_title.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;")

        self.verticalLayout_6.addWidget(self.screen_capture_all_title)

        self.screen_capture_all_desc = QLabel(self.screen_capture_all)
        self.screen_capture_all_desc.setObjectName(u"screen_capture_all_desc")
        self.screen_capture_all_desc.setStyleSheet(u"font-size: 14px;\n"
"")
        self.screen_capture_all_desc.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.screen_capture_all_desc)


        self.horizontalLayout_2.addWidget(self.screen_capture_all, 0, Qt.AlignLeft|Qt.AlignTop)

        self.scrollArea_2.setWidget(self.items)

        self.verticalLayout.addWidget(self.scrollArea_2)


        self.horizontalLayout.addWidget(self.settings_content)


        self.retranslateUi(Dialog)
        self.screen_capture_active_btn.toggled.connect(self.screen_capture_active.setFocus)
        self.screen_capture_all_btn.toggled.connect(self.screen_capture_all.setFocus)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.settings_btn.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.screen_capture_title.setText(QCoreApplication.translate("Dialog", u"Screen capture", None))
        self.screen_capture_active_btn.setText("")
        self.screen_capture_active_title.setText(QCoreApplication.translate("Dialog", u"Capture Active Monitorabel", None))
        self.screen_capture_active_desc.setText(QCoreApplication.translate("Dialog", u"Monitor that contains the active application", None))
        self.screen_capture_all_btn.setText("")
        self.screen_capture_all_title.setText(QCoreApplication.translate("Dialog", u"Capture All Monitor", None))
        self.screen_capture_all_desc.setText(QCoreApplication.translate("Dialog", u"All connected monitors", None))
    # retranslateUi

