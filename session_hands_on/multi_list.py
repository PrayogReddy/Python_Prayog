# matrix = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]

# print(matrix)
# print(matrix[0])
# print(matrix[1][1])
# print(matrix[1][2])

# matrix[2][1]=15
# print(matrix)

# matrix.append([4,5,6])
# print(matrix)

# matrix.insert(2,[5,6,7])
# print(matrix)

# del matrix[3]
# print(matrix)

# del matrix[1][1]
# print(matrix)

# for i in matrix:
#     for value in i:
#         print(value, end= " ")
#     print()

# a = [[1,2,3], [4,5,6]]
# b=a.copy()
# print(a)
# print(b)
# b[1] = [7,8,9]
# print(a)
# print(b)
# a[0][1] = 45
# print(a)
# print(b)

##Q&A
demo_matrix = [
    [11,22,33],
    [44,55,66],
    [77,88,99]
]
print(demo_matrix)

print(demo_matrix[1][2])

demo_matrix[0][0]=100
print(demo_matrix)

demo_matrix.append([1,2,3])
print(demo_matrix)

del demo_matrix[3]
print(demo_matrix)

for i in demo_matrix:
    for j in i:
        print(j)

total_sum = 0
for i in demo_matrix:
    for j in i:
        total_sum += j
print("Total Sum:", total_sum)

students_marks = [
    ["Ravi", 30, 40],
    ["Mahesh", 50, 60],
    ["Suresh", 70, 80]
]
for i in students_marks:
    name = i[0]
    total_marks = sum(i[1:])
    print(name, total_marks)

list_a = [[1, 2], [3, 4]]
list_b = list_a.copy()
print(list_a)
print(list_b)
list_b[0][1] = 55
print(list_a)
print(list_b)

for i in demo_matrix:
    for value in i:
        print(value, end= " ")
    print()