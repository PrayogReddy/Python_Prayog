# students = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# print(students[1])
# print(students[-1])

# name = "Ravi"
# print(list(name))

# r =range(1,5)
# print(list(r))

# Sentence = ("Hello World")
# print(list(Sentence))
# print(list(Sentence.split()))

# a = [0, 1, 2, 3, 4, 5]
# print(a[1:4])
# print(a[:2])
# print(a[3:])
# print(a[::3])
# print(a[::-1])
# print(a[3:1:-1])

# students = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# students[2] = "Sravan"
# print(students)

# students.append("Ravi")
# print(students)

# students.extend(["Pranay", "Raju"])
# print(students)

# students.insert(1, "Kiran")
# print(students)

# students.remove("Ravi")
# print(students)

# nums = [1, 2, 3, 4, 5]
# nums.pop()
# nums.pop(1)
# nums.pop(8)
# print(nums)

# nums = [1, 2, 3, 4, 5, 1, 3, 1]
# while 1 in nums:
#     nums.remove(1)
# print(nums)

# students = ["Ravi", "Ramesh", "Suresh", "Ravi", "Raju", "Suresh"]
# Duplicates = ["Ravi", "Suresh"]
# for student in Duplicates:
#     while student in students:
#         students.remove(student)
# print(students)

# students = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# print(students.index("Suresh"))
# students.clear()
# print(students)

# nums = [1, 2, 3, 4, 2, 3, 1]
# print(nums.index(3,3,6))
# print(nums.count(4))

# marks = [40, 80, 70, 90, 50]
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)

# names = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# names.sort()
# print(names)
# names.sort(reverse=True)
# print(names)

# marks = [40, 80, 70, 90, 50]
# print(marks)
# new_marks = sorted(marks)
# print(new_marks)
# marks.reverse()
# print(marks)

# a = [1, 2, 3, 4]
# print(a)
# b = a
# print(b)
# b.append(5)
# print(b)
# b= a.copy()
# print(b)
# b.append(6)
# print(b)
# print(a)

# nums = [71, 20, 53, 42]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))

# students = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# print("Ravi" in students)
# print("Kiran" in students)
# print("Kiran" not in students)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# for f in fruits:
#     print(f)
# for i in range(len(fruits)):
#     print(i, fruits[i])
# for j, fruit in enumerate(fruits):
#     print(j, fruit)

# names = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# for name in names:
#     if name.startswith("R"):
#         print(name)

# nums = [5, 12, 33, 4, 15]
# Total = 0
# for n in nums:
#     Total = Total + n
# print(Total)

# nums = [1, 2, 3, 4, 5]
# res =[]
# for n in nums:
#     res.append(n*n)
# print(res)
# print([n*n for n in nums])

# even_nums = []
# for i in range(15):
#     if i%2==0:
#         even_nums.append(i)
# print(even_nums)
# print([x for x in range(15) if x%2==0])

# labels = []
# for i in range(5):
#     if i%2==0:
#         labels.append("even")
#     else:
#         labels.append("odd")
# print(labels)
# print(["even" if i%2==0 else "odd" for i in range(5)])

##Q&A
# nums = [1,2,3,4,5]
# print(len(nums))
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# fruits = ["Apple", "Mango", "Banana"]
# if "Mango" in fruits:
#     print("Mango found")
# else:
#     print("Mango not found")

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# a = [1, 2, 3]
# print(a)
# b= a.copy()
# print(b)
# b.append(4)
# print(b)
# print(a)

# a = [1, 2, 3]
# print(a)
# b = a
# print(b)
# b.append(4)
# print(b)
# print(a)

# print([n*n*n for n in range(1,10)])

# print([i for i in range(1,31) if i%3==0])

# print(["Positive" if i>0 else "non-positive" for i in range(1,11)])

# names = ["Ravi", "Ramesh", "Suresh", "Mahesh", "Rajesh"]
# print([i for i in names if i.startswith("R")])

# total_sum = 0
# for i in range(1,51):
#     if i%2==0:
#         total_sum = total_sum + i
#     else:
#         pass
# print(total_sum)

# total = sum([i for i in range(1,51) if i%2==0])
# print(total)