import unittest
import game

class TestGame(unittest.TestCase):

	def test_printSelection(self):
		result=game.printSelection("rock","rock")
		self.assertEqual(result, "\nYou chose rock, computer chose rock.\n")

	def test_winnerDeclaration_PlayerWon(self):
		result=game.winnerDeclaration(3,1,3)
		self.assertEqual(result,"Congratualions you won against computer\n")

	def test_winnerDeclaration_ComputerWOn(self):
		result=game.winnerDeclaration(1,2,2)
		self.assertEqual(result,"Sorry! You lost against computer! Better luck next time\n")

	def test_gameAfterInput_tie_Rock(self):
		result=game.gameAfterInput("rock","rock",0,0)
		self.assertEqual(result,(0,0))

	def test_gameAfterInput_tie_scissors(self):
		result=game.gameAfterInput("scissors","scissors",3,0)
		self.assertEqual(result,(3,0))

	def test_gameAfterInput_tie_paper(self):
		result=game.gameAfterInput("paper","paper",2,3)
		self.assertEqual(result,(2,3))

	def test_gameAfterInput_playerWinPointByScissors(self):
		result=game.gameAfterInput("scissors","paper",2,3)
		self.assertEqual(result,(3,3))

	def test_gameAfterInput_playerWinPointByPaper(self):
		result=game.gameAfterInput("paper","rock",1,3)
		self.assertEqual(result,(2,3))

	def test_gameAfterInput_playerWinPointByRock(self):
		result=game.gameAfterInput("rock","scissors",2,0)
		self.assertEqual(result,(3,0))

	def test_gameAfterInput_CompWinPointByPaper(self):
		result=game.gameAfterInput("rock","paper",1,3)
		self.assertEqual(result,(1,4))

	def test_gameAfterInput_CompWinPointByRock(self):
		result=game.gameAfterInput("scissors","rock",2,1)
		self.assertEqual(result,(2,2))

	def test_gameAfterInput_CompWinPointByScissors(self):
		result=game.gameAfterInput("paper","scissors",2,5)
		self.assertEqual(result,(2,6))


if __name__ == '__main__':
	unittest.main()