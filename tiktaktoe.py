def print_board():

	# Creates the black tik tak toe board. Each position links to the board list.

	print ("{} | {} | {}".format(board[6], board[7], board[8]))
	print("---------")
	print ("{} | {} | {}".format(board[3], board[4], board[5]))
	print("---------")
	print ("{} | {} | {}".format(board[0], board[1], board[2]))

def player_one_gameplay(player_one_position):

	# Player 1 move and mark on the tik tak toe board. Code ensures that players cannot overwrite each other's position
	# and that they can only post in an open position. board is printed after Player 1 move.

	player_one_position = player_one_position - 1
	while True:	
		if (board[player_one_position] != player_one_marker) and (board[player_one_position] !=player_two_marker):
			board[player_one_position] = player_one_marker 
			break
		else:
			player_one_position = int(input ("Sorry, that position is already choosen! Please pick another position (1-9) \n"))
			player_one_position = player_one_position - 1
	return print_board()	

def player_two_gameplay(player_two_position):

	# Player 2 move and mark on the tik tak toe board. Code ensures that players cannot overwrite each other's position
	# and that they can only post in an open position. Board is printed after Player 2 move.

	player_two_position = player_two_position - 1
	while True:
		if (board[player_two_position] != player_one_marker) and (board[player_two_position] !=player_two_marker):
			board[player_two_position] = player_two_marker 
			break
		else:
			player_two_position = int(input ("Sorry, that position is already choosen! Please pick another position (1-9) \n"))
			player_two_position = player_two_position - 1
	return print_board()

def turns():

	# Back and forth game plays. Ensures that Player 1 and 2 alternate turns. Once game is done due to no winner or Tik Tak Toe, 
	# users have the option to play again. Playagain() function is initiated upon tik tak toe or a draw.


	print_board()
	player_one_tl = True
	
	while board.count(" ") > 0 and ticktaktoe() == False:
		if player_one_tl == True:
			player_one_position = int(input ("Player 1: Choose your position (1-9) \n"))
			player_one_gameplay(player_one_position)
			player_one_tl = False
			ticktaktoe()
			

		elif player_one_tl == False:
			player_two_position = int(input ("Player 2: Choose your position (1-9) \n"))
			player_two_gameplay(player_two_position)	
			player_one_tl = True
			ticktaktoe()
	
	if ticktaktoe() == True:
		print("Tik Tak Toe!")
		playagain()
	else:
		print("Draw!")
		playagain()

def ticktaktoe():

	# All tik tak toe test scenarios

	if (((board[0] and board[1] and board[2]) != " ") and (board[0] == board[1] == board[2])):
		return True
	elif (((board[3] and board[4] and board[5]) != " ") and (board[3] == board[4] == board[5])):
		return True
	elif (((board[6] and board[7] and board[8]) != " ") and (board[6] == board[7] == board[8])):
		return True	
	elif (((board[0] and board[3] and board[6]) != " ") and (board[0] == board[3] == board[6])):
		return True
	elif (((board[1] and board[4] and board[7]) != " ") and (board[1] == board[4] == board[7])):
		return True
	elif (((board[2] and board[5] and board[8]) != " ") and (board[2] == board[5] == board[8])):
		return True
	elif (((board[2] and board[4] and board[6]) != " ") and (board[2] == board[4] == board[6])):
		return True	
	elif (((board[0] and board[4] and board[8]) != " ") and (board[0] == board[4] == board[8])):
		return True
	else:
		return False	

def playagain():

	# Allows user to replay or quit. If yes, main () is initiated (which is the intro of the game)

	again = input ("Would you like to plan again (yes or no)?")

	while True:
		if again == "yes":
			break
		elif again == "no":
			exit()
		else:
			print ("You did not enter yes or no, please enter only yes or no.\n")
			again = input ("Would you like to play again (yes or no)?\n")
	main()		
	
def main():

	# Intro where fresh board is created and players choose marker, initiates turns 

	global board
	
	board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	print ("Welcome to Tik Tak Toe!")
	
	global player_one_marker

	global player_two_marker

	player_one_marker = input("Player 1: Would you like to be X or O? \n ")

	while True:
		if player_one_marker == "X":
			player_two_marker = "O"
			break
		elif player_one_marker == "O":
			player_two_marker = "X"
			break
		else:
			print ("You did not enter an X or O")
			player_one_marker = input("Player 1: Please enter an X or O? \n ")	
		
	print ("Player 1 is {}".format(player_one_marker))
	print ("Player 2 is {}".format(player_two_marker))

	print ("Player 1 will now go first.")
	
	turns()

main()