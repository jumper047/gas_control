# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
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
        Form.resize(543, 139)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.userSelection = QtGui.QComboBox(Form)
        self.userSelection.setObjectName(_fromUtf8("userSelection"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.userSelection)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passwordEdit = QtGui.QLineEdit(Form)
        self.passwordEdit.setAcceptDrops(False)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordEdit)
        self.wrongPassword = QtGui.QLabel(Form)
        self.wrongPassword.setEnabled(True)
        self.wrongPassword.setText(_fromUtf8(""))
        self.wrongPassword.setObjectName(_fromUtf8("wrongPassword"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.wrongPassword)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(Form)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(Form)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.userSelection, self.passwordEdit)
        Form.setTabOrder(self.passwordEdit, self.okButton)
        Form.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Авторизация", None))
        self.label.setText(_translate("Form", "Пользователь:", None))
        self.label_2.setText(_translate("Form", "Пароль:", None))
        self.okButton.setText(_translate("Form", "Ок", None))
        self.cancelButton.setText(_translate("Form", "Отмена", None))

