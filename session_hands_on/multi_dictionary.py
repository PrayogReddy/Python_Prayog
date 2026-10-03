students = {
        111: {
            "details": {"name": "Ravi", "age": 30, "gender": "M"},
            "marks": {"English": 50, "Science": 60},
            "Contact": ["7868686"]
        },
        222: {
            "details": {"name": "Mahesh", "age": 35, "gender": "M"},
            "marks": {"English": 70, "Science": 40},
            "Contact": [7894636, 789983836]
        }
    }

# print(students)
# print(students[111]["marks"]["Science"])
# print(students.get(111).get("marks").get("Social", "Not Found"))
# students[111]["Contact"] = "78969769"
# print(students)
# students[222]["marks"]["Maths"] = 85
# print(students)
# students[333]= {
#             "details": {"name": "Priyanka", "age": 25, "gender": "F"},
#             "marks": {"English": 90, "Science": 78},
#             "Contact": ["9568654"]
#         }
# print(students)
# students.setdefault(444, {}).setdefault("marks", {})["Social"]=65
# print(students)
# res = students[222]["marks"].pop("lan", "Not Found")
# print(res)
# print(students)

# del students[222]
# print(students)

# for roll, info in students.items():
#     print(roll)
#     print(info)
#     name = info["details"]["name"]
#     english = info["marks"]["English"]
#     print(f"Roll {roll}: {name} - English {english}")

res={}
for i in range(1,5):
    res[i] = i*i
print(res)

res1 = {i: i*i for i in range(1,5)}
print(res1)

res_even = {i: i*i for i in range(1,11) if i%2==0}
print(res_even)

fruits = ["apple", "banana", "mango"]
len_fruits = {i: len(i) for i in fruits}
print(len_fruits)