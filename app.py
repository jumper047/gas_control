# -*- coding: utf-8 -*-
import sys

import pyqtgraph as pg
from PyQt4 import QtCore, QtGui, uic

import modules.archive as archive
import modules.authentication as myauth
import modules.sensors as sensors
from modules.DateAxisItem import *

Ui_MainWindow_main, QMainWindow_main = uic.loadUiType('gui/QtDesigner/main.ui')
Ui_Form_details, QWidget_details = uic.loadUiType('gui/QtDesigner/details.ui')
Ui_Form_auth, QWidget_auth = uic.loadUiType('gui/QtDesigner/auth.ui')
Ui_Form_admin, QWidget_admin = uic.loadUiType('gui/QtDesigner/admin.ui')
Ui_Dialog_adduser, QDialog_adduser = uic.loadUiType(
    'gui/QtDesigner/adduser.ui')


class MyApp(QMainWindow_main, Ui_MainWindow_main):

    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)  # adds to widget all this amazing things:)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 199)
        self.tableWidget.setColumnWidth(3, 180)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setResizeMode(
            1, QtGui.QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.cellDoubleClicked.connect(self.showSensorDetails)

        self.refreshData()

        self.auth = Auth()
        self.auth.show()

        self.refreshTimer = QtCore.QTimer()
        self.refreshTimer.timeout.connect(self.refreshData)
        self.refreshTimer.start(5000)

        self.auth.authSuccessfull.connect(self.authenticationFinished)
        self.auth.authAdminSuccessfull.connect(
            self.authenticationAdminFinished)

    def authenticationAdminFinished(self):

        self.admin = Admin()
        self.admin.show()

    def authenticationFinished(self):

        self.show()
        self.auth.close()
        self.currentUser = self.auth.authenticatedUser
        self.userNameLabel.setText(self.currentUser)

    def refreshData(self):

        sens = sensors.SensorsStatement()
        data = sens.getData()
        archive.writeCurrentData(data)
        self.tableWidget.setRowCount(len(data))
        for row in range(len(data)):
            item = row + 1
            cell = QtGui.QTableWidgetItem(str(item))
            self.tableWidget.setItem(row, 0, cell)
            item = data[row][0]
            cell = QtGui.QTableWidgetItem(str(item))
            self.tableWidget.setItem(row, 1, cell)

            item = data[row][1]
            cell = QtGui.QTableWidgetItem(str(item))
            if item > 23:
                cell.setBackground(QtGui.QColor("Red"))
            elif item < 18:
                cell.setBackground(QtGui.QColor("Yellow"))
            self.tableWidget.setItem(row, 2, cell)
            item = data[row][2]
            if item != 1:
                item = "ERR"
                cell = QtGui.QTableWidgetItem(item)
                cell.setBackground(QtGui.QColor("Red"))
            else:
                item = "OK"
                cell = QtGui.QTableWidgetItem(item)
            self.tableWidget.setItem(row, 3, cell)

    def showSensorDetails(self):

        row = int(self.tableWidget.selectedIndexes()[0].row())
        id = int(self.tableWidget.item(row, 0).text())
        self.detail = Details(id)


class Details(QWidget_details, Ui_Form_details):

    def __init__(self, sensor_id):
        super(Details, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(u"Датчик №" + str(sensor_id))
        self.sensor_id = sensor_id

        self.conEndDateTime.setDate(QtCore.QDate.currentDate())
        self.conEndDateTime.setTime(QtCore.QTime.currentTime())
        self.conGraph = pg.PlotWidget(labels={"left": (u"Концентрация", "%")}, axisItems={
            'bottom': DateAxisItem(orientation='bottom')})
        self.verticalLayout_2.addWidget(self.conGraph)
        self.concShowButton.clicked.connect(self.getConcentrationGraph)

        self.stateEndDateTime.setDate(QtCore.QDate.currentDate())
        self.stateEndDateTime.setTime(QtCore.QTime.currentTime())
        self.stateGraph = pg.PlotWidget(labels={"left": (u"Состояние")}, axisItems={'bottom': DateAxisItem(
            orientation='bottom')})
        self.verticalLayout_3.addWidget(self.stateGraph)
        self.stateShowButton.clicked.connect(self.getStateGraph)

        self.show()

    def getConcentrationGraph(self):

        start = self.conStartDateTime.dateTime().toString(
            "yyyy-MM-dd HH:mm:ss")
        end = self.conEndDateTime.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        print "start:", start
        print "end:", end
        data = archive.getArchivedConcentration(self.sensor_id, start, end)
        print "data:", data[0][0], data[0][1]
        self.conGraph.plot(data[0], data[1])

    def getStateGraph(self):

        start = self.stateStartDateTime.dateTime().toString(
            "yyyy-MM-dd HH:mm:ss")
        end = self.stateEndDateTime.dateTime(
        ).toString("yyyy-MM-dd HH:mm:ss")
        data = archive.getArchivedState(self.sensor_id, start, end)
        self.stateGraph.plot(data[0], data[1])

    def printDateTime(self):

        print self.dateTimeEdit.dateTime()
        print str(self.dateTimeEdit.dateTime())
        print self.dateTimeEdit.dateTime().toString("HH:MM")
        print "date: %s" % self.dateTimeEdit.dateTime().date().toString()
        print "time: %s" % self.dateTimeEdit.dateTime().time().toString()


class Auth(QWidget_auth, Ui_Form_auth):

    authSuccessfull = QtCore.pyqtSignal()
    authAdminSuccessfull = QtCore.pyqtSignal()

    def __init__(self):
        super(Auth, self).__init__()
        self.setupUi(self)
        self.credentials = myauth.Authentication()
        for user in self.credentials.usersList():
            name = self.credentials.getUserName(user)
            self.userSelection.addItem(name, user)

        self.wrongPassword.setText("")
        self.authenticatedUser = ""

        self.okButton.clicked.connect(self.login)
        self.passwordEdit.editingFinished.connect(self.login)

    def login(self):
        inp_user_index = self.userSelection.currentIndex()
        inp_user = str(self.userSelection.itemData(inp_user_index).toString())
        inp_password = self.passwordEdit.text()
        if self.credentials.userCheck(inp_user, inp_password) is True:
            self.authenticatedUser = self.credentials.getUserName(inp_user)
            if inp_user == "admin":
                self.authAdminSuccessfull.emit()
            else:
                self.authSuccessfull.emit()
        else:
            self.wrongPassword.setText(u"Пароль не совпадает!")
            self.passwordEdit.setText("")


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

        self.users = myauth.Authentication()

        self.refreshUsers()

        self.addUserButton.clicked.connect(self.addUser)
        self.delUserButton.clicked.connect(self.delUser)

    def addUser(self):

        user_name, password, ok = AddUserDialog.inputUserData()
        self.users.userAdd(user_name, password)
        self.refreshUsers()

    def delUser(self):

        row = int(self.tableWidget.selectedIndexes()[0].row())
        id = int(self.tableWidget.item(row, 0).text())
        self.users.userDel(id)
        self.refreshUsers()

    def refreshUsers(self):

        row = 0
        self.tableWidget.setRowCount(len(self.users.usersIdsList()))
        for element in self.users.usersIdsList():
            col = 0
            for item in element:
                if not isinstance(item, basestring):
                    item = str(item)
                table_item = QtGui.QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, table_item)
                col += 1
            row += 1


class AddUserDialog(QDialog_adduser, Ui_Dialog_adduser):

    def __init__(self):
        super(AddUserDialog, self).__init__()
        self.setupUi(self)
        self.show()
        self.buttonBox.accepted.connect(self.addNewUser)
        self.buttonBox.rejected.connect(self.reject)
        self.user = ""
        self.password1 = ""

    def addNewUser(self):

        self.user = self.userName.text()
        self.password1 = self.password.text()
        password2 = self.passwordControl.text()

        if len(self.user) == 0:
            self.passwordIncorrect.setText(u"Введите имя!")
        elif self.password1 != password2:
            self.passwordIncorrect.setText(u"Пароли не совпадают!")
        elif len(self.password) == 0:
            self.passwordIncorrect.setText(u"Введите пароль!")
        else:
            self.accept()

    @staticmethod
    def inputUserData(parent=None):
        dialog = AddUserDialog()
        result = dialog.exec_()
        return (dialog.user, dialog.password1,
                dialog.result == QtGui.QDialog.Accepted)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MyApp()
    # temp = Details(2)
    sys.exit(app.exec_())
