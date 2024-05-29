from typing import List
from models.snls import Snls, get_list_pan_snls
from models.sub import Sub, get_sub, get_actual_list_subs
from models.transaction import Transaction
from upload import *
from save import *
from validation import *

def get_transactions_sub(list_transactions : List[Transaction], list_pan : List[str]):
    transactions_sub : List[Transaction] = []
    for el in list_transactions:
        if el.pan in list_pan:
            transactions_sub.append(el)
    return transactions_sub

def get_transaction_bad(transactions_sub : List[Transaction], list_subs : List[Sub]):
    bad_list : List[Transaction] = []
    count = 0
    for el in transactions_sub:
        sub : Sub = get_sub(el.pan, list_subs)
        if el.series == 96 and (el.date - sub.sale_date).days > 1 and el.date <= sub.till:
            bad_list.append(el)
            count = count + 1
    return bad_list

def check_list_transaction(list_transactions : List[Transaction], list_terminal : List[Terminal], list_subs : List[Sub]):
    print("Номер терминала, тип транзакции, дата транзакции, время транзакции, серия, номер билета, стоимость билета, PAN карты |  Какая должна быть серия")
    for el in list_transactions:
        for t in list_terminal:
            if el.terminal == t.serial_number:
                sub = get_sub(el.pan, list_subs)
                print(el, "|", sub.series)

def count_series(list_transactions : List[Transaction]):
    count_old = 0
    count_young = 0
    count_free = 0
    count_pay = 0
    for el in list_transactions:
        if el.series == 31:
            count_old = count_old + 1
        elif el.series == 30:
            count_young = count_young + 1
        elif el.series == 50:
            count_free = count_free + 1
        elif el.series == 96:
            count_pay = count_pay + 1
    print("Транзакции")
    print("Все:", count(list_transactions))
    print("96:", count_pay)
    print("50:", count_free)
    print("31:", count_old)
    print("30:", count_young)

def count_sub_series(list_subs : List[Sub]):
    count_old = 0
    count_young = 0
    count_free = 0
    for el in list_subs:
        if el.series == 31:
            count_old = count_old + 1
        elif el.series == 30:
            count_young = count_young + 1
        elif el.series == 50:
            count_free = count_free + 1
    print("Абонементы")
    print("Все:", count(list_subs))
    print("50:", count_free)
    print("31:", count_old)
    print("30:", count_young)

def print_list_transaction(list_transactions : List[Transaction]):
    for el in list_transactions:
        print(el)

list_terminal = load_terminal("source\\terminals_221123.txt")
list_snls = load_snls("source\\SNLS220524.txt")
save_in_file("result\\snls.txt", list_snls)
list_subs = load_subs('source\\subs220524.txt')
save_in_file("result\\list_subs.txt", list_subs)
list_pan = get_list_pan_snls(list_snls)
list_transactions = load_multiple()
save_in_file("result\\transactions.txt", list_transactions)
list_transactions_sub = get_transactions_sub(list_transactions, list_pan)
list_transactions_bad = get_transaction_bad(list_transactions_sub, list_subs)
check_list_transaction(list_transactions_bad, list_terminal, list_subs)
save_in_file("result\\transactions_bad.txt", list_transactions_bad)
count_series(list_transactions)
count_sub_series(list_subs)