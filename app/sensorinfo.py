# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic


Ui_Form_sensorinfo, QWidget_sensorinfo = uic.loadUiType('app/ui/sensorinfo.ui')


class SensorInfo(QWidget_sensorinfo, Ui_Form_sensorinfo):

    def __init__(self, sensor_id):
        super(SensorInfo, self).__init__()
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
