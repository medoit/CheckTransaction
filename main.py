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
        if el.series == 96 and (el.date - sub.sale_date).days > 1:
            bad_list.append(el)
            count = count + 1
    return bad_list

def check_list_transaction(list_transactions : List[Transaction], list_subs : List[Sub]):
    for el in list_transactions:
        sub = get_sub(el.pan, list_subs)
        print(format_date(el.date) - format_date(sub.sale_date))

def print_list_transaction(list_transactions : List[Transaction]):
    for el in list_transactions:
        print(el)

list_terminal = load_terminal("source\\terminals_221123.txt")
list_snls = load_snls("source\\snls_221123.txt")
save_in_file("result\\snls.txt", list_snls)
list_subs = get_actual_list_subs(load_subs('source\\subs_221123.txt'))
save_in_file("result\\list_subs.txt", list_subs)
list_pan = get_list_pan_snls(list_snls)
list_transactions = load_multiple()
save_in_file("result\\transactions.txt", list_snls)
list_transactions_sub = get_transactions_sub(list_transactions, list_pan)
list_transactions_bad = get_transaction_bad(list_transactions_sub, list_subs)
print_list_transaction(list_transactions_bad)
save_in_file("result\\transactions_bad.txt", list_transactions_bad)