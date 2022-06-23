import random


while True:
    print ("Welcome to the Game of Rock, Paper and Scissors. Select R for Rock, S for Scissors and P for Paper")
    choices = ["R", "P","S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("Pick either R, P or S")
        player = input ("R, P, S?: ").upper()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Its a tie. No one wins")
        pass

    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Loses")
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Wins")

    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Loses")
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Wins")

    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Loses")
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Player Wins")

    play_again = input ("Play again? (YES/NO): ").upper()

    if play_again != "Y":
        break

print("Good Game")


  
   



