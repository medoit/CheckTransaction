import os
from datetime import datetime
from typing import List
from models.snls import Snls
from models.sub import Sub
from models.transaction import Transaction
from models.terminal import Terminal
from validation import *

def load_snls(filepath):
    list_snls : List[Snls] = []
    with open(filepath) as f:
        for line in f:
            list_snls.append(Snls(line))
    return list_snls

def load_subs(filepath):
    sub_all : List[Sub] = []
    with open(filepath) as f:
        for line in f:
            el = line.split(';')
            sub_all.append(
                Sub(
                    id = int(el[0]),
                    series = el[1],
                    since = format_date(el[2]),
                    till = format_date(el[3]),
                    sale_date = format_date(el[4]),
                    pan = el[5].replace('"', '').strip()
                )
            )
    return sub_all

def load_transactions(filepath):
    transactions : List[Transaction] = []
    with open(filepath) as f:
        terminal = int(f.readline().split()[8])
        for line in f:
            el = line.split()
            if el[1] == '32':
                transactions.append(
                    Transaction(
                        terminal = terminal,
                        type = int(el[1]),
                        date = format_date(el[2]),
                        time = format_date(el[3]),
                        series = int(el[5]),
                        num_ticket = int(el[13]),
                        price = int(el[15]),
                        pan = el[16].strip()
                        )
                    )
    return transactions

def load_terminal(filepath):
    list_terminal : List[Terminal] = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            el = line.split(';')
            print
            list_terminal.append(
                Terminal(
                    number = int(el[0]),
                    serial_number = int(el[1]),
                    discription = el[2],
                    last_date_update = format_date(el[3]),
                    status_update = el[4],
                    revision = el[5]
                    )
                )
    return list_terminal

def count(subs):
    i = 0
    for el in subs:
        i = i + 1
    return i

def load_multiple():
    path = ".//transactions"
    months_list = os.listdir(path)
    transactions_all : List[Transaction] = []
    for month in months_list:
        days_list = os.listdir(path + "//" + month)
        for day in days_list:
            file_list = os.listdir(path + "//" + month + "//" + day)
            if count(days_list) > 0:
                for file in file_list:
                    transactions_el = load_transactions(path + "//" + month + "//" + day + "//" + file)
                    transactions_all = transactions_all + transactions_el
    return transactions_all