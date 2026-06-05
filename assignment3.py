# # question 1 

# n=int(input("enter number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# question 2

# a=int(input("enter number"))
# b=int(input("upto"))

# for x in range(1,b+1):
#      print(a,"*",x,"=",a*x)


# question 3 

# n=int(input("enter number to check whether it is prime or not"))

# if n<=1:
#     print("not prime")
# else:
#    for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#    else:
#     print("prime")

# question 4

# num=input("enter the number")
# s=n[::-1]
# print(s)
# if n==s:
#     print("the number is palidrome")
# else:
#     print("the number is not palidrome")

# original=num
# reverse=0

# while num > 0:
#     digit=num % 10
#     reverse=reverse*10 + digit
#     num= num // 10

# if original==reverse:
#     print("palidrome")
# else:
#     print("not palidrome")


# question 5


# for i in range(1,101):
    
 
#     if  i%3==0 and i%5==0:
#        print("Fizzbuzz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0:
#         print("Fizz")
#     else:
#        print(i)


# question 6


# n=input("enter the name")
# age=int(input("enter age"))

# print("choose a class")
# print("1. first class - $1500")
# print("2. second class - $1000")
# print("3. slepper class - $500")

# choice=int(input("enter your choice(1-3):"))
# if choice==1:
#     fare=1500
#     travel_class="first class"
# elif choice==2:
#     fare=1000
#     travel_class="second class"
# elif choice==3:
#     fare=500
#     travel_class="sleeper class"
# else:
#     print("invalid choice")
#     exit()
    
# if age<5:
#     fare=0
# elif age>=60:
#     fare=fare - (fare*20/100)
    
# meal=input("do you want meal (yesor no):")
# if meal=="yes":
#     fare+=200


# print("passenger name:",n)
# print("age:",age)
# print("class: ",travel_class)
# print("meal added:",meal)
# print("final fare:$",fare)

print("MENU..")

print("1.whopper burger - $150")
print("2.crispy veg - $100")
print("3.chicken wings - $120")

choice=int(input("enter the item number(1/2/3):"))
if choice==1:
    fare=150
elif choice==2:
    fare=100
elif choice==3:
    fare=120
else:
    print("invalid choice")
    
q=int(input("enter the quantity:"))
original_amount=q*fare
final_price=original_amount

c=input("do you any coupon code (yes/no):")
if c=="yes":
    code=input("enter your coupon code")
    if code=="king50":
      final_price=final_price-(final_price*50/100)
      discount_amount="50%"
    
    elif code=="bk20":
      final_price=final_price-20
      discount_amount="$20 off"
    else:
     print("invalid coupon code")

else:
    print("final price",final_price) 
    
      
    
    
print("original price: ",original_amount)
print("discount applied: ",discount_amount)    
print("final price: ",final_price)

