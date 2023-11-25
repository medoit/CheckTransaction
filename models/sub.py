import datetime
from typing import List
from validation import *

class Sub():
    
    def __init__(self, id, series, since, till, sale_date, pan):
        self.id : int = id
        self.series : int = series
        self.since : datetime = since
        self.till : datetime = till 
        self.sale_date : datetime = sale_date
        self.pan : str = pan
    
    def __str__(self):
        return f'{self.id}, {self.since}, {self.till}, {self.sale_date}, {self.pan}'

def get_sub(pan, list_subs: List[Sub]):
    for el in list_subs:
        if el.pan == pan:
            return el

def get_actual_list_subs(list_subs : List[Sub]):
    result : List[Sub] = []
    for sub in list_subs:
        if format_date(sub.till) > datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
            result.append(sub)
    return result

def get_list_pan_sub(list_subs : List[Sub]):
    result : List[str] = []
    for el in list_subs:
        result.append(el.pan)
    return result