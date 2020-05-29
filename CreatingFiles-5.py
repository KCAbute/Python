# 5. In question 4, take data size as input along with number of files and folder location,
# take total data size as input. Write logic in program to split data among all the files


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
total_data_size = int(input("Total data size"))
isExist = os.path.exists(user_path)
# total_needed_size = no_of_files * 2048    # total needed memory

if check_memory(total_data_size, user_path) and isExist:

    for i in range(no_of_files):
        file_name = user_path + "abc" + str(i) + ".txt"
        f = open(file_name, "w")
        size_of_file = total_data_size / no_of_files
        str1 = "k" * int(size_of_file)
        f.write(str1)
        f.close()
print(str(no_of_files)+" numbers of files have generated"+" of size"+str(size_of_file))
