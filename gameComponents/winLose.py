from gameComponents import gameVars

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
			gameVars.player_choice = False
			print ("Very well. Prepare yourself; I will not go easy on you this time.")
			
		else: 
			print ("I said Yes or No, fool. How did you get this far if you cannot read?")
			choice = False
