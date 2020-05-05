import re
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix 
matrix = []
print("Enter the entries row wise:")

# For user input matrix:
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(input())
    matrix.append(a)

# Reading matrix column wise and printing it as string:
string=''
dig_extra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for y in range(C):
    for x in range(R):
        string += matrix[x][y]
        for i in dig_extra:
            string = string.replace(str(i),' ')
length = len(string) - len(re.sub(r'\W+', ' ', string))
string = re.sub(r'\W+', ' ', string[:-length]) + string[-length:]
print(string)


