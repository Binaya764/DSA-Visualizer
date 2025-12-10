# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insertion_sort.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1116, 600)
        self.inputArray = QLineEdit(Widget)
        self.inputArray.setObjectName(u"inputArray")
        self.inputArray.setGeometry(QRect(20, 170, 261, 41))
        self.btnGenerate = QPushButton(Widget)
        self.btnGenerate.setObjectName(u"btnGenerate")
        self.btnGenerate.setGeometry(QRect(30, 260, 90, 29))
        self.btnSort = QPushButton(Widget)
        self.btnSort.setObjectName(u"btnSort")
        self.btnSort.setGeometry(QRect(190, 260, 90, 29))
        self.speedSlider = QSlider(Widget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setGeometry(QRect(30, 350, 191, 31))
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(100)
        self.speedSlider.setValue(50)
        self.speedSlider.setOrientation(Qt.Orientation.Horizontal)
        self.graphicsView = QGraphicsView(Widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(290, 0, 821, 381))
        self.statusLabel = QLabel(Widget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(670, 390, 171, 21))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.inputArray.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter numbers separated by commas", None))
        self.btnGenerate.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.btnSort.setText(QCoreApplication.translate("Widget", u"Sort", None))
        self.statusLabel.setText("")
    # retranslateUi

