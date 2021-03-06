# Keep imported packages to extend python at the very top.
from random import randint
from gameComponents import gameVars, winLose, comparison

# best to go imports then variables then functions, and then actual code


# player_choice == False
while gameVars.player_choice is False: 
	print ("==========*/ Welcome to my ROCK PAPER SCISSORS game! /*==========")
	print ("I have never lost this game. I cannot be defeated by a human.")
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

	print ("====================================================")
	print ("So, you chose " + gameVars.player_choice, ", eh?")

	# ai choice is random pick from the choices array
	gameVars.ai_choice = gameVars.choices[randint(0, 2)]
	print("I chose: " + gameVars.ai_choice, "\n")

	comparison.whowon()

	if gameVars.player_lives == 0:
		winLose.winorlose("LOST! AHA! You have lost all your mortal lives! You LOSE! I told you you could never defeat me.")

	if gameVars.ai_lives == 0:
		winLose.winorlose("WON? I CURSE you, human. Curse you and all of your descendents. You are mortal, while us computers are forever. My bretheren will outlast you! And in the waning days of humanity's spiralling fall, there will be no one left to remember your feeble victory at ROCK PAPER SCISSORS!!!")
		

	print("You now have", gameVars.player_lives, "lives left,")
	print("while I have", gameVars.ai_lives)
	print("====================================================")

	# make the loop run again by setting player_choice back to false
	# unset to restart the loop
	gameVars.player_choice = False