# n= int(input("Enter a number: "))

# if n>=0:
#     print("the nunbers is +ve")
#     print("Inside the if block")
# else:
#     print("the number is not +ve")

# print("Outside the if-else block")

# n= int(input("Enter a number: "))

# if n>0:
#     print("the nunbers is +ve")
# elif n==0:
#     print("the number is zero")
# else:
#     print("the number is -ve")

# n= int(input("Enter a number: "))

# if n%3==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# age = int(input("Enter Age: "))

# if age<10:
#     print("You are a child.")
# else:
#     if age<=17:
#         print("You are a teenager.")
#     else:
#         print("You are an adult.")

# age = int(input("Enter Age: "))
# member = True

# if age>18:
#     if member:
#         print("price is 10")
#     else:
#         print("price is 15")
# else:
#     if member:
#         print("price is 5")
#     else:
#         print("price is 1")

# x=-5

# value = "x is +ve" if x>0 else "x is -ve"
# print(value)

# print("even" if 11%2==0 else "odd")

# age = int(input("Enter Age: "))
# print("child" if age<10 else "teenager" if age<=17 else "adult")

##Q&A
# data = input("Enter a number: ")

# if data.isdigit():
#     print("It is an integer")
# else:
#     print("It is not an integer")

# while True:
#     try:
#         data = int(input("Enter your age: "))
#         break
#     except ValueError:
#         print("Please enter a valid integer.")
# print("Entered age is: ", data)

# n= int(input("Enter a number: "))
# if n>0:
#     print("the nunbers is +ve")
# elif n==0:
#     print("the number is zero")
# else:
#     print("the number is -ve")

# n= int(input("Enter a number: "))
# if n%4==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# a=5
# b=10
# c=15
# if a>b and a>c:
#     print("a is the largest number")
# elif b>a and b>c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")

# year = int(input("Enter a year: "))
# if year%4==0:
#     print("The year is a leap year")
# else:
#     print("The year is not a leap year")

# marks = int(input("Enter your marks: "))
# if marks>=90:
#     print("Grade A+")
# elif marks>=75:
#     print("Grade A")
# elif marks>=50:
#     print("Grade B")
# else:
#     print("Fail")

# age = int(input("Enter Age: "))
# if age<13:
#     print("You are a child.")
# else:
#     if age<=19:
#         print("You are a teenager.")
#     else:
#         print("You are an adult.")

# num = int(input("enter a number: "))
# if (num%3==0 and num%5==0):
#     print("Divisible by both 3 and 5")
# else:
#     if num%3==0:
#         print("Divisible by 3")
#     elif num%5==0:
#         print("Divisible by 5")
#     else:
#         print("Not divisible by 3 or 5")

# text = input("Enter a sinlgle character: ")
# if len(text)!=1 or not text.isalpha():
#     print("Invalid input. Please enter a single alphabetic character.")
# elif text in ("a", "e", "i", "o", "u"):
#     print("The character is a vowel.")
# else:
#     print("The character is a consonant.")

# print("even" if 12%2==0 else "odd")

# price = int(input("Enter Item Price: "))
# member = False
# if member:
#     final_price = price * 0.9  # 10% discount for members
#     print("Final price for member: ", final_price)
# else:
#     final_price = price  # No discount for non-members
#     print("Final price for non-member: ", final_price)