# numbers = [1, 2, 2, 3, 3, 4]
# dup = []
# for num in numbers:
#     if num not in dup:
#         dup.append(num)
# print(dup)

# unique = list(set(numbers))
# print(unique)

#########################################

# try:
#     x = int(input("Enter a value:"))

# except Exception as e:
#     print(f"Invalid input: {e}")

# try:
#     x = int(input("Enter a value:"))
# except ValueError:
#     print("Enter a valid value")

# try:
#     x = int(input())
# except ValueError as e:
#     print(f"Invalid input: {e}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     if num %2==0:
#         print(num)

# numbers = [10, 20, 5, 50, 30, 100]
# print(max(numbers))

# numbers = [10, 20, 20, 5, 5, 50, 30, 100, 100]
# print(set(numbers))

# try:
#     data = {"name": "Kiran"}
#     print(data["age"])
# except KeyError as k:
#     print("Enter a correct key")

# age = 30
# print("Age is:", age)

# with open("demo.txt", "r") as a:
#     res = a.read

# import os
# if os.path.exists("app.log"):
#     with open("app.log", "r") as f:
#         data = f.read()
#         print(data)
# else:
#     print("File not found")

# result = 100 / 0

# import os
# # print("Current directory: ", os.getcwd())

# os.system("ls")

#########################################

# try:
#     with open("app.log", "r") as file:
#         data = file.read()
# except FileNotFoundError:
#     print("File does not exist")
# except PermissionError:
#     print("Permission denied")
# except Exception as e:
#     print("Unexpected error:", e)
# print(data)

# def sum(a,b):
#     return a+b
# print(sum(1,2))

# import random
# for attempt in range(3):
#     success = random.choice([True, False])
#     if success:
#         print("Operation successful")
#         break
#     print("Attempt failed")
# else:
#     print("All attempts failed")

# import os

# region = os.getenv("AWS_REGION", "us-east-1")

# print(region)

# from pathlib import Path
# for file in Path(".").rglob("*.log"):
#     print(file)

#########################################

# a=1
# b=2

# if a==b:
#     print("true")
# else:
#     print("false")

# if a is b:
#     print("true")
# else:
#     print("false")

# import os
# os.mkdir("logs")

# count = 0
# with open("app.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             count += 1
# print("Total errors found: ", count)