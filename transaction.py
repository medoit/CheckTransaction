import datetime
from typing import List
from sub import Sub

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
        self.sub : bool = None

    def __str__(self):
        return f'{self.terminal}, {self.type}, {self.date}, {self.time}, {self.series}, {self.num_ticket}, {self.price}, {self.pan}, {self.sub}\n'
    
    def is_sub(self, subs : List[Sub]):
        for sub in subs:
            if self.pan == sub.card_num and sub.status == True and get_diff_date(self.date, self.time, sub.sale_date) > 3:
                self.sub = True
                break
            else:
                self.sub = False
    
def get_diff_date(date_d, date_t, date_s):
    result = (datetime.datetime.strptime(date_d + ' ' + date_t, '%d.%m.%y %H:%M:%S') - date_s).days
    return result