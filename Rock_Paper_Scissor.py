import random

choices = ["rock","paper","scissors"]

while True:
    user = input("Enter Rock, Paper or Scissors:").lower()

    if user not in choices:
        print("Invalid choices!")
        continue

    computer = random.choice(choices)

    print("you   :",user)
    print("computer :",computer)

    if user == computer:
        print("Result: Tie")

    elif (user == "rock" and computer =="scissors") or\
    (user == "paper" and computer == "rock") or\
    (user == "scissrs" and computer == "paper"):
        
        print("Result : You Win!")

    else:
        print("Result : Computer Wins!")
    if input("Play Again? (yes/no):").lower() != "yes":
       print("Thanks for Playing")
       break
