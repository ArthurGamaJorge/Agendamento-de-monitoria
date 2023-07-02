# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmReservas.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_FrmReservas(object):
    def setupUi(self, FrmReservas):
        if not FrmReservas.objectName():
            FrmReservas.setObjectName(u"FrmReservas")
        FrmReservas.resize(860, 681)
        self.centralwidget = QWidget(FrmReservas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grdReserva = QTableWidget(self.centralwidget)
        if (self.grdReserva.rowCount() < 18):
            self.grdReserva.setRowCount(18)
        __qtablewidgetitem = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.grdReserva.setVerticalHeaderItem(17, __qtablewidgetitem17)
        self.grdReserva.setObjectName(u"grdReserva")
        self.grdReserva.setGeometry(QRect(10, 50, 841, 581))
        self.grdReserva.setFocusPolicy(Qt.WheelFocus)
        self.grdReserva.setAcceptDrops(True)
        self.grdReserva.setFrameShape(QFrame.StyledPanel)
        self.grdReserva.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.grdReserva.setRowCount(18)
        self.grdReserva.setColumnCount(0)
        self.grdReserva.horizontalHeader().setVisible(True)
        self.grdReserva.verticalHeader().setVisible(True)
        self.btnAbrir = QPushButton(self.centralwidget)
        self.btnAbrir.setObjectName(u"btnAbrir")
        self.btnAbrir.setGeometry(QRect(175, 10, 75, 23))
        self.btnSalvar = QPushButton(self.centralwidget)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setGeometry(QRect(525, 10, 75, 23))
        FrmReservas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmReservas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 22))
        FrmReservas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmReservas)
        self.statusbar.setObjectName(u"statusbar")
        FrmReservas.setStatusBar(self.statusbar)

        self.retranslateUi(FrmReservas)

        QMetaObject.connectSlotsByName(FrmReservas)
    # setupUi

    def retranslateUi(self, FrmReservas):
        FrmReservas.setWindowTitle(QCoreApplication.translate("FrmReservas", u"Reservas de hor\u00e1rios de computadores", None))
        ___qtablewidgetitem = self.grdReserva.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FrmReservas", u"07:30", None));
        ___qtablewidgetitem1 = self.grdReserva.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FrmReservas", u"08:15", None));
        ___qtablewidgetitem2 = self.grdReserva.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FrmReservas", u"09:00", None));
        ___qtablewidgetitem3 = self.grdReserva.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FrmReservas", u"10:00", None));
        ___qtablewidgetitem4 = self.grdReserva.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FrmReservas", u"10:45", None));
        ___qtablewidgetitem5 = self.grdReserva.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FrmReservas", u"11:30", None));
        ___qtablewidgetitem6 = self.grdReserva.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FrmReservas", u"13:30", None));
        ___qtablewidgetitem7 = self.grdReserva.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FrmReservas", u"14:15", None));
        ___qtablewidgetitem8 = self.grdReserva.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FrmReservas", u"15:00", None));
        ___qtablewidgetitem9 = self.grdReserva.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("FrmReservas", u"16:00", None));
        ___qtablewidgetitem10 = self.grdReserva.verticalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("FrmReservas", u"16:45", None));
        ___qtablewidgetitem11 = self.grdReserva.verticalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("FrmReservas", u"17:30", None));
        ___qtablewidgetitem12 = self.grdReserva.verticalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("FrmReservas", u"18:15", None));
        ___qtablewidgetitem13 = self.grdReserva.verticalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("FrmReservas", u"19:00", None));
        ___qtablewidgetitem14 = self.grdReserva.verticalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("FrmReservas", u"19:45", None));
        ___qtablewidgetitem15 = self.grdReserva.verticalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("FrmReservas", u"20:30", None));
        ___qtablewidgetitem16 = self.grdReserva.verticalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("FrmReservas", u"21:30", None));
        ___qtablewidgetitem17 = self.grdReserva.verticalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("FrmReservas", u"22:15", None));
        self.btnAbrir.setText(QCoreApplication.translate("FrmReservas", u"Abrir", None))
        self.btnSalvar.setText(QCoreApplication.translate("FrmReservas", u"Salvar", None))
    # retranslateUi

