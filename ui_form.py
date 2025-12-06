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
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(613, 349)
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
        self.sort_comboBox = QComboBox(self.groupBox)
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.setObjectName(u"sort_comboBox")
        self.sort_comboBox.setEditable(False)

        self.verticalLayout_4.addWidget(self.sort_comboBox)

        self.search_comboBox = QComboBox(self.groupBox)
        self.search_comboBox.addItem("")
        self.search_comboBox.addItem("")
        self.search_comboBox.setObjectName(u"search_comboBox")

        self.verticalLayout_4.addWidget(self.search_comboBox)

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
        self.ref_graphicsView = QGraphicsView(self.widget)
        self.ref_graphicsView.setObjectName(u"ref_graphicsView")
        self.ref_graphicsView.setMaximumSize(QSize(900, 100))

        self.verticalLayout.addWidget(self.ref_graphicsView)

        self.visualizer_graphicsView = QGraphicsView(self.widget)
        self.visualizer_graphicsView.setObjectName(u"visualizer_graphicsView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.visualizer_graphicsView.sizePolicy().hasHeightForWidth())
        self.visualizer_graphicsView.setSizePolicy(sizePolicy)
        self.visualizer_graphicsView.setMaximumSize(QSize(900, 450))

        self.verticalLayout.addWidget(self.visualizer_graphicsView)


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

        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.Bubble_sort = QWidget()
        self.Bubble_sort.setObjectName(u"Bubble_sort")
        self.horizontalLayout_2 = QHBoxLayout(self.Bubble_sort)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.groupBox_2 = QGroupBox(self.Bubble_sort)
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

        self.custom_array_lineEdit = QLineEdit(self.groupBox_2)
        self.custom_array_lineEdit.setObjectName(u"custom_array_lineEdit")

        self.verticalLayout_9.addWidget(self.custom_array_lineEdit)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.BtnGenerate = QPushButton(self.groupBox_2)
        self.BtnGenerate.setObjectName(u"BtnGenerate")

        self.horizontalLayout_15.addWidget(self.BtnGenerate)

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

        self.code_graphicsView = QGraphicsView(self.frame_3)
        self.code_graphicsView.setObjectName(u"code_graphicsView")
        self.code_graphicsView.setMaximumSize(QSize(16777215, 600))

        self.verticalLayout_14.addWidget(self.code_graphicsView)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.Bubble_sort)
        self.Selection_sort = QWidget()
        self.Selection_sort.setObjectName(u"Selection_sort")
        self.label_5 = QLabel(self.Selection_sort)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 191, 16))
        self.stackedWidget.addWidget(self.Selection_sort)
        self.Linear_search = QWidget()
        self.Linear_search.setObjectName(u"Linear_search")
        self.label_6 = QLabel(self.Linear_search)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 161, 20))
        self.stackedWidget.addWidget(self.Linear_search)
        self.Binary_search = QWidget()
        self.Binary_search.setObjectName(u"Binary_search")
        self.verticalLayout_11 = QVBoxLayout(self.Binary_search)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_3 = QGroupBox(self.Binary_search)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_17.addWidget(self.lineEdit)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_17.addWidget(self.lineEdit_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 8)
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_4)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_17.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_17.addWidget(self.lineEdit_3)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_17.addWidget(self.label_9)

        self.graphicsView = QGraphicsView(self.groupBox_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_17.addWidget(self.graphicsView)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.Binary_search)

        self.horizontalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Data Structures", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Algorithms", None))
        self.sort_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Insertion Sort", None))
        self.sort_comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Bubble Sort", None))

        self.search_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Linear Search", None))
        self.search_comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Binary Search", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Linked List", None))

        self.Btnstart.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Array Configuration", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.BtnGenerate.setText(QCoreApplication.translate("Widget", u"+ Generate", None))
        self.Btnrandomize.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"code", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Insertion Sort", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Linear Search", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Binary Search", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"+Generate", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Target Value:", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"code", None))
    # retranslateUi

