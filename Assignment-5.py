import os


def file_size(fname):
    size = os.stat(fname)
    length_of_file=size.st_size
    return length_of_file


print("File size", file_size("C:\\Users\\Kanchan\\PycharmProjects\\PythonAssignments\\Assignment-5-pre.txt"))


# # Take substring from user to bring expected output.
sub_str = input('Enter a substring:')
compare = {}
count_start_substring = 0
count_end_with_substring = 0
count_within_substring = 0

# Read a file
f = open('C:\\Users\\Kanchan\\PycharmProjects\\PythonAssignments\\Assignment-5-pre.txt', "r")
# f.readlines()
file_length = file_size("C:\\Users\\Kanchan\\PycharmProjects\\PythonAssignments\\Assignment-5-pre.txt")
for i in range(file_length):
    f.readlines()
    for items in f:
        items = items.strip()
        print(items)
        items = items.upper()
        print(items)
        word = items.split(' ')
        if word.find(sub_str):
            count_within_substring += 1
        if word.startswith('sub_str'):
            count_start_substring += 1
        if word.endswith('sub_str'):
            count_end_with_substring += 1
print(count_within_substring)
print(count_start_substring)
print(count_end_with_substring)



