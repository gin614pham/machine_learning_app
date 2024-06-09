# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 747)
        MainWindow.setMinimumSize(QSize(1125, 747))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1125, 747))
        self.centralwidget.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnReadFile = QPushButton(self.frame_3)
        self.btnReadFile.setObjectName(u"btnReadFile")

        self.verticalLayout.addWidget(self.btnReadFile)

        self.labelReadFile = QLabel(self.frame_3)
        self.labelReadFile.setObjectName(u"labelReadFile")

        self.verticalLayout.addWidget(self.labelReadFile, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnHome = QPushButton(self.frame_4)
        self.btnHome.setObjectName(u"btnHome")

        self.verticalLayout_2.addWidget(self.btnHome)

        self.btnClear = QPushButton(self.frame_4)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout_2.addWidget(self.btnClear)

        self.btnChart = QPushButton(self.frame_4)
        self.btnChart.setObjectName(u"btnChart")

        self.verticalLayout_2.addWidget(self.btnChart)

        self.btnTrain = QPushButton(self.frame_4)
        self.btnTrain.setObjectName(u"btnTrain")

        self.verticalLayout_2.addWidget(self.btnTrain)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 382, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btnSaveCSV = QPushButton(self.frame)
        self.btnSaveCSV.setObjectName(u"btnSaveCSV")

        self.verticalLayout_3.addWidget(self.btnSaveCSV)

        self.btnQuit = QPushButton(self.frame)
        self.btnQuit.setObjectName(u"btnQuit")

        self.verticalLayout_3.addWidget(self.btnQuit)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.home_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tableData = QTableWidget(self.frame_5)
        self.tableData.setObjectName(u"tableData")

        self.verticalLayout_5.addWidget(self.tableData)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.home_page)
        self.clear_page = QWidget()
        self.clear_page.setObjectName(u"clear_page")
        self.horizontalLayout_2 = QHBoxLayout(self.clear_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.clear_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textInfo = QTextBrowser(self.frame_6)
        self.textInfo.setObjectName(u"textInfo")

        self.verticalLayout_6.addWidget(self.textInfo)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.clear_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.btnInfo = QPushButton(self.frame_7)
        self.btnInfo.setObjectName(u"btnInfo")

        self.verticalLayout_7.addWidget(self.btnInfo)

        self.btnNaN = QPushButton(self.frame_7)
        self.btnNaN.setObjectName(u"btnNaN")

        self.verticalLayout_7.addWidget(self.btnNaN)

        self.btnDuplicate = QPushButton(self.frame_7)
        self.btnDuplicate.setObjectName(u"btnDuplicate")

        self.verticalLayout_7.addWidget(self.btnDuplicate)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.tabWidget = QTabWidget(self.frame_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabNaN = QWidget()
        self.tabNaN.setObjectName(u"tabNaN")
        self.verticalLayout_9 = QVBoxLayout(self.tabNaN)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.tabNaN)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBoxEditIn = QComboBox(self.frame_8)
        self.comboBoxEditIn.addItem("")
        self.comboBoxEditIn.addItem("")
        self.comboBoxEditIn.setObjectName(u"comboBoxEditIn")

        self.horizontalLayout_4.addWidget(self.comboBoxEditIn)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.tabNaN)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.comboBoxSelectColumn = QComboBox(self.frame_10)
        self.comboBoxSelectColumn.setObjectName(u"comboBoxSelectColumn")

        self.horizontalLayout_5.addWidget(self.comboBoxSelectColumn)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.tabNaN)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)

        self.radioButtonDelete = QRadioButton(self.frame_9)
        self.btnGTypeNullEdit = QButtonGroup(MainWindow)
        self.btnGTypeNullEdit.setObjectName(u"btnGTypeNullEdit")
        self.btnGTypeNullEdit.addButton(self.radioButtonDelete)
        self.radioButtonDelete.setObjectName(u"radioButtonDelete")

        self.verticalLayout_8.addWidget(self.radioButtonDelete)

        self.radioButtonReplace = QRadioButton(self.frame_9)
        self.btnGTypeNullEdit.addButton(self.radioButtonReplace)
        self.radioButtonReplace.setObjectName(u"radioButtonReplace")

        self.verticalLayout_8.addWidget(self.radioButtonReplace)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.tabNaN)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.comboBoxReplace = QComboBox(self.frame_11)
        self.comboBoxReplace.addItem("")
        self.comboBoxReplace.addItem("")
        self.comboBoxReplace.addItem("")
        self.comboBoxReplace.setObjectName(u"comboBoxReplace")

        self.horizontalLayout_6.addWidget(self.comboBoxReplace)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.btnRunEditNull = QPushButton(self.tabNaN)
        self.btnRunEditNull.setObjectName(u"btnRunEditNull")

        self.verticalLayout_9.addWidget(self.btnRunEditNull)

        self.tabWidget.addTab(self.tabNaN, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btnDeleteDuplicate = QPushButton(self.tab_2)
        self.btnDeleteDuplicate.setObjectName(u"btnDeleteDuplicate")

        self.verticalLayout_10.addWidget(self.btnDeleteDuplicate)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(11, 11, 11, -1)
        self.btnToNumeric = QPushButton(self.tab)
        self.btnToNumeric.setObjectName(u"btnToNumeric")

        self.verticalLayout_11.addWidget(self.btnToNumeric)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 256, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.btnSave = QPushButton(self.frame_7)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout_7.addWidget(self.btnSave)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)
        self.stackedWidget.addWidget(self.clear_page)
        self.chart_page = QWidget()
        self.chart_page.setObjectName(u"chart_page")
        self.stackedWidget.addWidget(self.chart_page)
        self.train_page = QWidget()
        self.train_page.setObjectName(u"train_page")
        self.horizontalLayout_7 = QHBoxLayout(self.train_page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_12 = QFrame(self.train_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widgetMatplotlib = QWidget(self.frame_12)
        self.widgetMatplotlib.setObjectName(u"widgetMatplotlib")

        self.verticalLayout_13.addWidget(self.widgetMatplotlib)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.train_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.comboBoxTargetColumn = QComboBox(self.frame_14)
        self.comboBoxTargetColumn.setObjectName(u"comboBoxTargetColumn")

        self.horizontalLayout_8.addWidget(self.comboBoxTargetColumn)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.listWidgetColumns = QListWidget(self.frame_16)
        self.listWidgetColumns.setObjectName(u"listWidgetColumns")

        self.gridLayout.addWidget(self.listWidgetColumns, 1, 0, 1, 1)

        self.listWidgetColumnSelected = QListWidget(self.frame_16)
        self.listWidgetColumnSelected.setObjectName(u"listWidgetColumnSelected")

        self.gridLayout.addWidget(self.listWidgetColumnSelected, 1, 1, 1, 1)

        self.btnAddColumn = QPushButton(self.frame_16)
        self.btnAddColumn.setObjectName(u"btnAddColumn")

        self.gridLayout.addWidget(self.btnAddColumn, 2, 0, 1, 1)

        self.btnDelColumn = QPushButton(self.frame_16)
        self.btnDelColumn.setObjectName(u"btnDelColumn")

        self.gridLayout.addWidget(self.btnDelColumn, 2, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.line_2 = QFrame(self.frame_13)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.comboBoxTypeModel = QComboBox(self.frame_15)
        self.comboBoxTypeModel.addItem("")
        self.comboBoxTypeModel.addItem("")
        self.comboBoxTypeModel.addItem("")
        self.comboBoxTypeModel.addItem("")
        self.comboBoxTypeModel.setObjectName(u"comboBoxTypeModel")

        self.horizontalLayout_9.addWidget(self.comboBoxTypeModel)


        self.verticalLayout_12.addWidget(self.frame_15)

        self.verticalSpacer_3 = QSpacerItem(20, 233, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.btnTrainModel = QPushButton(self.frame_13)
        self.btnTrainModel.setObjectName(u"btnTrainModel")

        self.verticalLayout_12.addWidget(self.btnTrainModel)


        self.horizontalLayout_7.addWidget(self.frame_13)

        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 2)
        self.stackedWidget.addWidget(self.train_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.radioButtonReplace.clicked.connect(self.frame_11.show)
        self.radioButtonDelete.clicked.connect(self.frame_11.hide)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnReadFile.setText(QCoreApplication.translate("MainWindow", u"Read File", None))
        self.labelReadFile.setText(QCoreApplication.translate("MainWindow", u"No File", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear Data", None))
        self.btnChart.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.btnTrain.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.btnSaveCSV.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.textInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">No Data</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Info", None))
        self.btnInfo.setText(QCoreApplication.translate("MainWindow", u"Check Info", None))
        self.btnNaN.setText(QCoreApplication.translate("MainWindow", u"Check Null", None))
        self.btnDuplicate.setText(QCoreApplication.translate("MainWindow", u"Check Duplicate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Edit In", None))
        self.comboBoxEditIn.setItemText(0, QCoreApplication.translate("MainWindow", u"Column", None))
        self.comboBoxEditIn.setItemText(1, QCoreApplication.translate("MainWindow", u"Row", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Column", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Type Edit", None))
        self.radioButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.radioButtonReplace.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Replace With", None))
        self.comboBoxReplace.setItemText(0, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.comboBoxReplace.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.comboBoxReplace.setItemText(2, QCoreApplication.translate("MainWindow", u"Mode", None))

        self.btnRunEditNull.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNaN), QCoreApplication.translate("MainWindow", u"Edit Null Value", None))
        self.btnDeleteDuplicate.setText(QCoreApplication.translate("MainWindow", u"Delete All Duplicate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Edit Duplicate", None))
        self.btnToNumeric.setText(QCoreApplication.translate("MainWindow", u"Convert all to numeric", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Convert to numeric", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Target column", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Columns:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select:", None))
        self.btnAddColumn.setText(QCoreApplication.translate("MainWindow", u"Add >>", None))
        self.btnDelColumn.setText(QCoreApplication.translate("MainWindow", u"<< Delete", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.comboBoxTypeModel.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear Regression", None))
        self.comboBoxTypeModel.setItemText(1, QCoreApplication.translate("MainWindow", u"Logistic Regression", None))
        self.comboBoxTypeModel.setItemText(2, QCoreApplication.translate("MainWindow", u"KNN", None))
        self.comboBoxTypeModel.setItemText(3, QCoreApplication.translate("MainWindow", u"Decision Tree", None))

        self.btnTrainModel.setText(QCoreApplication.translate("MainWindow", u"Train", None))
    # retranslateUi

