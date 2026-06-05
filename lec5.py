# list comprehension


# names=["ram","jatin","akash"]
# upper_names=[n.upper() for n in names]
# print(upper_names)


# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=[x for x in numbers if x%2==0]
# print(even)

# s=["even" if x%2==0 else "odd" for x in numbers]

# print(s)

# l=[21,56,12,-12,15,-25,-30,58,-9,28,-18]

# s=[x if x>0 else 0 for x in l]
# print(s)
# n=[4,5,6,7,8]
# greater50=[x for x in n if x**2>50]
# print(greater50)

# words=["apple","dog","elephant","banana"]
# s=[x for x in words if len(x)>5]
# print(s)


'''tuples'''
'''it is immutuable, stores the value in ordered format, '''

# a=1,2,3,4,5
# b=(1,2,3,4)
# c=(1)
# d=(2,)

# print(a)
# print(type(b))
# print(type(c))
# print(type(d))


'''sets'''
''' ti is mutuble,  unindexed, store values in unordered format,do not allow duplictae values,, defined by {} brackets'''

# a={}
# d=set()
# b={1,2,3,4}
# print(type(a))
# print(type(d))
# print(type(b))

# s1={23,4,5,3,3,"manjot"}
# # print(s1)


# for s in s1:
#     print(s,end=" ")

# s1.update(["vivek", 2,23])
# print(*s1)

a={1,2,3,4}
b={3,4,5,6}

print(a.union(b)) # |
print(a.intersection(b)) #  &
print()