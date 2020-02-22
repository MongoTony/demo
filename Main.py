# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets   # 导入PyQt5部件
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import sys

from MainForm import NfcMainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = NfcMainForm()
    main.show()
    sys.exit(app.exec_())