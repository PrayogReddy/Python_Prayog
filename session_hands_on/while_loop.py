# i=0
# while i<5:
#     print(i)
#     i = i + 1
#     #i+=1

# n = int(input("Enter a number: "))
# i=1
# s=0
# while s<n:
#     s = s + i
#     print(f"After adding {i} -> sum {s} ")
#     i = i + 1

# user = "admin"
# password = "admin123"
# max_login_attempts = 3
# login_attempts = 0

# while login_attempts < max_login_attempts:
#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")
#     if username_input == user and password_input == password:
#         print("Login successful!")
#         break
#     else:
#         login_attempts = login_attempts + 1
#         print("Invalid credentials.")
#         print(f"Login attempts left: {max_login_attempts-login_attempts}")
# else:
#     print("Maximum login attempts exceeded. Access denied.")

##Q&A
# i=1
# while i<=10:
#     print(i)
#     i+=1

# n = int(input("Enter a number: "))
# i = 1
# while i<=10:
#     print(n, "x", i, "=", n*i)
#     i+=1

# n=0
# i=1
# while i<=50:
#     n = n+i
#     i= i+1
# print(n)

# n= int(input("Enter a number: "))
# while n>=1:    
#     n = n/2
#     print(n)

# i = 1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

# n = abs(int(input("Enter a number: ")))
# if n==0:
#     digit_count = 1
# else:
#     digit_count = 0
#     while n>0:
#         n = n//10
#         digit_count += 1
# print(f"Number of digits in : {digit_count}")

# while True:
#     num = int(input("Enter a number (or 0 to stop): "))
#     if num == 0:
#         print("Stopping the loop.")
#         break        
#     print(f"You entered: {num}")

# num = int(input("Enter a number: "))
# i = 2
# while i < num:
#     if num % i == 0:
#         print("Not prime")
#         break
#     i += 1
# else:
#     print("Prime")

# count = 10
# while count >= 1:
#     print(count)
#     count = count - 1
# print("Liftoff!")

# number = 25
# guess = int(input("Guess the number: "))
# while guess != number:
#     if guess > number:
#         print("Too high")
#     else:
#         print("Too low")
#     guess = int(input("Guess again: "))
# print("Correct! You guessed it.")