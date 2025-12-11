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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(615, 349)
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
        self.verticalLayout_4.setSpacing(7)
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
        self.Btnstart.setMaximumSize(QSize(60, 40))
        font = QFont()
        font.setPointSize(10)
        self.Btnstart.setFont(font)

        self.horizontalLayout.addWidget(self.Btnstart, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, 5)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.speed_comboBox = QComboBox(self.widget)
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.setObjectName(u"speed_comboBox")
        self.speed_comboBox.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.speed_comboBox)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


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
        self.horizontalLayout_5 = QHBoxLayout(self.Selection_sort)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_4 = QGroupBox(self.Selection_sort)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_20.addWidget(self.label_5)

        self.size_array_lineEdit_SelectionSort = QLineEdit(self.groupBox_4)
        self.size_array_lineEdit_SelectionSort.setObjectName(u"size_array_lineEdit_SelectionSort")

        self.verticalLayout_20.addWidget(self.size_array_lineEdit_SelectionSort)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_20.addWidget(self.label_12)

        self.CArray_lineEdit_SelectionSort = QLineEdit(self.groupBox_4)
        self.CArray_lineEdit_SelectionSort.setObjectName(u"CArray_lineEdit_SelectionSort")

        self.verticalLayout_20.addWidget(self.CArray_lineEdit_SelectionSort)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BtnGenerate_SelectionSort = QPushButton(self.groupBox_4)
        self.BtnGenerate_SelectionSort.setObjectName(u"BtnGenerate_SelectionSort")

        self.horizontalLayout_6.addWidget(self.BtnGenerate_SelectionSort)

        self.BtnRandomize_SelectionSort = QPushButton(self.groupBox_4)
        self.BtnRandomize_SelectionSort.setObjectName(u"BtnRandomize_SelectionSort")

        self.horizontalLayout_6.addWidget(self.BtnRandomize_SelectionSort)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.code_graphicsView_SSort = QGraphicsView(self.groupBox_5)
        self.code_graphicsView_SSort.setObjectName(u"code_graphicsView_SSort")

        self.verticalLayout_22.addWidget(self.code_graphicsView_SSort)


        self.verticalLayout_23.addLayout(self.verticalLayout_22)


        self.verticalLayout_20.addWidget(self.groupBox_5)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)


        self.verticalLayout_19.addWidget(self.groupBox_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_19)

        self.stackedWidget.addWidget(self.Selection_sort)
        self.Linear_search = QWidget()
        self.Linear_search.setObjectName(u"Linear_search")
        self.horizontalLayout_7 = QHBoxLayout(self.Linear_search)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_6 = QGroupBox(self.Linear_search)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_25.addWidget(self.label_6)

        self.size_array_lineEdit_LSearch = QLineEdit(self.groupBox_6)
        self.size_array_lineEdit_LSearch.setObjectName(u"size_array_lineEdit_LSearch")

        self.verticalLayout_25.addWidget(self.size_array_lineEdit_LSearch)

        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_25.addWidget(self.label_13)

        self.CArray_lineEdit_LSearch = QLineEdit(self.groupBox_6)
        self.CArray_lineEdit_LSearch.setObjectName(u"CArray_lineEdit_LSearch")

        self.verticalLayout_25.addWidget(self.CArray_lineEdit_LSearch)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BtnGenerate_LSearch = QPushButton(self.groupBox_6)
        self.BtnGenerate_LSearch.setObjectName(u"BtnGenerate_LSearch")

        self.horizontalLayout_8.addWidget(self.BtnGenerate_LSearch)

        self.BtnRandomize_LSearch = QPushButton(self.groupBox_6)
        self.BtnRandomize_LSearch.setObjectName(u"BtnRandomize_LSearch")

        self.horizontalLayout_8.addWidget(self.BtnRandomize_LSearch)


        self.verticalLayout_25.addLayout(self.horizontalLayout_8)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_25.addWidget(self.label_14)

        self.target_lineEdit_LSearch = QLineEdit(self.groupBox_6)
        self.target_lineEdit_LSearch.setObjectName(u"target_lineEdit_LSearch")

        self.verticalLayout_25.addWidget(self.target_lineEdit_LSearch)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.code_graphicsView_LSearch = QGraphicsView(self.groupBox_7)
        self.code_graphicsView_LSearch.setObjectName(u"code_graphicsView_LSearch")

        self.verticalLayout_27.addWidget(self.code_graphicsView_LSearch)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)


        self.verticalLayout_25.addWidget(self.groupBox_7)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)


        self.verticalLayout_24.addWidget(self.groupBox_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_24)

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

        self.size_array_lineEdit_Bsearch = QLineEdit(self.groupBox_3)
        self.size_array_lineEdit_Bsearch.setObjectName(u"size_array_lineEdit_Bsearch")

        self.verticalLayout_17.addWidget(self.size_array_lineEdit_Bsearch)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_17.addWidget(self.label_7)

        self.lineEdit_Bsearch = QLineEdit(self.groupBox_3)
        self.lineEdit_Bsearch.setObjectName(u"lineEdit_Bsearch")

        self.verticalLayout_17.addWidget(self.lineEdit_Bsearch)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 8)
        self.BtnGenerate_Bsearch = QPushButton(self.groupBox_3)
        self.BtnGenerate_Bsearch.setObjectName(u"BtnGenerate_Bsearch")

        self.horizontalLayout_4.addWidget(self.BtnGenerate_Bsearch)

        self.Btnrandomize_Bsearch = QPushButton(self.groupBox_3)
        self.Btnrandomize_Bsearch.setObjectName(u"Btnrandomize_Bsearch")

        self.horizontalLayout_4.addWidget(self.Btnrandomize_Bsearch)


        self.verticalLayout_17.addLayout(self.horizontalLayout_4)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_17.addWidget(self.label_8)

        self.target_lineEdit = QLineEdit(self.groupBox_3)
        self.target_lineEdit.setObjectName(u"target_lineEdit")

        self.verticalLayout_17.addWidget(self.target_lineEdit)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_17.addWidget(self.label_9)

        self.code_graphicsView_Bsearch = QGraphicsView(self.groupBox_3)
        self.code_graphicsView_Bsearch.setObjectName(u"code_graphicsView_Bsearch")

        self.verticalLayout_17.addWidget(self.code_graphicsView_Bsearch)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.Binary_search)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_29 = QVBoxLayout(self.page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_8 = QGroupBox(self.page)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_30.addWidget(self.label_15)

        self.lineEdit = QLineEdit(self.groupBox_8)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_30.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.pushButton_3 = QPushButton(self.groupBox_8)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_8)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_8)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)


        self.verticalLayout_30.addLayout(self.gridLayout)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.graphicsView = QGraphicsView(self.groupBox_9)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_12.addWidget(self.graphicsView)


        self.verticalLayout_30.addWidget(self.groupBox_9)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)


        self.horizontalLayout_9.addWidget(self.groupBox_8)


        self.verticalLayout_29.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Data Structures", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Algorithms", None))
        self.sort_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Selection Sort", None))
        self.sort_comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Bubble Sort", None))

        self.search_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Linear Search", None))
        self.search_comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Binary Search", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Stack", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Queue", None))

        self.Btnstart.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Speed", None))
        self.speed_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"1x", None))
        self.speed_comboBox.setItemText(1, QCoreApplication.translate("Widget", u"1.25x", None))
        self.speed_comboBox.setItemText(2, QCoreApplication.translate("Widget", u"1.5x", None))
        self.speed_comboBox.setItemText(3, QCoreApplication.translate("Widget", u"2x", None))
        self.speed_comboBox.setItemText(4, QCoreApplication.translate("Widget", u"3x", None))
        self.speed_comboBox.setItemText(5, QCoreApplication.translate("Widget", u"0.25x", None))
        self.speed_comboBox.setItemText(6, QCoreApplication.translate("Widget", u"0.5x", None))
        self.speed_comboBox.setItemText(7, QCoreApplication.translate("Widget", u"0.75x", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Bubble Sort", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.BtnGenerate.setText(QCoreApplication.translate("Widget", u"+ Generate", None))
        self.Btnrandomize.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"code", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"Selection Sort", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.BtnGenerate_SelectionSort.setText(QCoreApplication.translate("Widget", u"+Generate", None))
        self.BtnRandomize_SelectionSort.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Widget", u"Code", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Widget", u"Linear Search", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.BtnGenerate_LSearch.setText(QCoreApplication.translate("Widget", u"+Generate", None))
        self.BtnRandomize_LSearch.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Target", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Widget", u"Code", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Binary Search", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Array Size", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Custom Array", None))
        self.BtnGenerate_Bsearch.setText(QCoreApplication.translate("Widget", u"+Generate", None))
        self.Btnrandomize_Bsearch.setText(QCoreApplication.translate("Widget", u"Randomize", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Target Value:", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"code", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Widget", u"Stack", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Input values", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Peek", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Push", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Pop", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Widget", u"Code", None))
    # retranslateUi

