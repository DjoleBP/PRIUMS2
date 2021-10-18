from PyQt5.QtCore import QThread, pyqtSignal
from pymongo import *
from datetime import datetime
import time
import sys


class MyDBThread(QThread):
    def __init__(self):
        super().__init__()
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['database']
        self.collection = self.db.kolekcija
        self.cnt = 0
        self.doc = {'_id': None, 'CO2': None,
                    'time': None}

    def run(self):
        while(1):
            time.sleep(10)

    def update_data_base(self, data):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.cnt += 1
        self.doc['_id'] = self.cnt
        self.doc['CO2'] = data[0]
        self.doc['time'] = current_time

        try:
            self.collection.insert_one(self.doc)
        except:
            err = sys.exc_info()[0]
            print(err)

    def exit(self):
        self.terminate()
