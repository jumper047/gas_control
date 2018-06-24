# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic

Ui_Dialog_adduser, QDialog_adduser = uic.loadUiType(
    'gui/QtDesigner/adduser.ui')


class AddUserDialog(QDialog_adduser, Ui_Dialog_adduser):

    def __init__(self):
        super(AddUserDialog, self).__init__()
        self.setupUi(self)
        self.show()
        self.buttonBox.accepted.connect(self.addNewUser)
        self.buttonBox.rejected.connect(self.reject)
        self.user = str()
        self.password1 = str()

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
