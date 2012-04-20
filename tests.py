# testcases for 

from letterscore import *

wordlist = 

def letterscoretest(char):
	
	# letterscore.py contains 4 functions:
	# 1) capitalletterscore(char) : function that takes upper case A-Z characters and assigns A=1...Z=26 to them
	# 2) lowercaseletterscore(char) : function that takes lower case a-z characters and assigns a=1...z=26 to them
	# 3) allletterscore(char) : function that takes upper and lower case A-Z and a-z characters and assigns a=1,A=1...z=26,Z=26 to them
	# 4) scrabblescore(char) : function that takes upper case A-Z and assigns Scrabble tile scoring to them.
	
	# capitalletterscore(A) = 1
	
	# test1: single characters
	
	test1 = 0

	if capitalletterscore(A) == 1:
		test1 += 1
	if capitalletterscore(B) == 2:
		test1 += 1		
	if capitalletterscore(C) == 3:
		test1 += 1
	if capitalletterscore(D) == 4:
		test1 += 1
	if capitalletterscore(E) == 5:
		test1 += 1	
	if capitalletterscore(F) == 6:
		test1 += 1
	if capitalletterscore(G) == 7:
		test1 += 1
	if capitalletterscore(H) == 8:
		test1 += 1
	if capitalletterscore(I) == 9:
		test1 += 1
	if capitalletterscore(J) == 10:
		test1 += 1
	if capitalletterscore(K) == 11:
		test1 += 1
	if capitalletterscore(L) == 12:
		test1 += 1
	if capitalletterscore(M) == 13:
		test1 += 1
	if capitalletterscore(N) == 14:
		test1 += 1			
	if capitalletterscore(O) == 15:
		test1 += 1
	if capitalletterscore(P) == 16:
		test1 += 1
	if capitalletterscore(Q) == 17:
		test1 += 1
	if capitalletterscore(R) == 18:	
		test1 += 1
	if capitalletterscore(S) == 19:
		test1 += 1
	if capitalletterscore(T) == 20:	
		test1 += 1
	if capitalletterscore(U) == 21:
		test1 += 1					
	if capitalletterscore(V) == 22:
		test1 += 1
	if capitalletterscore(W) == 23:
		test1 += 1
	if capitalletterscore(X) == 24:
		test1 += 1
	if capitalletterscore(Y) == 25:
		test1 += 1
	if capitalletterscore(Z) == 26:
		test1 += 1
									
	if test1 == 26:
		print "Test 1: Passed"
	else:
		print "Test 1: Passed %d out of 26"
		