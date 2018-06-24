# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic

import app.lib.authentication as auth

Ui_Form_admin, QWidget_admin = uic.loadUiType('app/ui/admin.ui')


class Admin(QWidget_admin, Ui_Form_admin):

    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setResizeMode(
            1, QtGui.QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)

        self.refreshUsers()

        self.addUserButton.clicked.connect(self.addUser)
        self.delUserButton.clicked.connect(self.delUser)

    def addUser(self):

        user_name, password, ok = AddUserDialog.inputUserData()
        auth.userAdd(user_name, password)
        self.refreshUsers()

    def delUser(self):

        row = int(self.tableWidget.selectedIndexes()[0].row())
        id = int(self.tableWidget.item(row, 0).text())
        auth.userDel(id)
        self.refreshUsers()

    def refreshUsers(self):

        row = 0
        self.tableWidget.setRowCount(len(auth.usersIdsList()))
        for element in auth.usersIdsList():
            col = 0
            for item in element:
                if not isinstance(item, basestring):
                    item = str(item)
                table_item = QtGui.QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, table_item)
                col += 1
            row += 1
