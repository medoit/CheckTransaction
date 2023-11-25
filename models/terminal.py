import datetime

class Terminal():

    def __init__(self, number,
                serial_number,
                discription, 
                last_date_update,
                status_update,
                revision):
        self.number : int = number
        self.serial_number : int = serial_number
        self.discription : str = discription
        self.last_date_update : datetime = last_date_update
        self.status_update : str = status_update
        self.revision : int = revision
    
    def __str__(self):
        return f'{self.number}, {self.serial_number}, {self.discription}, {self.last_date_update}, {self.status_update}, {self.revision}'
    