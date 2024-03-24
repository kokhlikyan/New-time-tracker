# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ui.resources

class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(448, 548)
        Auth.setStyleSheet(u"QDialog{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QFrame{\n"
"	border: none;\n"
"}\n"
"QLineEdit{\n"
"	color:  #AAAAAA;\n"
"	border: 1px solid #AAAAAA;\n"
"	border-radius: 5px;\n"
"	background-color: #FFFFFF;\n"
"	padding: 0 16px;\n"
"}\n"
"Line{\n"
"	background-color:  #EDEEFF;\n"
"}")
        self.gridLayout = QGridLayout(Auth)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(Auth)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 320))
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setStyleSheet(u"QLabel {\n"
"	color: #111111;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 12)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"font-size: 32px;\n"
"font-weight: bold;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 102))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 102))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_3)

        self.username = QLineEdit(self.frame_6)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 50))
        self.username.setMaximumSize(QSize(16777215, 50))
        self.username.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_3.addWidget(self.username)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.gridLayout_2.addWidget(self.frame_7, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 52))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.login = QPushButton(self.frame_8)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(0, 50))
        self.login.setMaximumSize(QSize(16777215, 50))
        self.login.setCursor(QCursor(Qt.PointingHandCursor))
        self.login.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #000080;\n"
"border-radius: 5px;\n"
"font-size: 18px;\n"
"font-weight:500;")

        self.verticalLayout_4.addWidget(self.login)


        self.gridLayout_2.addWidget(self.frame_8, 4, 1, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 102))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setMargin(0)

        self.verticalLayout.addWidget(self.label_2)

        self.password = QLineEdit(self.frame_5)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 50))
        self.password.setMaximumSize(QSize(16777215, 50))
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password)


        self.gridLayout_2.addWidget(self.frame_5, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Auth)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background: none;\n"
"	border-radius: 5px;\n"
"	font-size: 18px;\n"
"	border: 2px solid #EDEEFF;\n"
"	font-weight: 500;\n"
"	text-align:  left;\n"
"	padding-left: 16px;\n"
"	\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(175, 178, 178);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 20, 399, 1))
        self.label_5.setMinimumSize(QSize(0, 1))
        self.label_5.setMaximumSize(QSize(16777215, 1))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, -3, 46, 46))
        self.label_6.setMinimumSize(QSize(46, 46))
        self.label_6.setMaximumSize(QSize(46, 46))
        self.label_6.setStyleSheet(u"background-color:  #FFFFFF;\n"
"color:  #AAAAAA;\n"
"font-size:14px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.frame_3)

        self.google = QPushButton(self.frame_2)
        self.google.setObjectName(u"google")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.google.sizePolicy().hasHeightForWidth())
        self.google.setSizePolicy(sizePolicy)
        self.google.setMinimumSize(QSize(0, 50))
        self.google.setMaximumSize(QSize(16777215, 50))
        self.google.setCursor(QCursor(Qt.PointingHandCursor))
        self.google.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.google.setAutoFillBackground(False)
        self.google.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.google.setIcon(icon)
        self.google.setCheckable(False)
        self.google.setAutoRepeat(True)
        self.google.setAutoExclusive(False)
        self.google.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.google, 0, Qt.AlignVCenter)

        self.apple = QPushButton(self.frame_2)
        self.apple.setObjectName(u"apple")
        self.apple.setMinimumSize(QSize(0, 50))
        self.apple.setMaximumSize(QSize(16777215, 50))
        self.apple.setCursor(QCursor(Qt.PointingHandCursor))
        self.apple.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/apple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.apple.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.apple)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)


        self.retranslateUi(Auth)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Auth", u"Sign in", None))
        self.label_3.setText(QCoreApplication.translate("Auth", u"Username", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Auth", u"Username", None))
        self.login.setText(QCoreApplication.translate("Auth", u"Sign in", None))
        self.label_2.setText(QCoreApplication.translate("Auth", u"Password", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Auth", u"Password", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Auth", u"or", None))
        self.google.setText(QCoreApplication.translate("Auth", u"                    Continue with Google", None))
        self.apple.setText(QCoreApplication.translate("Auth", u"                    Continue with Apple", None))
    # retranslateUi

