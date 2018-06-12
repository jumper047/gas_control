# -*- coding: utf-8 -*-
import os
import sqlite3

from PyQt4 import QtCore, QtGui


class Authentication(object):

    def __init__(self):
        if os.path.isfile("data/users.db") is not True:
            with sqlite3.connect("data/users.db") as con:
                cur = con.cursor()
                cur.executescript("""
                CREATE TABLE IF NOT EXISTS Users\
                (Id INTEGER PRIMARY KEY, Name TEXT,Pass TEXT);
                INSERT INTO Users(Name, Pass) VALUES ('Администратор','admin');
                INSERT INTO Users(Name, Pass) VALUES ('А.Б. Иванов','1');
                INSERT INTO Users(Name, Pass) VALUES ('В.Г. Петров','1');
                """)
                con.commit()

    def usersList(self):
        """
        Get list of currently registered users
        usersList() -> [id1, id2, ..etc] 
        """
        with sqlite3.connect("data/users.db") as con:
            con.row_factory = lambda cursor, row: row[0]
            cur = con.cursor()
            cur.execute("SELECT Id FROM Users")
            uids = cur.fetchall()
        return uids

    def usersIdsList(self):
        """
        Get list of currently registered users with theri ids
        usersIdsList() -> [[1, "Admin"], [2, "J. Doe"], ... etc]
        """
        with sqlite3.connect("data/users.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Id, Name FROM Users")
            uids = cur.fetchall()
        return uids

    def getUserName(self, uid):
        """
        Get human-readable username
        getUserName(uid) -> "Name" 
        """
        with sqlite3.connect("data/users.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Name FROM Users WHERE Id=?", str(uid))
            name = cur.fetchall()[0][0]
        return name

    def userCheck(self, uid, inp_password):
        """
        Check user's password
        userCheck(uid, password) -> True/False
        """
        with sqlite3.connect("data/users.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Pass FROM Users WHERE Id=?", str(uid))
            password = cur.fetchall()[0][0]
        if inp_password == password[0]:
            return True
        else:
            return False

    def userAdd(self, user_name, password):
        """
        Add new user
        userAdd(user_name, password)
        """
        added_user = (str(user_name), str(password))
        with sqlite3.connect("data/users.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO Users(Name, Pass) VALUES(?, ?)", added_user)
            return True

    def userDel(self, user_id):
        """
        Delete selected user
        userDel(id)
        """
        with sqlite3.connect("data/users.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Users WHERE Id=?", str(user_id))
            return True
