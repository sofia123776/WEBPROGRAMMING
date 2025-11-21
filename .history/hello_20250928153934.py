print("Hello World!!")
name=("sophie","hafsa","atieno")
print(name[2])

number =int(input("insert a number"))
if number > 0:
    print("the number is positive")

elif number < 0:
    print("the number is negative")

else:
    print("number is 0")

for i in[0,1,2,3,4,5,5,6,7]:
    print(i)

names ={"kenya":"nairobi","uganda":"kampala"}
print(names["kenya"])

def square(x):
    return x*x
for i in range(10):
    print(f"the square of{i}is{square(i)}")
class point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2
p = point(6,7)
print(p.x)
print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
        
    def open_seats(self):
        return  self.capacity-len(self.passenger)
flight = Flight(3)
people=["sophie","hafsa", "maliha", "zainab"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")

    else:
        print(f"{person} not added the seats are all taken")
    

    def announce(f):
        def wrapper():
            print("about to use the function")
            f()
            print("already used the function")
        return wrapper
    @announce
    def hello():
        print("Hello world!")
    hello()

people = [ {"name":"sofia", "house":"sierra"},
          {"name":"zainab", "house":"luna"},
          {"name":"hafsa", "house":"zindeki"}]
def f(person):
    return person["name"]

people.sort(key =f)
print(people)