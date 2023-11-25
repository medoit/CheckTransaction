from typing import List

class Snls():

    def __init__(self, data):
        self.pan : str = set_pan(data)
        self.serias : str = set_serias(data)

    def __str__(self) -> str:
        return f'{self.pan}, {self.serias}'

def get_list_pan_snls(list_snls: List[Snls]):
    result : List[str] = []
    for el in list_snls:
        result.append(el.pan)
    return result

def set_pan(data):
    return data[:-3]

def set_serias(data):
    return data[-3:]