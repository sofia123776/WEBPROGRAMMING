import random
def realnumber():

    print("Welcome to the number guessing game")
    lower = int(input("Enter the lower bound: "))
    upper= int(input("Enter the upper bound:"))

    realnumber = random.randint(lower,upper)
    guess = int(input("Guess the real number"))
    attempt=0
    while True:
        if guess < realnumber:
            print("The number is less than the real number")
            attempt +=1
            break

        elif guess > realnumber:
            print("The number is greater than the real number")
            break

        else:
            print(f"Congradulations you got the number at{attempt} attempts")
            break
        
realnumber()