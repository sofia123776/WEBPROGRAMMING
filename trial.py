name = "sofia"
print(name)

age = 22

print("your age is:" +str(age) )

name = input("what is your name")
print("hello " +name)

adj = input("adjective..")
verb1 = input("verb1...")
verb2 = input("verb2...")
famous_person = input("name of famous person...")
madlib = f"you look so {adj} and the fact that you like {verb1} makes it so good for the {verb2} and {famous_person} likes it"
print(madlib)

import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a random number between 1 and {x}"))
        if guess < random_number:
            print("oh sorry try again,too low")
            
        elif guess > random_number:
            print("oh sorry try again,too high")
    print(f"woohooo congrats you guessed the number {random_number} correctly")        
        
guess(10)

for i in range(10,50,5):
    print(i)
for i in "sofia hafsa":
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

phone_number = "123_4573_6374"
for i in phone_number:
    if i == "_":
        continue
    print(i,end="")  
food =["Mandazi","Chapati","Chicken","Eggs","Chips","Mtura"]
food.insert(0,"Bajia")
for x in food:
    print(x)

utensils={"cup","knife","plate"}
{"spoon","pan","fork","knife"}
print(utensils.difference(dishes))
capitals={'uganda' : 'kampala',
         'kenya' : 'nairobi',
         'nigeria' : 'abuja'}
print(capitals['kenya'])

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])

age = input("How old are you?")
if age >= str(18):
    print("You are an adult")
else:
    print("You are a child")


spongebob = patrick = sandy =30
print(spongebob)
print(patrick)
print(sandy)

x=1
y=2.0
z="3"
print(x)
print(int(y))
print(z)

firstname="Sophie"
food="pizza"
email="sofiahafsa00@gmail.com"

print("Hello " + firstname)
print("You like " + food)
print(f"your email is: {email}")

age=25
quantity=10
print("You are " + str(age) + " years old")
print(f"you are buying {quantity} items")

age = 21
age += 1
print("your age is "+str(age))

firstname="Sofia"
lastname="Hafsa"
fullname= firstname+" "+lastname
print("hello " +fullname)

human=True
print("you are a "+str(human))

# a program to convert temp to Fahrenheit
celcius = float(input("Enter the temperature in celcius: "));
Farhenheit = celcius*(9/5)+32;

print("The temperature in Fahrenheit is: ",Farhenheit)

#program to get the factorial of a number
number =int(input("Enter a number: "));
Factorial = 1;
if number< 0:
    print("The number must be greater than 0,it should not be a negative number ");

else:
    print("You can continue ");

    for i in range(1,number +1):
     Factorial*=i   
    
print("The factorial of the number is",Factorial);

def min_and_max(numbers):
    return min(numbers), max(numbers)

result = min_and_max([1, 2, 3])
print("The minimum and maximum number is",min,max);

point = (10, 20)
x, y = point
print(x,y);

numbers =([1,20,23,45,67,23,80]);
total_number_of_numbers = 7
Average = sum(numbers)/total_number_of_numbers
print("The average of the numbers is",Average)


