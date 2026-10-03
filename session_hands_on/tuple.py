nums= (1,2,3,4)
print(nums[1])
print(nums[1:3])

t1=(1,2)
t2=(3,4)
print(t1+t2)

print(len(nums))

for i in nums:
    print(i)

print(nums.count(2))

print(nums.index(3))

print(nums * 2)

# nums[1]=8
# print(nums)

new_list = list(nums)
new_list[1]=8
print(new_list)

print(nums)