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
