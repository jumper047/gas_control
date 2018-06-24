# This module will do some things about sensors - get data from sensors
# and write it to database

import datetime
import random


class SensorsStatement(object):

    def __init__(self):
        pass        # self.data = {}

    def getData(self):

        data = {}
        k = 0
        with open("app/lib/fake.txt", "r") as file:
            raw_data = file.readline()
            values = raw_data.split(',')
            # for i in range(0,len(values),2): # 9 strings
            #     values[i] = int(values[i])
            #     values[i+1] = int(values[i+1])
            #     time = [datetime.datetime.now().strftime("%H:%M")]
            #     value = [values[i], values[i+1]]
            #     data[k] = time + value
            #     k += 1
            for i in range(0, 9):
                concentration = random.randint(16, 25)
                health = random.randint(0, 1)
                time = [datetime.datetime.now().strftime("%H:%M")]
                value = [concentration, health]
                data[k] = time + value
                k += 1

            return data
