# students = {
#     "name" : "Ravi",
#     "age" : 30,
#     "roll no." : 535358
# }
# print(students)

# unique1 = {
#     "name" : "Ravi",
#     "age" : 30,
#     "name" : "Mahesh"
# }
# print(unique1)

# students = {
#     "name" : "Ravi",
#     "age" : 30,
#     "roll no." : 535358
# }
# print(students["name"])
# print(students["number"])
# print(students.get("age"))
# print(students.get("number", "Not Found"))

# students["name"] = "Mahesh"
# print(students)
# students["gender"] = "Male"
# print(students)

# students.update({"Address" : "Hyd" , "Pincode" : 500072})
# print(students)

# p1 = {
#     "name" : "Ravi",
#     "age" : 30
# }
# res = p1.pop("age")
# print(p1)
# print(res)
# res1 = p1.pop("gender", "Not found")
# print(p1)
# print(res1)

# del p1[3]
# print(p1)
# p1.popitem()
# print(p1)
# p1.clear()
# print(p1)

# students = {
#     "name" : "Ravi",
#     "age" : 30,
#     "roll no." : 535358
# }
# print(students.keys())
# print(students.values())
# print(students.items())

# for key in students.keys():
#     print(key)

# for key, value in students.items():
#     print(key, value)

a = {"x":1, "y":2}
b = {"y":3, "z":2}
# a.update(b)
# print(a)
# print(b)

merge = {**a, **b}
print(merge)