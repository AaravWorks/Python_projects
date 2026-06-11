print("welcome to rock ,paper, scissors")
import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input(" rock, paper, scissors:")
print("system choose:", computer)
if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("YOU LOSE")
elif player == "paper" and computer == "rock":
    print("YOU WON")
elif player == "rock" and computer == "scissors":
    print("YOU WON")
elif player == "scissors" and computer == "rock":
    print("YOU LOSE")
elif player == "paper" and computer == "scissors":
    print("YOU LOSE")
elif player == "scissors" and computer == "paper":
    print("YOU WON")
else:
    print("invalid move please type from selected")
print("thanks for playing")
print("game over")


