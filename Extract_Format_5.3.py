from datetime import datetime

list1 = ["random_2020-05-04 18:08_string", "random_string_2019-02-12 12:00", "string_random_2019-02-15 16:00"]
list2 = []
for items in list1:
    # match = re.search('\d{4}-\d{2}-\d{2}' ,items)
    datetime.strptime(items, "%Y-%m-%d")
    list2.append(items)
print(list2)
