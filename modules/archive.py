import datetime
import os
import sqlite3
import time


# select * from "1" where Time < date ('2016-09-15 00:00:00') and Time >
# date ('2016-09-10 00:00:00')


def firstRun():
    "Create database, if not.."

    if os.path.isfile("../data/archive.db") is not True:
        with sqlite3.connect("data/archive.db") as con:
            cur = con.cursor()
            cur.executescript("""
            CREATE TABLE IF NOT EXISTS Sensors\
            (Id INTEGER PRIMARY KEY, Name TEXT,Info TEXT);
            CREATE TABLE IF NOT EXISTS 1(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 2(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 3(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 4(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 5(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 6(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 7(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 8(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
            CREATE TABLE IF NOT EXISTS 9(Time DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY, Concentration REAL, State INTEGER);
                """)
            con.commit()


def writeCurrentData(data):
    "Write fresh data to database"

    with sqlite3.connect("data/archive.db") as con:
        cur = con.cursor()
        for i in data.keys():
            id = i
            concentration = data[i][1]
            state = data[i][2]
            cur.execute(
                "INSERT INTO \"" + str(i + 1) + "\"(Concentration, State) VALUES(?, ?)", (str(concentration), str(state)))
    return True


def getArchivedConcentration(id, start, stop):
    """Get concentration from archive
    getArchivedConcentration(id, "2016-01-01 00:00:00", "2016-02-02 11:11:11")
    -> [[0000000000000,00000000001,...], [21.1,22.3,24.4]]"""

    with sqlite3.connect("data/archive.db") as con:
        cur = con.cursor()
        request = "SELECT Time, Concentration FROM \"" + \
            str(id) + "\" WHERE Time > ? AND Time < ?"
        cur.execute(request, (str(start), str(stop)))
        raw_data = cur.fetchall()
        timestmp = []
        concentration = []
        print "len:", len(raw_data)
        for i in range(0, len(raw_data)):
            print "concentration:", raw_data[i][1]
            print "time:", raw_data[i][0]
            print "i:", i
            concentration.append(raw_data[i][1])
            dt = datetime.datetime.strptime(
                str(raw_data[i][0]), "%Y-%m-%d %H:%M:%S")
            timestmp.append(time.mktime(dt.timetuple()))
    return [timestmp, concentration]


def getArchivedState(id, start, stop):
    """Get sensor's states from archive
    getArchivedState(id, "2016-01-01 00:00:00", "2016-02-02 11:11:11")
    -> [[0000000000000,00000000001,...], [21.1,22.3,24.4]]"""

    with sqlite3.connect("data/archive.db") as con:
        cur = con.cursor()
        request = "SELECT Time, State FROM \"" + \
            str(id) + "\" WHERE Time > ? AND Time < ?"
        cur.execute(request, (str(start), str(stop)))
        raw_data = cur.fetchall()
        timestmp = []
        state = []
        for i in range(0, len(raw_data)):
            state[i] = raw_data[i][1]
            dt = datetime.datetime.strptime(
                str(raw_data[i][0]), "%Y-%m-%d %H:%M:%S")
            timestmp[i] = time.mktime(dt.timetuple())
    return [timestmp, state]
