from datetime import datetime
from pydantic import BaseModel

class Terminal(BaseModel):
    number : int
    serial_number : int
    discription : str
    last_date_update : datetime
    status_update : str
    revision : str       
    
    def __str__(self):
        return f'{self.number}, {self.serial_number}, {self.discription}, {self.last_date_update}, {self.status_update}, {self.revision}'
    