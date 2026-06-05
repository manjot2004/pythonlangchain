# # # # # lecture_--- forloops  

# # # # a=int(input("enter number"))
# # # # b=int(input("upto"))

# # # # for x in range(1,b+1):
# # # #     print(a,"*",x,"=",a*x)


# # # for i in range(0,5):
# # #     for j in range(0,i+1):
# # #         print("*", end=" ")
# # #     print()

# for i in range(5,0, -1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
    
for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    
# #     while loop

# i=0
# while i<10:
#     print(i)
#     i+=1


# strings

# name=input("enter name")
# print(len(name))
# for i in range(len(name)):
#     print("manjot")