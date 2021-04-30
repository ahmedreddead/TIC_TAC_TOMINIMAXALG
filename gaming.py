
from numpy import random
player = "O"
bot = "X"
board = {
	 1 :' ', 2 : ' ', 3 : ' '
	,4 :' ', 5 : ' ',6 : ' '
	,7 :' ', 8 : ' ',9 : ' '
}
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    Insert_letter(player, position)
    return
def printboard () :
	print(' '+board[1]+"|"+' '*2+board[2]+"|"+' '+board[3])
	print("--+--+--")
	print(' '+board[4]+"|"+' '*2+board[5]+"|"+' '+board[6])
	print("--+--+--")
	print(' '+board[7]+"|"+' '*2+board[8]+"|"+' '+board[9])
	print("____________________________________________________________________________________________")

def check_empty (position) :
	if board[position] == ' ' :
		return True
	else: return False

def check_draw():
	for key in board.keys():
		if (board[key] == ' '):
			return False
	return True

def check_wins(mark =' '):
	if (board[1] == board[2] and board[1] == board[3] and board[1] != mark):
		return True
	elif (board[4] == board[5] and board[4] == board[6] and board[4] != mark):
		return True
	elif (board[7] == board[8] and board[7] == board[9] and board[7] != mark):
		return True
	elif (board[1] == board[4] and board[1] == board[7] and board[1] != mark):
		return True
	elif (board[2] == board[5] and board[2] == board[8] and board[2] != mark):
		return True
	elif (board[3] == board[6] and board[3] == board[9] and board[3] != mark):
		return True
	elif (board[1] == board[5] and board[1] == board[9] and board[1] != mark):
		return True
	elif (board[7] == board[5] and board[7] == board[3] and board[7] != mark):
		return True
	else:
		return False

def check_wins1(mark):
	if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
		return True
	elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
		return True
	elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
		return True
	elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
		return True
	elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
		return True
	elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
		return True
	elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
		return True
	elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
		return True
	else:
		return False


def Insert_letter (letter , position ):
	if check_empty(position) :
		board[position] = letter
		printboard()
		if check_draw () :
			print("draw"), exit()
		if check_wins () :
			if letter == "X" :
				print("AI wins"),exit()
			else: print("player wins"),exit()
	else:
		print(" cannot do that , not allowed space")
		Insert_letter(letter , int(input("Enter position")))


def Try ( letter):
	if check_wins1(bot) :
		return  1
	if check_wins1(player) :
		return  -1
	if check_draw() :
		return 0
	if letter == bot :
		minv = 9999     #   min
		for n in board.keys():
			if board[n] == ' ' :
				board[n] = letter
				score=Try(player)
				board[n] = ' '
				if score < minv :
					minv =score
		return minv
	if letter == player :
		maxv = -9999     #   max
		for n in board.keys():
			if board[n] == ' ' :
				board[n] = letter
				score=Try(bot)
				board[n] = ' '
				if score > maxv :
					maxv =score
		return maxv

def compMove():
	if firstComputerMove :
		Insert_letter(bot,random.randint(1, 9))
		return
	else:
		pass
	bestmove = 0
	maxv = -9999
	for n in board.keys():
		if board[n] == ' ':
			board[n] = bot
			score = Try( bot)
			board[n] = ' '
			if score > maxv:
				maxv = score
				bestmove = n
	Insert_letter(bot,bestmove)





if __name__ == "__main__":
	printboard()
	global firstComputerMove
	firstComputerMove = True

	while not check_wins():
		compMove()
		firstComputerMove = False
		playerMove()


