'''question 1'''


fruitsl=['banana\n','mango\n','orange\n']
with open('fruits.txt','w') as file:
    # file.writelines(fruitsl)
    for fruit in fruitsl:
        file.write(fruit)
    

'''question 2'''

try:
    with open('vegetables.txt','r')as file:
        content=file.read
        print(content)
except FileNotFoundError:
    print("file is not exist so filenot found error is come")

'''question 3'''

with open('fruits.txt','a')as file:
    file.write("apple\n")
    file.write("grapes\n")


'''question4 '''

with open('fruits.txt','r')as file:
    for line in file:
        print('fruit: {}'.format(line.strip()))
        
        
'''questin 5'''

try:
    num1=int(input("enter number: "))
    num2=int(input("enter numbe: "))
    result=num1/num2
    print(result)

except ValueError:
    print("try to divide by non number")
    
except ZeroDivisionError:
    print("try to divide number by zero")
else:
    print(result)
finally:
    print("division attempt finished")
    
    
'''question 6'''

my_colors = ["red", "blue", "green"]
student_info = {"name": "John", "grade": "A"}

try:
    print(my_colors[5])
except IndexError:
    print("index out of range")
    
try:
    print(student_info["age"])
except KeyError:
    print("key is found")


