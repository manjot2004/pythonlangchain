'''list comprehension question'''

# num=[1,2,3,4,5,6,7,8,9,10]
# squares=[n**2 for n in range(1,11) ]
# print(squares)

# even_num=[x for x in range(1,21) if x%2==0]
# print(even_num)

# l=["ram","jatin","akash"]
# upper=[x.upper() for x in l]
# print(upper)

# length=[len(x) for x in l]
# print(length)


# l2=[n for n in range(1,101) if n%2==0 and n%5==0]
# print(l2)

t="hello world"
r=" ".join([char for char in t if char not in 'aeiou'])
print(r)



# m=[5*x for x in range(1,11)]
# print(m)
# tuple=[(n,n**2) for n in range(1,11)]
# print(tuple)


'''tuple questions'''

# t=("eng","hindi","math","science","sst","hindi")
# for x in t:
#     print(x)

# s=[i for i in t]
# print(s)
    
# print(t.count("hindi"))

# t1=(1,2,3,4)
# t2=(5,6,7,8)

# t3=t1+t2
# print(t3)


'''set questions'''

# s={1,2,3,4,5,6,7,8,9,10}
# for x in s:
#     print(x)

# s.update([11,12,13])
# print(s)

# s.remove(2)
# print(s)

# s.discard(13)
# print(s)

# s1={1,2,3,4}
# s2={4,3,7,8}

# print(s1.union(s2))
# print(s1 | s2)


# print(s1.intersection(s2))
# print(s1 & s2)

# print(s1.difference(s2))
# print(s1 - s2)


# s={22,2,5,33,53,}

# x=int(input("enter num"))

# if x in s:
#     print("exist")
# else:
#     print("not")

# final=["exist" if x in s else "not exist"]
# print(final)


# list=[1,2,3,2,4,5,6,5,6]

# unique=set(list)

# print("umique element=",unique)