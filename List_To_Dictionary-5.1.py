# 1. Given a list of files
# ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]
# create dictionary with key representing the extension of file and value containing list of file names with that extension
# e.g.
# {
# ".txt": ["file1.txt", "file2.txt", "file2.ppt.txt"]
# }
# Note: .ppt.txt will be considered as .txt extension type
#
# list1 = ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]
# final_dict = dict_to_list = {}
#
# # Lists for names and extensions
# extensions, first_names = ([] for i in range(2))
# for items in list1:
#     words = items.rsplit(".", 1)
#     extensions.append(words)
# print(extensions)
#
# for items in extensions:
#     for i in items:
#         dict[i].append(items[i])
#
#     final_dict[tuple(items[1:])] = tuple(items[:1])
# print(str(final_dict))


# use rsplit  str.rsplit(separator, maxsplit)  ==? rsplit('.', 1)   =>split string at last occurance of '.'
# Use join
# re.split
# os.path.splittext(filename)
import os
list_of_files = ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]
print("\nList of files : ", list_of_files)


def find_file(lst):
    list1 = []
    converted_dict = {}
    for file_ in lst:
        name, ext1 = os.path.splitext(file_)
        list1.append(ext1)
        list_2 = list(set(list1))
    for i in range(0, len(list_2)):
        ll = []
        for file1 in lst:
            name, ext = os.path.splitext(file1)
            if list_2[i] == ext:
                ll.append(file1)
        converted_dict[list_2[i]] = ll
    print('Output : ', converted_dict)
    return converted_dict


find_file(list_of_files)
