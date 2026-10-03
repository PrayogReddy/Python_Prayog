# try:
#     int(input("Enter a number: "))
# except:
#     print("Enter a valid number")

# try:
#     num = int(input("Enter a number: "))
#     print(f"Value entered: {num}")
#     res = 20/num
#     print(f"Result: {res}")
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Plese enter a valid number greater than zero")

# try:
#     num = int(input("Enter a number: "))
#     res = 20/num
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Plese enter a valid number greater than zero")
# else:
#     print(f"Result: {res}")

# val = None
# try:
#     val = open("log.txt", "r")
#     print(val.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     if val is not None:
#         val.close()
#         print("File Closed")

def validate_age(age):
    if age<0:
        raise ValueError("Please enter a postive value")
    ticket_price = 1000/age
    return ticket_price
try:
    user_age = int(input("Enter a number: "))
    res = validate_age(user_age)
except ValueError as v:
    print(v)
except ZeroDivisionError:
    print("Please enter a number greater than zero")
else:
    print(f"Ticket Price is: {res}")
finally:
    print("Program completed")