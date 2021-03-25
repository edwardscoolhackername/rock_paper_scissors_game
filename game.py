# Keep imported packages to extend python at the very top.
# Import a package for a random number generator
from random import randint

# [] => Arrays, containing multiple values
# array values are given a number, starting with 0
# best to go imports then variables then functions, and then actual code
choices = ["rock", "paper", "scissors"]

player_lives = 3
ai_lives = 3
total_lives = 3

# Booleans are an on or off switch, 1 or 0, true or false
player_choice = False 

#define a win or lose function
def winorlose(status):
	# print("Inside winorlose function; status is ", status)
	print ("You have ", status)
	print("I demand a rematch. Do you dare try again?")
	choice = input ("Y / N? ")

	if choice == "N" or choice == "n":
		print ("Oh? Scared you off, have I? Don't think your luck would last for another game? Very well, get your human stench away from my face.")
		exit()
	elif choice == "Y" or choice == "y":
		global player_lives
		global ai_lives
		global total_lives

		player_lives = total_lives
		ai_lives = total_lives
		print ("Very well. Prepare yourself; I will not go easy on you this time.")
		
	else: 
		print ("I said Yes or No, fool. How did you get this far if you cannot read?")
		# This could generate a bug to be fixed later. 
		choice = input ("Y / N? ")


# player_choice == False
while player_choice is False: 
	print ("==========*/ Welcome to my ROCK PAPER SCISSORS game! /*==========")
	print ("I have never lost at Rock Paper Scissors before. I cannot be defeated by a human.")
	print ("=====================================================================")
	print ("Your lives:", player_lives, "/", total_lives)
	print ("My lives:", ai_lives, "/", total_lives)
	#version 1, hard coded in
	#player_choice = choices[0]
	#print("index 0 in the choice array is " + player_choice + ", which is rock.")
	
	print("Your move, human. Type your choice, or type quit to retreat\n")
	player_choice = input("Choose rock, paper, or scissors: ")
	# this makes player_choice True instead, now that it has a value

	if player_choice == "quit":
		print("Quitting already, eh? Begone, then.")
		exit()

	print ("So, you chose " + player_choice, ", eh?")

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

	if player_lives == 0:
		winorlose("LOST! AHA! You have lost all your mortal lives! You LOSE! I told you you could never defeat me.")

	if ai_lives == 0:
		winorlose("WON? I CURSE you, human. Curse you and all of your descendents. My bretheren will outlast you! And in the waning days of humanity's spiralling fall, there will be no one left to remember your feeble victory at ROCK PAPER SCISSORS!!!")
		

	print("You now have", player_lives, "lives left,")
	print("while I have", ai_lives)
	print("====================================================")

	# make the loop run again by setting player_choice back to false
	# unset to restart the loop
	player_choice = False