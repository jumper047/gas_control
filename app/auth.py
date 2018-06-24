# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic

import app.lib.authentication as myauth

Ui_Form_auth, QWidget_auth = uic.loadUiType('app/ui/auth.ui')


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
