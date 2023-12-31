from datetime import datetime

def format_date(str):
    fromats = [
        '"%Y-%m-%d %H:%M:%S"',
        '"%Y-%m-%d %H:%M:%S.%f"',
        '%d.%m.%Y',
        '%d.%m.%y',
        '%H:%M:%S'
    ]
    for el in fromats:
        try:
            result = bool(datetime.strptime(str, el))
        except:
            result = False
        if result:
            return datetime.strptime(str, el)

def is_digit(str : str):
    if str.isdigit():
        return int(str)