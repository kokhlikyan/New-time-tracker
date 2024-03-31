# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'success_alert.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(441, 50)
        Dialog.setMinimumSize(QSize(0, 50))
        Dialog.setMaximumSize(QSize(16777215, 60))
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setWindowOpacity(1.000000000000000)
        Dialog.setStyleSheet(u"background-color: rgba(227, 253, 235, 1);\n"
"border-color: rgba(38, 179, 3, 1);\n"
"color: rgba(60, 118, 61, 1);\n"
"border-radius: 3px\n"
"")
        Dialog.setInputMethodHints(Qt.ImhNoAutoUppercase)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Your data has been saved.", None))
    # retranslateUi

