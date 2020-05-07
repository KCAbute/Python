import os
# path = "C:\\Users\\Kanchan"
# usage = os.path.getsize(path)
# print('size of %s' % path, usage)
# print(usage)

import shutil

# os.stat("C:\\Users\\Kanchan\\newfile.txt").st_size
path = "C:\\Users\\Kanchan"
stat = shutil.disk_usage(path)
print(stat)
remain = stat[1]*100/stat[0]
print(remain)
# remain=64667652096*100/523611664384
print("How much you want to fill in %")
fill = input()
fill_to_memory = int(fill)-int(remain)
print(fill_to_memory)

f = open('C:\\Users\\Kanchan\\newfile.txt', "wb")
f.seek(fill_to_memory-1)
f.write(b"\0")
f.close()

