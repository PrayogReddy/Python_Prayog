from datetime import datetime, date, time

# print(datetime.now())
# print(date.today())
# print(datetime.now().time())
# print(date(2026, 4, 25))
# print(time(9, 33, 56))

# print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
# print(datetime.now().strftime("%d-%m-%Y"))
# print(datetime.now().strftime("%A, %B, %d"))
date1 = datetime.strptime("24-09-2026", "%d-%m-%Y")
date2 = datetime.strptime("10-03-2027", "%d-%m-%Y")
print(date2-date1)
print((date2-date1).days)
