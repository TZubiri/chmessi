class Player:
	def make_move(board,move):
		pass

class Board:
	def setup(Board):
		pass

class Arbiter:
	def is_legal(board,move,log) -> bool:
		pass

class Log:
	pass

class Player:
	def log_move(move):
		self.moves.append(move)

class Rules:
	def initial_setup():
		pass
	def is_legal(board,move,log):
		pass
	def result(): #-> Enum("1-0","0-1","1/2-1/2","live")
		pass
