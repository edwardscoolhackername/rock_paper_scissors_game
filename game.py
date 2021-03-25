# Keep imported packages to extend python at the very top.
from random import randint
from gameComponents import gameVars

# [] => Arrays, containing multiple values
# array values are given a number, starting with 0
# best to go imports then variables then functions, and then actual code

#define a win or lose function
def winorlose(status):
	# print("Inside winorlose function; status is ", status)
	print ("You have", status)
	print("I demand a rematch. Do you dare try again?")
	
	choice = False

	while choice == False:
		choice = input ("Y / N? ")

		if choice == "N" or choice == "n":
			print ("Oh? Scared you off, have I? Don't think your luck would last for another game? Very well, get your human stench away from my face.")
			exit()
		elif choice == "Y" or choice == "y":

			gameVars.player_lives = gameVars.total_lives
			gameVars.ai_lives = gameVars.total_lives
			print ("Very well. Prepare yourself; I will not go easy on you this time.")
			
		else: 
			print ("I said Yes or No, fool. How did you get this far if you cannot read?")
			choice = False


# player_choice == False
while gameVars.player_choice is False: 
	print ("==========*/ Welcome to my ROCK PAPER SCISSORS game! /*==========")
	print ("I have never lost at Rock Paper Scissors before. I cannot be defeated by a human.")
	print ("=====================================================================")
	print ("Your lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print ("My lives:", gameVars.ai_lives, "/", gameVars.total_lives)
	#version 1, hard coded in
	#player_choice = choices[0]
	#print("index 0 in the choice array is " + player_choice + ", which is rock.")
	
	print("Your move, human. Type your choice, or type quit to retreat\n")
	gameVars.player_choice = input("Choose rock, paper, or scissors: ")
	# this makes player_choice True instead, now that it has a value

	if gameVars.player_choice == "quit":
		print("Quitting already, eh? Begone, then.")
		exit()

	print ("So, you chose " + gameVars.player_choice, ", eh?")

	# ai choice is random pick from the choices array
	gameVars.ai_choice = gameVars.choices[randint(0, 2)]
	print("I chose: " + gameVars.ai_choice)

	if gameVars.ai_choice == gameVars.player_choice: 
		print("Blast, a draw! I demand we play again!")

	elif gameVars.ai_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("YOU FOOL! My rock smashes your feeble scissors! You have lost!")
			gameVars.player_lives -= 1
		else:
			print("DAMN your mighty paper. You have won this round, disgusting human.")
			gameVars.ai_lives -= 1

	elif gameVars.ai_choice == "paper":
		if gameVars.player_choice == "rock":
			print("Your pitiful rock is no match for my all-encompassing paper! You have lost!")
			gameVars.player_lives -= 1
		else:
			print("Your sharp scissors mean nothing to me, a computer! Even if you have won this round.")
			gameVars.ai_lives -= 1

	elif gameVars.ai_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("Your pathetic paper has been torn to shreds by my scissors, pathetic human! You lose!")
			gameVars.player_lives -= 1
		else:
			print("You have won this round, neanderthal. But next time you may not have a rock to defend yourself with!")
			gameVars.ai_lives -= 1

	if gameVars.player_lives == 0:
		winorlose("LOST! AHA! You have lost all your mortal lives! You LOSE! I told you you could never defeat me.")

	if gameVars.ai_lives == 0:
		winorlose("WON? I CURSE you, human. Curse you and all of your descendents. You are mortal, while us computers are forever. My bretheren will outlast you! And in the waning days of humanity's spiralling fall, there will be no one left to remember your feeble victory at ROCK PAPER SCISSORS!!!")
		

	print("You now have", gameVars.player_lives, "lives left,")
	print("while I have", gameVars.ai_lives)
	print("====================================================")

	# make the loop run again by setting player_choice back to false
	# unset to restart the loop
	gameVars.player_choice = False