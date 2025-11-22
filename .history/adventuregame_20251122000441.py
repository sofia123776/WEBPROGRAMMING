def startgame():
    print("Welcome to the adventure game!")
    print("You find yourself in a dimly light corridor and two paths ahead of you,on your right and on your left")

    choice1 = input("Choose either to go on RIGHT or LEFT").strip().lower()
    if choice1 == "right":
        darkroom()

    elif choice1 == "left":
        traproom()

    else:
        print("Invalid choice,please choose between the given choices")
    
        startgame()

def darkroom():
    print("\n In the dark room there is a flickering torch on the wall")
    choice2=input("TAKE the torch or KEEP MOVING").strip().lower()

    if choice2 == "take":
        print("\nYou will use the torch to lead you out,YOU HAVE WON THE GAME!")

    elif choice2 == "keep moving":
        print("\nYou leave without the torch you stamble and fall in the pit,GAME OVER!!")
        retry()
    else:
        print("Invalid choice,try again")
        darkroom()

def traproom():
    print("\n In the trap room there is a treasure box at the corner")
    choice3 = input("OPEN the box  or LEAVE:").strip().lower()

    if choice3 == "open":
        print("\nThe box has poisonous gas which kills you,GAME OVER!")
        retry()
    
    elif choice3 == "leave":
        print("\nYou leave the room safely,YOU HAVE WON THE GAME")
    else:
        print("Invalid choice,try again")
        traproom()

def retry():
    choice4 = input("Would you like to continue with the game,YES or NO:").strip().lower()

    if choice4 == "yes":
        print("\nThe game has started again!")
        startgame()

    elif choice4 == "no":
        print("\nThanks for playing")
        quit()

startgame()
    




