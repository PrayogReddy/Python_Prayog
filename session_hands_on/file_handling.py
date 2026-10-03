# file = open("log.txt", "r")
# print(file.read())
# file.close()

# file = open("log.txt", "r")
# print(file.read(3))
# file.close()

# file = open("log.txt", "r")
# print(file.readline())
# print(file.readline())
# file.close()

# file = open("log.txt", "r")
# print(file.readlines())
# file.close()

# file = open("log.txt", "r")
# print(file.read().splitlines())
# file.close()

# file = open("log.txt", "w")
# file.write("Hello \n")
# file.write("World!")
# file.close()

# file = open("log.txt", "w")
# file.write("Hi \n")
# file.write("World!")
# file.close()

# file = open("log.txt", "w")
# names = ["Ravi \n", "Mahesh \n", "Raju \n"]
# file.writelines(names)
# file.close()

# file = open("log.txt", "r")
# file.seek(6)
# res = file.read(3)
# print(res)
# file.close()

# file = open("log.txt", "r")
# print(file.tell())
# res = file.read(3)
# print(file.tell())
# print(res)
# file.close()

# with open("log.txt", "r") as file:
#     file.read()

# with open("log.txt", "a") as file:
#     file.write("Welcome")

# with open("log.txt", "r+") as file:
#     file.write("\nWelcome")
#     print(file.read())

# with open("config.txt", "r+") as file:
#     current_data = file.read()
#     print(f"current data in file: {current_data}")

#     file.seek(7)
#     file.write("Online")
#     file.truncate()

# with open("log.txt", "w+") as file:
#     file.write("Welcome")
#     print(file.read())

# with open("session.txt", "w+") as file:
#     file.write("Today's Log: User logged in at 09:00 AM")
#     file.seek(0)
#     print(file.read())

# with open("log.txt", "a+") as file:
#     file.write("\nHello")
#     print(file.tell())
#     file.seek(0)
#     print(file.read())

# with open("demo.jpg", "rb") as file:
#     data = file.read()
#     print(len(data))

# with open("copy.jpg", "wb") as c:
#     c.write(data)

# from datetime import datetime
# with open("logs.txt", "a") as f:
#     f.write(f"User1 logged in at: {datetime.now()}\n")

with open("config.txt", "r") as file:
    for line in file:
        key,value = line.strip().split("=")
        print(key, "=", value)
