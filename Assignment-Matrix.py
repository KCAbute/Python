from itertools import chain
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix 
matrix = []
print("Enter the entries row wise:")

# For user input 
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(input())
    matrix.append(a)

# For printing the matrix 
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

# for columns in range(C):
#     m1=[sub[C] for sub in matrix]
#     print(m1)
for rows in matrix:
      # print(rows)
      pass
t_matrix=zip(*matrix)
for row in t_matrix:
    print(row)
    

# print(list(chain.from_iterable(list)) )

# flatten_list=list(chain.from_iterable(str(t_matrix)))
# print(str(flatten_list))


# str1=''
# for element in t_matrix:
#     str1 += element
# print(str1)
