import os
import re

def file_size(fname):
    size = os.stat(fname)
    length_of_file=size.st_size
    return length_of_file


print("Word count in file:", file_size("C:\\Users\\Kanchan\\PycharmProjects\\PythonAssignments\\Assignment-5-pre.txt"))
# Take substring from user to bring expected output.
sub_str = input('Enter a substring:')

#counters for various scenarios
count_with_regex = 0
count_without_regex = 0

count_start_substring = 0
count_not_starting_with_substring = 0

count_end_with_substring = 0
count_not_ending_with_substring = 0

count_within_substring = 0
count_not_within_substring = 0

# initializing multiple lists:

words_starting_with_substring = []
words_containing_substring = []
words_ending_with_substring= []

# Read a file
with open('C:\\Users\\Kanchan\\PycharmProjects\\PythonAssignments\\Assignment-5-pre.txt', "r") as f:
    for line in f:
        word = line.split()
        for items in word:
            if sub_str in items:
                count_within_substring += 1
                words_containing_substring.append(items)
            else:
                count_not_within_substring += 1
            if items.startswith('sub_str'):
                count_start_substring += 1
                words_starting_with_substring.append(items)
            else:
                count_not_starting_with_substring += 1
            if items.endswith('sub_str'):
                count_end_with_substring += 1
                words_ending_with_substring.append(items)
            else:
                count_not_ending_with_substring += 1
            reg_ex = re.match(r"^.*\b(is)\b.*$", items)
            if reg_ex:
                count_with_regex += 1
            else:
                count_without_regex += 1
f.close()
dict_of_count = {}
dict_of_count["word count starting with substring "] = count_start_substring
dict_of_count["word count containing substring "] = count_within_substring
dict_of_count["word count ending with substring "] = count_end_with_substring
dict_of_count["word count with regex"] = count_with_regex
dict_of_count["word count with not regex <^.*\b(is)\b.*$>"] = count_without_regex
dict_of_count["word count not starting with substring "] = count_not_starting_with_substring
dict_of_count["word count not containing substring "] = count_not_within_substring
dict_of_count["word count not ending with substring"] = count_not_ending_with_substring
dict_of_count["words starting with "] = words_starting_with_substring
dict_of_count["words containing "] = words_containing_substring
dict_of_count["Words end with substring"] = words_ending_with_substring
print(dict_of_count)



