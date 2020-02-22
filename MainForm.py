# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets  # 导入PyQt5部件
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTreeWidgetItem, QTreeWidget
from PyQt5 import QtCore

from MainWindow import Ui_MainWindow
import json

with open('cmdlist.json', 'r') as f:
    cmdList = json.load(f)


class NfcMainForm(QMainWindow, Ui_MainWindow):
    # 用于处理树控件中 item 索引定位
    currPoint = 0

    # 树控件当前配置参数
    paramsDict = {"name": ' ', 'header': [], "params": []}

    def __init__(self):
        super(NfcMainForm, self).__init__()
        self.setupUi(self)

        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.UI_MenuContextTree)

        self.pushButton_8.clicked.connect(self.UI_PushButton8Clicked)
        self.comboBox_CmdList.currentIndexChanged.connect(self.UI_SelectionChange)

        self.UI_InitCmdList()

        self.textEdit_4.setReadOnly(True)
        self.textEdit.setReadOnly(True)

        self.setGeometry(0, 0, 1024, 600)
        self.setWindowTitle('NFC TOOL')

    def UI_PushButton8Clicked(self):
        text = self.comboBox_CmdList.currentText()
        self.UpdateParamsConfig()

        NfcUtils.NciCmdEncode(self.paramsDict)
        self.textEdit_4.setText(NfcUtils.nciCmdStr)

    def UI_MenuContextTree(self, point):
        index = self.treeWidget.indexAt(point)
        self.currPoint = point
        if not index.isValid():
            return
        item = self.treeWidget.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        addAction = QAction("Add a " + name)
        delAction = QAction("Del a " + name)
        addAction.triggered.connect(self.UI_AddItem)
        delAction.triggered.connect(self.UI_DelItem)

        menu.addAction(addAction)
        menu.addAction(delAction)
        menu.exec_(self.treeWidget.mapToGlobal(point))

    def UI_AddItem(self):
        # add this item
        item = self.treeWidget.itemAt(self.currPoint)
        itemParent = QTreeWidgetItem.parent(item)
        node = QTreeWidgetItem.clone(item)
        itemParent.addChild(node)

    def UI_DelItem(self):
        # del this item
        item = self.treeWidget.itemAt(self.currPoint)
        itemParent = QTreeWidgetItem.parent(item)
        itemParent.removeChild(item)

    def UI_SelectionChange(self, i):
        self.UI_UpdateParaTree(i)

    def UI_UpdateParaTree(self, i):
        self.treeWidget.clear()
        text = self.comboBox_CmdList.currentText()
        params = cmdList["NciCmdList"][text]['params']
        headerList = list(params[0].keys())

        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(headerList[0:3])
        for i in range(len(headerList[0:3])):
            self.treeWidget.setColumnWidth(i, 250)

        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, text)

        nodeList = []
        for param in params:
            node = QTreeWidgetItem(root)
            node.setText(0, param['type'])
            node.setText(1, str(param['length']))
            if isinstance(param['value'], list):
                for i in range(0, param['length']):
                    self.UI_ProcessParams(param['value'], node)
            else:
                node.setText(2, str(param['value']))
            node.setToolTip(0, param['tips'])
            node.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable)
            if str(param['checked']) == 'True':
                node.setCheckState(0, QtCore.Qt.Checked)
            elif str(param['checked']) == 'False':
                node.setCheckState(0, QtCore.Qt.Unchecked)
            nodeList.append(node)

        self.treeWidget.insertTopLevelItems(0, nodeList)
        self.treeWidget.expandAll()

    def UI_ProcessParams(self, params, root):
        for param in params:
            node = QTreeWidgetItem(root)
            node.setText(0, param['type'])
            node.setText(1, str(param['length']))
            lst = param['value']
            if isinstance(param['value'], list):
                for i in range(0, param['length']):
                    self.UI_ProcessParams(param['value'], node)
            else:
                node.setText(2, str(param['value']))

            node.setToolTip(0, param['tips'])
            node.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable)
            node.setCheckState(0, QtCore.Qt.Checked)

    def UI_InitCmdList(self):
        self.comboBox_CmdList.addItems(cmdList["NciCmdList"])

    def UpdateParamsConfig(self):
        cmd = self.comboBox_CmdList.currentText()
        self.paramsDict['name'] = cmd
        self.paramsDict['header'] = cmdList["NciCmdList"][cmd]['header']

        self.paramsDict['params'].clear()
        it = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        while it.value():
            item = it.value()
            if item.checkState(0) == QtCore.Qt.Checked:
                if item.childCount() == 0:
                    if item.text(1).isdigit() and item.text(2).isdigit():
                        self.paramsDict['params'].append(
                            {'type': item.text(0),
                             'length': int(item.text(1)),
                             'value': int(item.text(2))})
            it = it.__iadd__(1)


class NfcUtils:
    nciCmdStr = ''
    hciCmdStr = ''

    @staticmethod
    def Int2HexStr(cmd_bytes):
        lin = ['%02X' % i for i in cmd_bytes]
        NfcUtils.nciCmdStr = " ".join(lin)

    @staticmethod
    def NciCmdEncode(paramsDict):
        cmd_bytes = []
        MT = 0b001
        PBF = 0b0
        GID = int(paramsDict['header'][0]['value'])
        cmd_bytes.append((MT << 5) + (PBF << 4) + GID)

        OID = paramsDict['header'][1]['value']
        cmd_bytes.append(OID)

        len = 0
        cmd_bytes.append(len)
        for i in paramsDict['params']:
            cnt = int(i['length'])
            len += cnt
            cmd_bytes.append(i['value'])

        cmd_bytes[2] = len
        NfcUtils.Int2HexStr(cmd_bytes)

    @staticmethod
    def HciCmdEncode(paramsDict):
        #for i in range(len(paramsDict)):
           #t = paramsDict[i]['type']
        NfcUtils.hciCmdStr = '002041125a'
