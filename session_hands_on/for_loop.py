# for i in range(10):
#     print(i)

# n= int(input("Enter a number: "))
# for i in range(1,11):
#     print(n, "x", i, "=", n*i)

# for i in range(1,11):
#     if i%3 !=0:
#         print(i)

# for i in range(1, 11, 3):
#     print(i)

# for i in range(1,7):
#     for j in range(1,7):
#         print(i, j)

# target = 6
# for i in range(1,7):
#     for j in range(1,7):
#         if i+j == target:
#             print(i, j)

# target = 6
# total = 36
# count = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == target:
#             count = count + 1

# prob =  (count / total)* 100
# print(f"pairs:{count}, Prob: {prob:.2f}%")

# target = 6
# total = 216
# count = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         for k in range(1, 7):
#             if i + j + k == target:
#                 count = count + 1

# prob =  (count / total)* 100
# print(f"pairs:{count}, Prob: {prob:.2f}%")

# for i in range(1, 11):
#     if i%2==0:
#         continue
#     print(i)

# for i in range(1, 11):
#     if i==5:
#         continue
#     print(i)

# def add_numbers(a, b):
#     result = a + b
#     return result 
#     print("This will never print!")
# total = add_numbers(5, 10)
# print(total)

# for number in range(1, 6):
#     if number == 3:
#         break
#     print(number)
# print("Loop ended!")

##Q&A
# for i in range(1, 11):
#     print(i)

# for i in range(1, 20):
#     if i%2 == 0:
#         print(i)

# n=4
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# for i in range(10, 0, -1):
#     print(i)

# num = int(input("Enter a number: "))
# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end="\t")
#     print()

# for i in range(1, 31):
#     if i % 3 == 0:
#         continue        
#     print(i)

# num = int(input("Enter a number: "))
# for i in range(1, 50):
#     if i == num:
#         print("Found")
#         break
# else:
#     print("Not Found")

# count = 0
# for i in range(1, 51):
#     if i%4==0 and i%6==0:
#         count = count + 1
# print(f"total numbers divisible by 4 and 6 between 1 and 50: {count}")