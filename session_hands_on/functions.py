# nums = [1,2,3,4,5]
# total = 0
# for n in nums:
#     total = total+n
# print(total)
# print(sum(nums))

# def greet():
#     print("Hello World")
# greet()
# greet()

# def greet1(name):
#     print("Hello", name)
# greet1("Ravi")
# greet1("Mahesh")

# def greet2(name1, name2):
#     print("Hello", name1 + " & " + name2)
# greet2("Ravi", "Mahesh")

# def math(a,b):
#     print(a+b)
# math(3,5)

# def add1(a,b):
#     print(a+b)
# res = add1(2,3)
# print(res)

# def add2(a,b):
#     return a+b
# res = add2(2,3)
# print(res)
# print(res*res)

# def greet(name="User"):
#     print("Hello", name)
# greet("Ravi")
# greet()

# def sub1(a,b):
#     print(a-b)
# sub1(4,2)
# sub1(a=5,b=1)
# sub1(a=1,b=5)

# def example(a,b,/,c,*,d):
#     return a+b+c+d
# print(example(1,2,3,d=4))
# print(example(a=1,b=2,c=3,d=4))
# print(example(1,2,c=3,d=4))
# print(example(3,5,c=2,d=40))

# def demo(a,b):
#     return a-b, a+b, a*b
# res = demo(3,5)
# print(res)
# sub, sum, mul = res
# print(sub, sum, mul)

# a=5
# def demo():
#     b=10
#     print("inside function: ", a, b)
#     return b
# demo()

# b=15
# print("outside function: ", a, b)

# def multi_args(a, *args, **kwargs):
#     print("a: ", a)
#     print("args: ", args)
#     print("kwargs: ", kwargs)
# multi_args(2,7,4,87,name="Ravi", age= 30)

# def add(a: int, b: int):
#     return a+b
# print(add(3,5))
# print(add("3","5"))

def multi(a,b):
    return a*b

def area_rectangle(len,wid):
    return multi(len,wid)
print(area_rectangle(2,3))