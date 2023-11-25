import os
import datetime
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
            sub_all.append(Sub(el[0],el[1],format_date(el[2]),format_date(el[3]),format_date(el[4]),el[5].replace('"', '').strip()))
    return sub_all

def load_transactions(filepath):
    transactions : List[Transaction] = []
    with open(filepath) as f:
        first_line = f.readline().split()
        for line in f:
            el = line.split()
            if el[1] == '32':
                transactions.append(Transaction(first_line[8], el[1], el[2], el[3], el[5], el[13], el[15].replace('0', ''), el[16].strip()))
    return transactions

def load_terminal(filepath):
    list_terminal : List[Terminal] = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            el = line.split(';')
            list_terminal.append(Terminal(el[0],
                                        el[1],
                                        el[2],
                                        format_date(el[3]),
                                        el[4],
                                        el[5]))
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