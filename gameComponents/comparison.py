from gameComponents import gameVars

def whowon():
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