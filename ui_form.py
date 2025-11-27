# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(609, 330)
        self.horizontalLayout_14 = QHBoxLayout(Widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_11.addWidget(self.frame)

        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMaximumSize(QSize(900, 450))

        self.verticalLayout.addWidget(self.graphicsView)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.Btnstart = QPushButton(self.widget)
        self.Btnstart.setObjectName(u"Btnstart")

        self.horizontalLayout.addWidget(self.Btnstart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setSizeIncrement(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalSlider = QSlider(self.frame_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_13.addWidget(self.horizontalSlider)


        self.verticalLayout_16.addLayout(self.verticalLayout_13)


        self.verticalLayout_12.addWidget(self.frame_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_12)


        self.horizontalLayout_11.addWidget(self.widget)

        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2)

        self.size_array_lineEdit = QLineEdit(self.groupBox_2)
        self.size_array_lineEdit.setObjectName(u"size_array_lineEdit")

        self.verticalLayout_9.addWidget(self.size_array_lineEdit)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.Btnrandomize = QPushButton(self.groupBox_2)
        self.Btnrandomize.setObjectName(u"Btnrandomize")

        self.horizontalLayout_15.addWidget(self.Btnrandomize)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_14.addWidget(self.label_4)

        self.graphicsView_2 = QGraphicsView(self.frame_3)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_14.addWidget(self.graphicsView_2)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_11.addWidget(self.frame_2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Data Structures", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Algorithms", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Widget", u"Sorting", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Widget", u"Bubble Sort", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Widget", u"Insertion Sort", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Widget", u"Searching", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Linked List", None))

        self.Btnstart.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Array Configuration", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"+ Generate", None))
        self.Btnrandomize.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"code", None))
    # retranslateUi

