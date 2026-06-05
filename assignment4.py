# question 1
# l=["manjot","ashish","vivek","sukh","dikshit"]
# print(l)
# n=input("enter name")
# l.append(n)
# print(l)
# a=input("enter name of most important friend ")
# b=int(input("enter your choice"))
# l.insert(b,a)
# print(l)

# question 2

# l1=[1,10,100,3,6,8]
# l1.insert(2,59)
# l1.insert(4,59)
# l1.insert(5,59)
# print(l1)
# l1.append(5)
# print(l1)
# print(len(l1))


#qustion 3
# new=[]
# l2=["cat","apple","bag","papaer","run"]
# for i in l2:
#     if len(i)<4:
#         new.append(i)
# print(new)


#question4 

# list=[]
# result=[]
# n=int(input("enter the range"))
# for i in range(n):
#     x=int(input("enter the number"))
#     list.append(x)
# print(list)

# for x in list:
#     if x%2==0:
        
#         result.append("even")
#     if  x%2!=0:
        
#         result.append("odd")
# print(result)

# question 5
# l=[]
# for i in range(1,1000+1):
#     if i%7==0:
#         l.append(i)
# print(l)


# question 6

# string="hello how are you"
# print(string.count(" "))


# quesion 7
list2=[]
a=[1,2,3,4]
b=[2,3,4,5]
for i in a:
    if i in b:
        list2.append(i)
print(list2)