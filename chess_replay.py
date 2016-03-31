


class Player:
	def __init__(self,name,color):
		self.name = name
		self.color = color
		
	def __str__(self):
		return "{n} playing {c}".format(n=self.name,c = self.color)
		
	

class Piece:
	def __init__(self,color,ptype):
		self.color = color
		self.ptype = ptype
		self.pos = None
		

class Piece:
  def __init__(self,color,ptype,pos):
	self.ptype = ptype
	self.color = color
	self.pos = pos

  def __str__(self):
	string = ""
	if self.color == "white":
		string += "W"
	else:
		string += "B"
	if self.ptype == "pawn":
		string += "x"
	elif self.ptype == 'knight':
		string += 'N'
	else:
		string += self.ptype[0].upper()
	return string


class Board:
  def __init__(self):
	#init board
	self.b = [[None for i in range(8)] for j in range(8)]
	self.plyrs = ["P1","P2"]
	self.init_game()
	self.to_move = "P1"

  def __getitem__(self,key):
	key = key.lower()
	if key[0] > 'h' or key[0] < 'a':
		raise ValueError("invalid File: {file}".format(file=key[0]))
	elif key[1] < '1' or key[1] > '8':
		raise ValueError("invalid Rank: {rank}".format(rank=key[1]))
	i = ord(key[0]) - 97
	j = ord(key[1]) - 49
	return self.b[j][i]

  def __setitem__(self,key,piece):
	key = key.lower()
	if key[0] > 'h' or key[0] < 'a':
		raise ValueError("invalid File: {file}".format(file=key[0]))
	elif key[1] < '1' or key[1] > '8':
		raise ValueError("invalid Rank: {rank}".format(rank=key[1]))
	#elif piece is not type(Piece):
		#raise ValueError("Object {obj} not a type of Piece".format(obj = str(piece)) )
	i = ord(key[0]) - 97
	j = ord(key[1]) - 49
	self.b[j][i] = piece
	
	
  def init_game(self):
	k = Piece('white','king','e1')
	self['e1']  = k
	k = Piece('black','king','e8')
	self['e8'] = k

	self['d1'] = Piece('white','queen','d1')
	
	self['c1'] = Piece('white','bishop','c1')
	self['f1'] = Piece('white','bishop','f1')

	
	self['g1'] = Piece('white','knight','g1')
	self['b1'] = Piece('white','knight','b1')
 
	self['a1'] = Piece('white','rook','a1')
	self['h1'] = Piece('white','rook','h1')

	for i in 'abcdefgh':
		self[i+'2'] = Piece('white','pawn',i+'2')
	
	
	self['d8'] = Piece('black','queen','d8')

	self['c8'] = Piece('black','bishop','c8')
	self['f8'] = Piece('black','bishop','f8')

	
	self['g8'] = Piece('black','knight','g8')
	self['b8'] = Piece('black','knight','b8')

	
	self['a8'] = Piece('black','rook','a8')
	self['h8'] = Piece('black','rook','h8')

	for i in 'abcdefgh':
		self[i+'7'] = Piece('black','pawn',i+'7')
		
		
  def print_board(self):
		vborder = "*"*27
		board = " "+vborder+"\n *"
		for i in reversed(range(8)):
			string = str(i)+"|"
			for j in range(8):
				p = self.b[i][j]
				if p is None:
					string += "__|"
				else:
					string += str(p) + "|"
			board += string + "\n *"
		board += vborder	
		return board
		
  def move(self,piece,destination):
		curr_pos = piece.pos
		self[curr_pos] = None
		self[destination] = piece	
			
  def __str__(self):
		return self.print_board()
		
obj = Board()
print obj
pawn = obj['e2']
obj.move(pawn,'e4')
print obj
		



	 