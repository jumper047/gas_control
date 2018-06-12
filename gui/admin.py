# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(771, 582)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.manage = QtGui.QWidget()
        self.manage.setObjectName(_fromUtf8("manage"))
        self.verticalLayout = QtGui.QVBoxLayout(self.manage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.manage)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addUserButton = QtGui.QPushButton(self.manage)
        self.addUserButton.setObjectName(_fromUtf8("addUserButton"))
        self.horizontalLayout_2.addWidget(self.addUserButton)
        self.delUserButton = QtGui.QPushButton(self.manage)
        self.delUserButton.setObjectName(_fromUtf8("delUserButton"))
        self.horizontalLayout_2.addWidget(self.delUserButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget.raise_()
        self.tableWidget.raise_()
        self.tabWidget.addTab(self.manage, _fromUtf8(""))
        self.log = QtGui.QWidget()
        self.log.setObjectName(_fromUtf8("log"))
        self.tabWidget.addTab(self.log, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Администратор", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Имя пользователя", None))
        self.addUserButton.setText(_translate("Form", "Добавить", None))
        self.delUserButton.setText(_translate("Form", "Удалить", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manage), _translate("Form", "Управление", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("Form", "Действия пользователей", None))

