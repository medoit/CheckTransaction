from datetime import datetime
from typing import List
from validation import *
from pydantic import BaseModel

class Sub(BaseModel):
    id : int
    series : int
    since : datetime
    till : datetime
    sale_date : datetime
    pan : str
    
    def __str__(self):
        return f'{self.id}, {self.since}, {self.till}, {self.sale_date}, {self.pan}'
    
    def get_id(self):
        return self.id
    
    def get_series(self):
        return self.series
    
    def get_since(self):
        return self.since
    
    def get_sale_date(self):
        return self.sale_date
    
    def get_pan(self):
        return self.pan

def get_sub(pan, list_subs: List[Sub]):
    for el in list_subs:
        if el.pan == pan:
            return el

def get_actual_list_subs(list_subs : List[Sub]):
    result : List[Sub] = []
    for sub in list_subs:
        if sub.till > datetime.now():
            result.append(sub)
    return result

def get_list_pan_sub(list_subs : List[Sub]):
    result : List[str] = []
    for el in list_subs:
        result.append(el.pan)
    return result