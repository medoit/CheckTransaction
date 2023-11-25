from datetime import datetime
from pydantic import BaseModel

class Transaction(BaseModel):
    terminal : int
    type : int
    date : datetime
    time : datetime
    series : int
    num_ticket : int
    price : int
    pan : str
    
    def __str__(self):
        return f'{self.terminal}, {self.type}, {self.get_str_date()}, {self.get_str_time()}, {self.series}, {self.num_ticket}, {self.price}, {self.pan}'
    
    def get_str_date(self):
        return self.date.strftime('%d.%m.%y')
    
    def get_str_time(self):
        return self.time.strftime('%H:%M:%S')
    
def get_diff_date(date_d, date_t, date_s):
    result = (datetime.strptime(date_d + ' ' + date_t, '%d.%m.%y %H:%M:%S') - date_s).days
    return result