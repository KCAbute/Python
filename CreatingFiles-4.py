# 4. Write a program to create a given number of files parallely with some random data of 2048 char string.
# Your program should take folder location and number of files as input.


import random
import os.path
import shutil

# Ask for location.


def check_memory(memory_size_check, path):
    stat = shutil.disk_usage(path)
    # print(stat)
    if memory_size_check > stat[2]:
        print("Not sufficient memory")
        exit()
    else:
        return True


user_path = input("Enter location for creating files:")
no_of_files = int(input("Number of files you want to create? "))
isExist = os.path.exists(user_path)
total_needed_size = no_of_files * 2048    # total needed memory

if check_memory(total_needed_size, user_path) and isExist:

    for i in range(no_of_files):
        file_name = user_path + "abc" + str(i) + ".txt"
        f = open(file_name, "w")
        str1 = "k" * 2048
        f.write(str1)
        f.close()


