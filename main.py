# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic

from app.myapp import MyApp

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MyApp()
    sys.exit(app.exec_())
