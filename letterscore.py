# A library to convert letters into numbers

# Currently implemented:
	# 1) capitalletterscore(char) : function that takes upper case A-Z characters and assigns A=1...Z=26 to them
	# 2) lowercaseletterscore(char) : function that takes lower case a-z characters and assigns a=1...z=26 to them
	# 3) allletterscore(char) : function that takes upper and lower case A-Z and a-z characters and assigns a=1,A=1...z=26,Z=26 to them
	# 4) scrabblescore(char) : function that takes upper case A-Z and assigns Scrabble tile scoring to them.
	

def capitalletterscore(char):
	letterscore = 0
	
	if char == "A":
		letterscore = 1
	elif char == "B":
		letterscore = 2
	elif char == "C":
		letterscore = 3
	elif char == "D":
		letterscore = 4
	elif char == "E":
		letterscore = 5
	elif char == "F":
		letterscore = 6
	elif char == "G":
		letterscore = 7
	elif char == "H":
		letterscore = 8
	elif char == "I":
		letterscore = 9
	elif char == "J":
		letterscore = 10
	elif char == "K":
		letterscore = 11
	elif char == "L":
		letterscore = 12
	elif char == "M":
		letterscore = 13
	elif char == "N":
		letterscore = 14
	elif char == "O":
		letterscore = 15
	elif char == "P":
		letterscore = 16
	elif char == "Q":
		letterscore = 17
	elif char == "R":
		letterscore = 18
	elif char == "S":
		letterscore = 19
	elif char == "T":
		letterscore = 20
	elif char == "U":
		letterscore = 21
	elif char == "V":
		letterscore = 22
	elif char == "W":
		letterscore = 23
	elif char == "X":
		letterscore = 24
	elif char == "Y":
		letterscore = 25
	elif char == "Z":
		letterscore = 26
	else:
		break
	
	return letterscore

def lowercaseletterscore(char):
	letterscore = 0
	
	if char == "A":
		letterscore = 1
	elif char == "B":
		letterscore = 2
	elif char == "C":
		letterscore = 3
	elif char == "D":
		letterscore = 4
	elif char == "E":
		letterscore = 5
	elif char == "F":
		letterscore = 6
	elif char == "G":
		letterscore = 7
	elif char == "H":
		letterscore = 8
	elif char == "I":
		letterscore = 9
	elif char == "J":
		letterscore = 10
	elif char == "K":
		letterscore = 11
	elif char == "L":
		letterscore = 12
	elif char == "M":
		letterscore = 13
	elif char == "N":
		letterscore = 14
	elif char == "O":
		letterscore = 15
	elif char == "P":
		letterscore = 16
	elif char == "Q":
		letterscore = 17
	elif char == "R":
		letterscore = 18
	elif char == "S":
		letterscore = 19
	elif char == "T":
		letterscore = 20
	elif char == "U":
		letterscore = 21
	elif char == "V":
		letterscore = 22
	elif char == "W":
		letterscore = 23
	elif char == "X":
		letterscore = 24
	elif char == "Y":
		letterscore = 25
	elif char == "Z":
		letterscore = 26
	else:
		break
		
	return letterscore

	
def allletterscore(char):
	letterscore = 0

	if char == "A" or char == "a":
		letterscore = 1
	elif char == "B" or char == "b":
		letterscore = 2
	elif char == "C" or char == "c":
		letterscore = 3
	elif char == "D" or or char == "d":
		letterscore = 4
	elif char == "E" or char == "e":
		letterscore = 5
	elif char == "F" or char == "f":
		letterscore = 6
	elif char == "G" or char == "g":
		letterscore = 7
	elif char == "H" or char == "h":
		letterscore = 8
	elif char == "I" or char == "i":
		letterscore = 9
	elif char == "J" or char == "j":
		letterscore = 10
	elif char == "K" or char == "k":
		letterscore = 11
	elif char == "L" or char == "l":
		letterscore = 12
	elif char == "M" or char == "m":
		letterscore = 13
	elif char == "N" or char == "n":
		letterscore = 14
	elif char == "O" or char == "o":
		letterscore = 15
	elif char == "P" or char == "p":
		letterscore = 16
	elif char == "Q" or char == "q":
		letterscore = 17
	elif char == "R" or char == "r":
		letterscore = 18
	elif char == "S" or char == "s":
		letterscore = 19
	elif char == "T" or char == "t":
		letterscore = 20
	elif char == "U" or char == "u":
		letterscore = 21
	elif char == "V" or char == "v":
		letterscore = 22
	elif char == "W" or char == "w":
		letterscore = 23
	elif char == "X" or char == "x":
		letterscore = 24
	elif char == "Y" or char == "y":
		letterscore = 25
	elif char == "Z" or char == "z":
		letterscore = 26
	else:
		break

	return letterscore
	
def scrabblescore(char):
	
	# A, E, I, O, U, L, N, R, S, T	=  1
	# D, G	= 2
	# B, C, M, P = 3
	# F, H, V, W, Y	 = 4
	# K	 = 5
	# J, X = 8
	# Q, Z = 10
	
	letterscore = 0
	
	if char = "A" or char = "E" or char = "I" or char = "O" or char = "U" or char = "L" or char = "N" or char = "R" or char = "S" or char = "T":
		letterscore = 1
	elif char = "D" or char = "G":
		letterscore = 2
	elif char = "B" or char = "C" or char = "M" or or char = "P":
		letterscore = 3
	elif char = "F" or char = "H" or char = "V" or char = "W" or char = "Y":
		letterscore = 4
	elif char = "K":
		letterscore = 5
	elif char = "J" or char = "X":
		letterscore = 8
	elif char = "Q" or char = "Z":
		letterscore = 10
	else:
		break
	
	return letterscore