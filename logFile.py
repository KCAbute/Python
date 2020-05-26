import random
from datetime import datetime
from datetime import date
import random
import re


f = open("C://Users//Kanchan//PycharmProjects//PythonAssignments//First_log.txt", "w")


def random_date():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    random_d=random_day.strftime("%d"'th '"%B %Y")
    return random_d


def file_log():
    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)
    for items in range(30):
        error_code = ['ERROR', 'WARNING', 'INFO', 'DEBUG', 'CRITICAL']
        n = random.randint(120, 130)
        # print(n)
        random_error = random.choice(error_code)
        # print(random_error)
        now = datetime.now()
        random_time = now.strftime(" %X")
        line = str(random_error)+':'+str(n)+':'+str(random_date())+':'+str(random_time)+'\n'
        f.write(line)


file_log()
f.close()
f = open("C://Users//Kanchan//PycharmProjects//PythonAssignments//First_log.txt", "r")
error_code = ['ERROR', 'WARNING', 'INFO', 'DEBUG', 'CRITICAL']

# initialize lists for counting purpose
error_list, warning_list, info_list, debug_list, critical_list = ([] for i in range(5))

for i in range(0, 30):
    f.readline()
    for items in f:
        items = items.strip()
        # print(items)
        items = items.upper()
        # print(items)
        word = items.split(':')
        if word[0] == error_code[0]:
            error_list.append(items)
        elif word[0] == error_code[1]:
            warning_list.append(items)
        elif word[0] == error_code[2]:
            info_list.append(items)
        elif word[0] == error_code[3]:
            debug_list.append(items)
        elif word[0] == error_code[4]:
            critical_list.append(items)

print(str(error_code[0])+':'+'occurs'+' '+str(len(error_list))+' '+'times')
print(str(error_code[1])+':'+'occurs'+' '+str(len(warning_list))+' '+'times')
print(str(error_code[2])+':'+'occurs'+' '+str(len(info_list))+' '+'times')
print(str(error_code[3])+':'+'occurs'+' '+str(len(debug_list))+' '+'times')
print(str(error_code[4])+':'+'occurs'+' '+str(len(critical_list))+' '+'times')

def count_of_error_code(list_all: []):
    empty_list=[]
    dictOfElems = dict()
    for elements in list_all:
        words_list = elements.split()
        for word1 in words_list:
            for k in re.findall(r'(?<!\d)\d{3}(?!\d)', word1):
                empty_list.append(k)
    print(empty_list)
    for i in empty_list:
        if i in dictOfElems:
            dictOfElems[i] += 1
        else:
            dictOfElems[i] = 1
    pr = 1
    global summation
    sum = 0
    for key, value in dictOfElems.items():
        pr = int(key) * value
        sum += pr
    return dictOfElems


print("{} occurs {} time".format(error_code[0], len(error_list)))
error_dic = count_of_error_code(error_list)
for key, value in error_dic.items():
    print("ERROR CODE", key, ': occurs', value, "times.")
print("ERROR Codes summation:", sum, '\n')
print("{} occurs {} time".format(error_code[1], len(warning_list)))
warning_dic = count_of_error_code(warning_list)
for key, value in warning_dic.items():
    print("WARNING CODE", key, ': occurs', value, "times.")
print("WARNING Codes summation:", sum, '\n')
print("{} occurs {} time".format(error_code[2], len(info_list)))
info_dic = count_of_error_code(info_list)
for key, value in info_dic.items():
    print("INFO CODE", key, ': occurs', value, "times.")
print("INFO Codes summation:", sum, '\n')
print("{} occurs {} time".format(error_code[3], len(debug_list)))
debug_dic = count_of_error_code(debug_list)
for key, value in debug_dic.items():
    print("DEBUG CODE", key, ': occurs', value, "times.")
print("DEBUG Codes summation:", sum, '\n')
print("{} occurs {} time".format(error_code[4], len(critical_list)))
critical_dic = count_of_error_code(critical_list)
for key, value in critical_dic.items():
    print("CRITICAL CODE", key, ': occurs', value, "times.")
print("CRITICAL Codes summation:", sum, '\n')

f.close()









