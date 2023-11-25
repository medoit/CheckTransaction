import datetime
from typing import List
from models.sub import Sub

class Transaction():

    def __init__(self, terminal, type, date, time, series, num_ticket, price, pan):
        self.terminal : int = terminal
        self.type : int = type
        self.date : datetime = date
        self.time : datetime = time
        self.series : int = series
        self.num_ticket : int = num_ticket
        self.price : int = price
        self.pan : str = pan

    def __str__(self):
        return f'{self.terminal}, {self.type}, {self.date}, {self.time}, {self.series}, {self.num_ticket}, {self.price}, {self.pan}'
    
def get_diff_date(date_d, date_t, date_s):
    result = (datetime.datetime.strptime(date_d + ' ' + date_t, '%d.%m.%y %H:%M:%S') - date_s).days
    return result