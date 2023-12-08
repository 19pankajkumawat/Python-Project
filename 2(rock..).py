import random
User = input("Select Rock, Paper, or Scissor :")
player2 = random.choice(["Rock", "Paper", "Scissor"])
print("Player 2 selected: ", player2)

if User == "rock" and player2 == "paper":
 print("player2 Won");
 
elif User == "paper" and player2 == "scissor":
 print("player2 Won");

elif User == "scissor" and player2 == "rock":
 print("player2 Won");
else:
 print("User WON")


