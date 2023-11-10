import datetime
import os
from typing import List
from sub import Sub
from transaction import Transaction

def format_date(str):
    if '.' not in str:
        date_time_obj = datetime.datetime.strptime(str, '"%Y-%m-%d %H:%M:%S"')
    else:
        date_time_obj = datetime.datetime.strptime(str, '"%Y-%m-%d %H:%M:%S.%f"')
    return date_time_obj

def load_subs(filepath):
    sub_all : List[Sub] = []
    with open(filepath) as f:
        for line in f:
            el = line.split(';')
            sub_all.append(Sub(el[0],el[1],format_date(el[2]),format_date(el[3]),format_date(el[4]),el[5].replace('"', '').strip()))
    return sub_all       

def set_status_subs(subs : List[Sub]):
    for el in subs:
        el.set_status()

def get_sub_actual(subs : List[Sub]):
    sub_actual : List[Sub] = []
    for el in subs:
        if el.status == True:
            sub_actual.append(el)
    return sub_actual

def load_transactions(filepath):
    transactions : List[Transaction] = []
    with open(filepath) as f:
        first_line = f.readline().split()
        for line in f:
            el = line.split()
            if el[1] == '32':
                transactions.append(Transaction(first_line[8], el[1], el[2], el[3], el[5], el[13], el[15].replace('0', ''), el[16].strip()))
    return transactions

def set_is_sub(transactions : List[Transaction], subs : List[Sub]):
    for el in transactions:
        el.is_sub(subs)

def get_transactions_sub(transactions : List[Transaction]):
    transactions_sub : List[Transaction] = []
    for el in transactions:
        if el.sub == True:
            transactions_sub.append(el)
    return transactions_sub

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

def get_transaction_bad(transactions : List[Transaction] = []):
    bad_list : List[Transaction] = []
    count = 0
    for el in transactions:
        if el.series == '96':
            bad_list.append(el)
            count = count + 1
    print(count)
    return bad_list

def count(subs):
    i = 0
    for el in subs:
        i = i + 1
    return i 

def save_in_file(filepath, data):
    with open(filepath, 'w+') as f:
        for el in data:
            f.write(str(el) + '\n')


path = ".//transactions"
dir_list = os.listdir(path)
for dir in dir_list:
    print(f'folder: {dir}')
    file_list = os.listdir(path + "//" + dir)
    if count(file_list) > 0:
        for file in file_list:
            print(f'file: {file}')

sub_all = load_subs('subs.txt')
set_status_subs(sub_all)
sub_actual = get_sub_actual(sub_all)
transactions = load_multiple()
set_is_sub(transactions, sub_actual)
# print(*transactions)
transactions_sub = get_transactions_sub(transactions)
bad_list = get_transaction_bad(transactions_sub)
# print(*bad_list)

# count_in_month = {
#     'Jan' : 0,
#     'Feb' : 0,
#     'Mar' : 0,
#     'Apr' : 0,
#     'May' : 0,
#     'Jun' : 0,
#     'Jul' : 0,
#     'Aug' : 0,
#     'Sep' : 0,
#     'Oct' : 0,
#     'Nov' : 0,
#     'Dec' : 0,
# }


# for el in bad_list:
#     date = datetime.datetime.strptime(el.date, '%d.%m.%y').strftime('%b')
#     count_in_month[date] = count_in_month[date] + 1

# print(count_in_month)

save_in_file('result\\sub_all.txt', sub_all)
save_in_file('result\\sub_actual.txt', sub_actual)
save_in_file('result\\transactions.txt', transactions)
save_in_file('result\\transactions_sub.txt', transactions_sub)
save_in_file('result\\bad_list.txt', bad_list)