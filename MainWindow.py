# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.nci_decoder = QtWidgets.QWidget()
        self.nci_decoder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nci_decoder.setObjectName("nci_decoder")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.nci_decoder)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.nci_decoder)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setMinimumSize(QtCore.QSize(180, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_6.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_6.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_6.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_6.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_6.addWidget(self.checkBox_7)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setSizeIncrement(QtCore.QSize(0, 5))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_7.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_2.addWidget(self.widget)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.nci_decoder)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.nci_decoder, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_9.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_9)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.treeWidget)
        self.widget_3 = QtWidgets.QWidget(self.groupBox_9)
        self.widget_3.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.verticalLayout_8.addWidget(self.groupBox_11)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_14.addWidget(self.groupBox_9)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_12.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_12.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_12)
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        self.widget_4 = QtWidgets.QWidget(self.groupBox_12)
        self.widget_4.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_14 = QtWidgets.QGroupBox(self.widget_4)
        self.groupBox_14.setObjectName("groupBox_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_13.addWidget(self.pushButton_13)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_13.addWidget(self.pushButton_12)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem4)
        self.verticalLayout_11.addWidget(self.groupBox_14)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.verticalLayout_14.addWidget(self.groupBox_12)
        self.gridLayout_2.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox_CmdList = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_CmdList.setObjectName("comboBox_CmdList")
        self.horizontalLayout_6.addWidget(self.comboBox_CmdList)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_12.clicked.connect(self.textEdit_4.clear)
        self.pushButton_9.clicked.connect(self.treeWidget.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "NCI Decoder Results"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Filters"))
        self.checkBox_3.setText(_translate("MainWindow", "COMMAND Message"))
        self.checkBox_4.setText(_translate("MainWindow", "RESPONSE Message"))
        self.checkBox_5.setText(_translate("MainWindow", "NOTIFICATION Message"))
        self.checkBox_6.setText(_translate("MainWindow", "DATA Message"))
        self.checkBox_7.setText(_translate("MainWindow", "ERROR Message"))
        self.pushButton_4.setText(_translate("MainWindow", "Apply filters"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Output"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear"))
        self.pushButton_7.setText(_translate("MainWindow", "Turn ON Logs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "NCI Message to be decoded []"))
        self.groupBox_5.setTitle(_translate("MainWindow", "String Format"))
        self.label.setText(_translate("MainWindow", "Byte Fomat"))
        self.label_2.setText(_translate("MainWindow", "Byte Separator"))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "Decode"))
        self.checkBox.setText(_translate("MainWindow", "On The Fly"))
        self.checkBox_2.setText(_translate("MainWindow", "Enable HCI Decoder"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Save Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nci_decoder), _translate("MainWindow", "NCI Decoder"))
        self.groupBox_8.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_9.setTitle(_translate("MainWindow", "NCI Message Param"))
        self.groupBox_11.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_8.setText(_translate("MainWindow", "Encode"))
        self.pushButton_9.setText(_translate("MainWindow", "Clear"))
        self.pushButton_10.setText(_translate("MainWindow", "Save Input"))
        self.groupBox_12.setTitle(_translate("MainWindow", "NCI Message String"))
        self.groupBox_14.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_13.setText(_translate("MainWindow", "Save Output"))
        self.pushButton_12.setText(_translate("MainWindow", "Clear"))
        self.groupBox_7.setTitle(_translate("MainWindow", "NCI Message"))
        self.label_3.setText(_translate("MainWindow", "Command : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "NCI Encoder"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
