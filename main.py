class Player:
	def make_move(board,move:str):
		pass

class Board:
	def setup(self):
		pass

class Arbiter:
	def is_legal(board:Board,move:str,log) -> bool:
		pass

class Log:
	pass

class Player:
	def log_move(move:str):
		self.moves.append(move)

class Rules:
	def initial_setup():
		pass
	def is_legal(board:Board,move:str,log:Log):
		pass
	def result(): #-> Enum("1-0","0-1","1/2-1/2","live")
		pass

class AI:
	def legal_moves(board:Board,log)->[str]:
		...
