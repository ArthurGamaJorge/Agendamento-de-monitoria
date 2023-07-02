# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 243)
        self.actionAlunos = QAction(MainWindow)
        self.actionAlunos.setObjectName(u"actionAlunos")
        self.actionComputadores = QAction(MainWindow)
        self.actionComputadores.setObjectName(u"actionComputadores")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.actionQuadro_de_reservas = QAction(MainWindow)
        self.actionQuadro_de_reservas.setObjectName(u"actionQuadro_de_reservas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 10, 312, 183))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 333, 22))
        self.menuCadastros = QMenu(self.menubar)
        self.menuCadastros.setObjectName(u"menuCadastros")
        self.menuConsultas = QMenu(self.menubar)
        self.menuConsultas.setObjectName(u"menuConsultas")
        self.menuSair = QMenu(self.menubar)
        self.menuSair.setObjectName(u"menuSair")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuConsultas.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())
        self.menuCadastros.addAction(self.actionAlunos)
        self.menuCadastros.addAction(self.actionComputadores)
        self.menuCadastros.addSeparator()
        self.menuConsultas.addAction(self.actionQuadro_de_reservas)
        self.menuSair.addAction(self.actionSair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Reservas de Hor\u00e1rios", None))
        self.actionAlunos.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.actionComputadores.setText(QCoreApplication.translate("MainWindow", u"Computadores", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.actionQuadro_de_reservas.setText(QCoreApplication.translate("MainWindow", u"Quadro de reservas", None))
        self.menuCadastros.setTitle(QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.menuConsultas.setTitle(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.menuSair.setTitle(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

