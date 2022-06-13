print ("Welcome to the Rock, Paper and Scissors. Let's Begin")
print ("Basic Rules: Type R for Rock, S for Scissors and P for Paper")

import random 

while True:
  choices = ["R", "P", "S"]
  
  computer = random.choices(choices)
  player = none
  
  
  while player not in choices:
   print("Error! Wrong Choice. Try Again")
   player = input("R, P or S?:").lower()

  if player == computer
   print("computer {} : Player {}")
   print("TIE")
  
  elif player == "R"
   if computer == "P"
    print("computer {} : Player {}",computer,player)
    print("Computer Wins")
   if computer == "P"
    print("computer {} : Player {}",computer,player)
    print("Player Wins. Well Done.")

  elif player == "S"
   if computer == "R"
    print("computer {} : Player {}",computer,player)
    print("Computer Wins.")
   if computer == "P"
    print("computer {} : Player {}",computer,player)
    print("Player Wins. Well Done.")
   
   elif player == "P"
   if computer == "S"
    print("computer {} : Player {}",computer,player)
    print("Computer Wins")
   if computer == "R"
    print("computer {} : Player {}",computer,player)
    print("Player Wins. Well Done.")
   
   play_again = input("Play Again? Yes/No):").lower()

   if play_again!="yes"
    break

print("Bye!")

  
   



