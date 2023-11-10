import datetime

class Sub():
    
    def __init__(self, id, series, since, till, sale_date, card_num):
        self.id : int = id
        self.series : int = series
        self.since : datetime = since
        self.till : datetime = till 
        self.sale_date : datetime = sale_date
        self.card_num : str = card_num
        self.status : bool = None
    
    def __str__(self):
        return f'{self.id}, {self.since}, {self.till}, {self.sale_date}, {self.card_num}, {self.status}'
    
    def set_status(self):
        if self.till < datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
            self.status = False
        else:
            self.status = True