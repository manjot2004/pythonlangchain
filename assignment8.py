def separate_section(title):
    print("\n" + "="*20 + " " + title + " " + "="*20)
    
separate_section("lambda questions ")


separate_section("question 1")

calculate_volume= lambda l,w,h:l*w*h
print("volume of rectnagel prism=",calculate_volume(2,3,4))


separate_section("question 2")

even=lambda n:"true" if n%2==0 else "false"
print(even(4))

separate_section("question 3")

str=lambda s:s[::-1]
print(str("sukh hates preeti"))

separate_section("map questions ")
separate_section("1 question ")


l=["15","42","7"]
con=map(int,l)
print("integer=",list(con))

separate_section("2 question")

str=["sukh ","loves", "preeti"]
def upper(word):
    return word.upper()
uppercase=map(upper,str)
print(list(uppercase))

num=list(input("enter your string").split(","))
print(num)
upper_case=list(map(str.upper,num))
print(upper_case)

separate_section("3 question")


l=[1,2,3,4,5]
num=map(lambda x:x**2,l)
print("squared numbers=",list(num))

separate_section("filter question")

separate_section("1 question")

l=[1,-2,3,-4,5]
positive_numbers=filter(lambda x:x>0,l)
print("postive numbers=",list(positive_numbers))

separate_section("2 question")


words=["apple","banana","bat","run","elephant"]
longer=filter(lambda word:len(word)>5,words)
print("longer than 5 character=",list(longer))

separate_section("3 question")
num=[10,"sukh",69,"preeti"]
# num=list(input("enter your string").split(","))
# print(num)
strings=filter(lambda x:isinstance(x,str),num)
print(list(strings))


separate_section("enumerate question")

separate_section("1 question")

fruits=["apple","mango","banana"]
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
    
separate_section("2 question")

str="python"
for index,x in list(enumerate(str)):
    print(index,x)
    
str="python"
result=list(enumerate(str))
print(result)

separate_section("3 question")

l1=["True","False","True"]
for i,j in enumerate(l1,start=1):
    if j=="True":
        print(i,j)























