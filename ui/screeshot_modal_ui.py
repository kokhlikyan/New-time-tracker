# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenshot_modal.ui'
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
                           QPalette, QPixmap, QRadialGradient, QTransform, QGuiApplication)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)
import ui.resources

class Ui_Screenshot(object):
    def setupUi(self, Screenshot):
        if not Screenshot.objectName():
            Screenshot.setObjectName(u"Screenshot")
        Screenshot.resize(300, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Screenshot.sizePolicy().hasHeightForWidth())
        Screenshot.setSizePolicy(sizePolicy)
        Screenshot.setMinimumSize(QSize(300, 150))
        Screenshot.setMaximumSize(QSize(300, 150))
        Screenshot.setStyleSheet(u"background-color: #FFFFFF;")
        self.horizontalLayout = QHBoxLayout(Screenshot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image = QLabel(Screenshot)
        self.image.setObjectName(u"image")
        self.image.setStyleSheet(u"border-image: url(:/icons/design/icons/bg.png);")

        self.horizontalLayout.addWidget(self.image)


        self.retranslateUi(Screenshot)

        QMetaObject.connectSlotsByName(Screenshot)
        self.move_to_bottom_right()


    def move_to_bottom_right(self):
        screen_rect = QGuiApplication.primaryScreen().geometry()
        dialog_rect = self.geometry()
        self.move(screen_rect.right() - dialog_rect.width() - 10, screen_rect.bottom() - dialog_rect.height() - 100)
    #

    def retranslateUi(self, Screenshot):
        Screenshot.setWindowTitle(QCoreApplication.translate("Screenshot", u"Screenshot", None))
        self.image.setText("")
    # retranslateUi

