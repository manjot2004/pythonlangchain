'''question 1'''
import random
import string

def generate_password():
    chars=string.ascii_letters+string.digits
    password=" ".join(random.choice(chars ) for i in range(8))
    return password

print("generated password:",generate_password())


'''question 2'''

def calculate_bmi(weight,height):
    bmi=weight/height**2
    print(bmi)
calculate_bmi(60,1.8)

'''question 3'''
def book_flight(destination,classtype="economy"):
    return f"flight booked to {destination} in {classtype} class"
destination=input("enter destination")
classtype=input("enter classd")
if classtype=="":
   print(book_flight(destination))
else:
   print(book_flight(destination,classtype))


'''qustion 4'''

def create_profile(username, age, country='Unknown'):
    return{ f"name: {username} , age: {age}, country: {country}"}

profile=create_profile(age=20,country="india",username="sukh")
print(profile)

'''question 5'''

def concatenate_words(*words):
    return "-".join(words)
print(concatenate_words("sukh","loves","preeti","but","preeti","not"))

'''question 6'''

def build_configration(**settings):
   
   
    for i,j in settings.items():
        print(f"{i}={j}")
        print(i,"=",j)
        
        
    
    
   
    
build_configration(theme='dark', debug=True, max_users=100)    