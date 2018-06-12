# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 155)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.userName = QtGui.QLineEdit(Dialog)
        self.userName.setObjectName(_fromUtf8("userName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.userName)
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.password)
        self.passwordControl = QtGui.QLineEdit(Dialog)
        self.passwordControl.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordControl.setObjectName(_fromUtf8("passwordControl"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.passwordControl)
        self.passwordIncorrect = QtGui.QLabel(Dialog)
        self.passwordIncorrect.setText(_fromUtf8(""))
        self.passwordIncorrect.setObjectName(_fromUtf8("passwordIncorrect"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.passwordIncorrect)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Добавление пользователя", None))
        self.label.setText(_translate("Dialog", "Имя пользователя:", None))
        self.label_2.setText(_translate("Dialog", "Пароль:", None))
        self.label_3.setText(_translate("Dialog", "Пароль повторно:", None))

