from PyQt4 import QtCore, QtGui, uic

import app.lib.archive as archive
import app.lib.authentication as myauth
import app.lib.sensors as sensors

from app.auth import Auth
from app.admin import Admin
from app.sensorinfo import SensorInfo

Ui_MainWindow_main, QMainWindow_main = uic.loadUiType('app/ui/main.ui')


class MyApp(QMainWindow_main, Ui_MainWindow_main):

    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
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
        self.tableWidget.cellDoubleClicked.connect(self.showSensorInfo)

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

        data = sensors.getData()
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

    def showSensorInfo(self):

        row = int(self.tableWidget.selectedIndexes()[0].row())
        id = int(self.tableWidget.item(row, 0).text())
        self.detail = SensorInfo(id)
