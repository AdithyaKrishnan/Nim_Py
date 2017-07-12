#Acknowledgment : Wikipedia, My Ever Supportive Friends and Ullas Sir!

from random import randint
import sys
from functools import reduce


def NIM():
	pile = [randint(1, 50), randint(1, 50), randint(1, 50)]  #Random Number Generation is limited to 50 for simplicity.
	print("Welcome to NIM! The coin Piles are : {}" .format(pile))
	pileCollection = [x is not 0 for x in pile]
	while any(pileCollection):
		temp = [x is not 0 for x in pile]
		choice = int(input("Do you wish to pick coin(s) from pile 1 or 2 or 3? "))
		pickCoins = int(input("Enter the number of coin(s) to pick:"))
		if choice < 4:
			if pickCoins <= pile[choice - 1]:
				pile[choice-1] -= pickCoins
			else:
				print("Invalid Input! Please retry!")
				sys.exit(0)
			print("You have taken {} from pile {}" .format(pickCoins, choice))
			print("The pile now contains {}" .format(pile))			
			if all([x is 0 for x in pile]):
				print("Congratulations!!! you won!")
				sys.exit(0)
			else:
				ComputersTurn(pile)		
			print("Computer has made its move. Next is your turn")
			print("The Pile now contains {}" .format(pile))
			pileCollection = [x is not 0 for x in pile]
		else:
			print("Invalid Input. Please Retry!")
			sys.exit(0)
	print("Sorry!!You Lost! Better luck next time!!")
	sys.exit(0)

def ComputersTurn(pile):
	sum = reduce(lambda x,y: x^y, pile)
	if sum is 0 and any([x is not 0 for x in pile]):
		index = randint(0, 2)
		if pile[index] > 1:
			pile[index] -= randint(1, pile[index])
		else:
			index = randint(0, 2)
			pile[index] -= 1
	else:
		index, removeNumber = TurnDetail(pile, sum)
		pile[index] = pile[index] - removeNumber

def TurnDetail(pile, sum):
	sumpile = [x^sum for x in pile]	
	for x in range(0, 3):
		if sumpile[x] < pile[x]:
			return (x, pile[x] - sumpile[x])

NIM()
