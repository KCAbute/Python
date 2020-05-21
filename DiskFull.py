import shutil
import os


def memory_usage_info():

    total, used, free = shutil.disk_usage("/")
    total_mem = (total//(2 ** 30))
    used_mem = (used // (2 ** 30))
    free_mem = (free //(2 ** 30))
    storage_list = total_mem, used_mem, free_mem
    print("Your current memory status of c drive in GB:")
    print(storage_list)
    return storage_list


def mem_conversion(fill):

    mem_info = memory_usage_info()
    mem_used_in_percentage = mem_info[1]/mem_info[0]*100
    print('mem_used_in_percentage: '+str(mem_used_in_percentage)+" %")
    memory_to_fill_in_gb = int(fill) - int(mem_used_in_percentage)  # here you will get number of % user want to fill
    if mem_used_in_percentage> int(fill):
        print("Memory is already "+str(mem_used_in_percentage)+' occupied')
        exit()
    else:
        # need to convert that into GB now
        in_gb = (memory_to_fill_in_gb / 100) * mem_info[0]
    # call gb_to_bytes function to convert gb to bytes
    in_bytes_01 = gb_to_bytes(in_gb)
    return in_bytes_01
    # remain=64667652096*100/523611664384


def gb_to_bytes(in_gb):

    in_byte = in_gb*1024*1024*1024
    print('memory in_byte:'+str(in_byte)+' bytes')
    return in_byte


def fill_memory():

    print("How much you want to fill in %")
    fill = input()  # user will enter in percentage
    f = open('C:\\Users\\Kanchan\\newfile.txt', "wb")
    mem_in_bytes_01 = mem_conversion(fill)
    f.seek(int(mem_in_bytes_01)-1)
    f.write(b"\0")
    f.close()


def free_memory():
    if os.path.exists('C:\\Users\\Kanchan\\newfile.txt'):
        os.remove('C:\\Users\\Kanchan\\newfile.txt')
    else:
        print("The file does not exist")


# os.system('df -h')
fill_memory()
# memory_usage_info()
# If want to check current size
total, used, free = shutil.disk_usage("/")
total_mem = (total//(2**30))
used_mem = (used // (2 ** 30))
free_mem = (free // (2 ** 30))
storage_list = total_mem, used_mem, free_mem
print(storage_list)
# Memory used in % after filling the memory as per user input.
mem_used_in_percentage = storage_list[1]/storage_list[0]*100
print('mem_used_in_percentage '+str(mem_used_in_percentage)+' %')
free_memory()
total, used, free = shutil.disk_usage("/")
total_mem = (total//(2**30))
used_mem = (used // (2 ** 30))
free_mem = (free // (2 ** 30))
storage_list = total_mem, used_mem, free_mem
print(storage_list)
# Memory used in % after filling the memory as per user input.
print("After clearing momory ")
mem_used_in_percentage = storage_list[1]/storage_list[0]*100
print('mem_used_in_percentage '+str(mem_used_in_percentage)+' %')

