# Keep imported packages to extend python at the very top.
# Import a package for a random number generator
from random import randint

# [] => Arrays, containing multiple values
# array values are given a number, starting with 0
# best to go imports then variables then actual code
choices = ["rock", "paper", "scissors"]

player_lives = 3
ai_lives = 3
total_lives = 3

#version 1, hard coded in
#player_choice = choices[0]
#print("index 0 in the choice array is " + player_choice + ", which is rock.")
print ("I have never lost at Rock Paper Scissors before. I cannot be defeated by a human.")
player_choice = input("Choose rock, paper, or scissors: ")
print ("So, you chose: " + player_choice)

# ai choice is random pick from the choices array
ai_choice = choices[randint(0, 2)]
print("I chose: " + ai_choice)

if ai_choice == player_choice: 
	print("Blast, a draw! I demand we play again!")

elif ai_choice == "rock":
	if player_choice == "scissors":
		print("YOU FOOL! My rock smashes your feeble scissors! You have lost!")
		player_lives -= 1
	else:
		print("DAMN your mighty paper. You have won this round, disgusting human.")
		ai_lives -= 1

elif ai_choice == "paper":
	if player_choice == "rock":
		print("Your pitiful rock is no match for my all-encompassing paper! You have lost!")
		player_lives -= 1
	else:
		print("Your sharp scissors mean nothing to me, a computer! Even if you have won this round.")
		ai_lives -= 1

elif ai_choice == "scissors":
	if player_choice == "paper":
		print("Your pathetic paper has been torn to shreds by my scissors, pathetic human! You lose!")
		player_lives -= 1
	else:
		print("You have won this round, neanderthal. But next time you may not have a rock to defend yourself with!")
		ai_lives -= 1

print("You now have", player_lives, "lives left,")
print("while I have", ai_lives)