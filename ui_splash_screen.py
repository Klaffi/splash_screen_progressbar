# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenVfhnbf.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QMainWindow, QSizePolicy, QVBoxLayout, QWidget)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMinimumSize(QSize(300, 300))
        SplashScreen.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame {\n"
                                     "	background-color: rgb(40, 42, 54);\n"
                                     "	color: #44475a;\n"
                                     "	font: 9pt \"Segoe UI\";\n"
                                     "	border-radius: 120px;\n"
                                     "}")
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 180))
        self.texts.setStyleSheet(u"background: none;")
        self.texts.setFrameShape(QFrame.StyledPanel)
        self.texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.texts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.empty = QFrame(self.texts)
        self.empty.setObjectName(u"empty")
        self.empty.setMinimumSize(QSize(0, 80))
        self.empty.setFrameShape(QFrame.StyledPanel)
        self.empty.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.empty, 1, 0, 1, 1)

        self.frame = QFrame(self.texts)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.version = QLabel(self.frame)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(100, 24))
        self.version.setMaximumSize(QSize(100, 24))
        self.version.setStyleSheet(u"QLabel{ \n"
                                   "	border-radius: 12px;\n"
                                   "	color: #50fa7b;\n"
                                   "	background-color: rgb(68, 71, 90);\n"
                                   "	\n"
                                   "}")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.version)

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1, Qt.AlignHCenter)

        self.title = QLabel(self.texts)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.loading = QLabel(self.texts)
        self.loading.setObjectName(u"loading")
        self.loading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.loading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loading, 3, 0, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalLayout_3.addWidget(self.texts)

        self.verticalLayout_2.addWidget(self.circle_bg)

        self.verticalLayout.addWidget(self.container)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.version.setText(QCoreApplication.translate("SplashScreen", u"v1.0.0 - Beta 1", None))
        self.title.setText(QCoreApplication.translate("SplashScreen", u"Modern GUI for my APP", None))
        self.loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
    # retranslateUi
