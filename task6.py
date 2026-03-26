import random

choices = ["stone", "paper", "scissor"]

user = input("Enter stone, paper or scissor: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "stone" and computer == "scissor") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissor" and computer == "paper"):
    print("You win!")
elif user in choices:
    print("Computer wins!")
else:
    print("Invalid input!")