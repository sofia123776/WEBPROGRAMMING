print("let's play a game about the computer")
playing =input("Are you ready to play the game? ")
if playing != "yes":
    quit()
print("Okay let's have some fun!")
score = 0
answer =input("What is the CPU meaning ")
if answer =="central processing unit":
    print("correct!")
    score += 1               
else: 
    print("incorrect!")

answer =input("What is the GPU meaning ")
if answer == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
print("You got "+str(score)+ "question")   
print("You got "+str(score/2 *100)+ "%" )
    

