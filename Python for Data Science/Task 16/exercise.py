# =========================
# Overview
# =========================

####################################################################################
# ========================
# Part 1: Vector and Complex Numbers
# ========================

# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================
import math
# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.
'''
I read up on Vectors to understand the concept.
Reference #1: https://towardsdatascience.com/introduction-to-vectors-and-matrices-using-python-for-data-science-e836e014eb12
Reference #2: http://hplgit.github.io/primer.html/doc/pub/class/._class-solarized004.html - for implementing the Vector class
'''
# 1. Vector class as a template to create objects
class Vector(object):    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%f,%f)' % (self.x,self.y)
    '''
    __str__ method invoked when needing to display/use print command
    (%f,%f) used to format floating decimal point string output
    Reference: https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
    '''

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    '''
    Vector addition
    Adds the values of the 2 x-coordinates and the 2 y-coordinates
    '''
        
    def __sub__(self,other):
        return Vector(self.x - other.x,self.y - other.y )
    '''
    Vector subtraction
    Subtracts the arguent passed from the values x and y 
    '''
    
    def __mul__(self,other):
        return Vector(self.x * other.x + self.y * other.y)
    '''
    Scalar multiplication
    mul method gives the product of the 2 x-co-ordinates added to product of 2 y-co-ordinates
    '''
        
    def __abs__(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    '''
    Length    
    In this case, I used the distance formula to derive the answer, i.e. to get square root of the distance 
    between the difference of 2 x and y co-ordinates squared
    '''
        
    def __cmp__(self,other):
        return Vector(self.x == other.x and self.y == other.y)
    '''
    eq method compares two objects (vectors) by their values
    Reference: https://www.pythontutorial.net/python-oop/python-__eq__/#:~:text=Python%20automatically%20calls%20the%20__,the%20__eq__%20method.
    '''
import numpy as np
'''
Reference: https://www.w3schools.com/python/numpy/default.asp
'''
# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.

# 1. MyComplex class as a template to create objects
class MyComplex(Vector):
    def __init__(self,complex1,complex2,complex_no):
        self.complex1 = complex1
        self.complex2 = complex2
        self.complex_no = complex_no
    
    def multiply(self,complex1,complex2):
        return complex1.mul(complex2)  
    '''
    Seeing as MyComplex class inherits from Vector class, called the mul method 
    to do multply calculation
    '''
        
    def conjugate(self,complex_no):
        return np.conj(complex_no)
    '''
    Used numpy function conj to return the conjugate of a complex number
    Reference: https://www.geeksforgeeks.org/numpy-conj-in-python/#:~:text=The%20numpy.,its%20conjugate%20is%202%2D5j.
    '''
    
    def __str__(self):
        return 'The product of two complex numbers is: ' + str(self.multiply(complex1,complex2)) + '\t' + 'The complex conjugate would be: ' + str(conjugate(complex_no))
    '''
    New string method produces output
    '''
####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and overcomplication.

# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

# 1. Piece class as a template to create board object
class Piece(object):
    '''
        Initialised the display board before the first game has started
    '''    
    def __init__(self,board):        
        self.board = board
    '''
        This adds "-" pieces to the board
    '''    
    def add_board(self,board):
        self.board.append(board)       
    
# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:
'''
    Both X and O classes inherit from the Piece class
    The logic for both classes is the same. So I'll only comment once.
'''
class X(Piece):
    '''
        Inherit the super class constructor
    '''
    def __init__(self,board,position,piece,current_player):
        super(X,self).__init__(board)
        self.position = position
        self.piece = "X"
        self.current_player = False 
    '''
        When this method is called, it signals that it is player X's turn
    '''
    def mark_current_player(self):
        self.current_player = True
        return
    '''
        When this method is called, it signals that it is not player X's turn
    '''
    def mark_next_player(self):
        self.current_player = False
        return
    '''
        This adds a player's piece to the board
    '''
    def add_to_board(self, position, piece):         
        self.board[position] = self.piece
        return    
    '''
        This checks to see that an applicable square or tile has been occupied on the board or not
    '''
    def check_marked(self,position):
        if self.board[position] == "-":
            return False
        else:
            return True
    '''
        When this method is called, it adds X to a position on the board provided there tile is open
        It also calls the mark_next_player method to set X's turn off
    '''
    def add_piece(self):
        while self.current_player:
            position = int(input("Player " + self.piece + ": Choose a position from 1 to 9: "))
            while self.check_marked(position-1):
                position = int(input("This space has been taken. Choose another position from 1 to 9: "))
            self.add_to_board(position-1,self.piece)
            self.mark_next_player()
        return

class O(Piece):

    def __init__(self,board,position,piece,current_player):
        super(O,self).__init__(board)
        self.position = position
        self.piece = "O"
        self.current_player = False    

    def mark_current_player(self):
        self.current_player = True
        return

    def mark_next_player(self):
        self.current_player = False
        return
    
    def add_to_board(self, position, piece):         
        self.board[position] = self.piece
        return
        
    def check_marked(self,position):
        if self.board[position] == "-":
            return False
        else:
            return True         
    
    def add_piece(self):
        while self.current_player:
            position = int(input("Player " + self.piece + ": Choose a position from 1 to 9: "))    
            while self.check_marked(position-1):
                position = int(input("This space has been taken. Choose another position from 1 to 9: "))        
            self.add_to_board(position-1,self.piece)
            self.mark_next_player()
        return    

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

class TicTacToeBoard(object):
    '''
        Constructor class
    '''
    def __init__(self,board,player1,player2,game_active):
        self.board = board
        self.player_one = player1
        self.player_two = player2
        self.game_active = False    

    '''
        This resets the board for another game
    '''
    def reset_board(self):
        return self.board == ["-","-","-",
                              "-","-","-",
                              "-","-","-"]    
    '''
        start_game method sets the properties for the beginning of the Tic-Tac-Toe game
        Each player in turn becomes an object of the TicTacToeBoard class
    '''
    def start_game(self):
        self.game_active = True        
        if self.player_one == "X":
            self.player_one = X(self.board,-1,"X",True)
            self.player_two = O(self.board,-1,"O",False)
        elif self.player_one == "O":
            self.player_one = O(self.board,-1,"O",True)
            self.player_two = X(self.board,-1,"X",False)
        return

    '''
        display_current_board method shows the current state of the board after each player move
    '''
    def display_current_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])
    
    '''
        add_current_board method adds the pieces for each player and switches turns
    '''
    def add_current_board(self):
        if self.player_one.current_player:            
            self.player_one.add_piece()
            self.player_two.mark_current_player()
            self.display_current_board()
        else:
            self.player_two.add_piece()
            self.player_one.mark_current_player()
            self.display_current_board()

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

piece = Piece([])

for b in board:
    piece.add_board(b)

player_choice = input("Choose X or O: ")
if player_choice.lower() == "x":
    player1 = "X"
    player2 = "O"    
elif player_choice.lower() == "o":
    player1 = "O"
    player2 = "X"

tictactoe = TicTacToeBoard(piece.board,player1,player2,False)    
tictactoe.start_game()

winning_combo = ""

'''
    check_row function checks to see whether any of the rows on the board match
    When such occurs, it returns the first piece on the board which corresponds
    with the rest of the row
    Reference: https://www.youtube.com/watch?v=BHh654_7Cmw
'''
def check_row():
    first_row = tictactoe.board[0] == tictactoe.board[1] == tictactoe.board[2] != "-"
    second_row = tictactoe.board[3] == tictactoe.board[4] == tictactoe.board[5] != "-"
    third_row = tictactoe.board[6] == tictactoe.board[7] == tictactoe.board[8] != "-"
        
    if first_row or second_row or third_row:
        tictactoe.game_active = False

    if first_row:
        return tictactoe.board[0]
    elif second_row:
        return tictactoe.board[3]
    elif third_row:
        return tictactoe.board[6]
    return
'''
    check_column function checks to see whether any of the columns on the board match
    When such occurs, it returns the first piece on the board which corresponds
    with the rest of the column
    Reference: https://www.youtube.com/watch?v=BHh654_7Cmw
'''        
def check_column():
    first_column = tictactoe.board[0] == tictactoe.board[3] == tictactoe.board[6] != "-"
    second_column = tictactoe.board[1] == tictactoe.board[4] == tictactoe.board[7] != "-"
    third_column = tictactoe.board[2] == tictactoe.board[5] == tictactoe.board[8] != "-"
        
    if first_column or second_column or third_column:
        tictactoe.game_active = False

    if first_column:
        return tictactoe.board[0]
    elif second_column:
        return tictactoe.board[1]
    elif third_column:
        return tictactoe.board[2]
    return
    
'''
    check_diag function checks to see whether any of the diagonals on the board match
    When such occurs, it returns the first piece on the board which corresponds
    with the rest of the pieces on the diagonal
    Reference: https://www.youtube.com/watch?v=BHh654_7Cmw
''' 
def check_diag():
    first_diag = tictactoe.board[0] == tictactoe.board[4] == tictactoe.board[8] != "-"
    second_diag = tictactoe.board[2] == tictactoe.board[4] == tictactoe.board[6] != "-"

    if first_diag or second_diag:
        tictactoe.game_active = False
        
    if first_diag:
        return tictactoe.board[0]
    elif second_diag:
        return tictactoe.board[2]
    return
'''
    check_win function checks to see whether the game has been won by player X or player Y.
    It checks to see whether any of the rows, columns, or diagonals have been matched
    If so, it determines the winner
    Reference: https://www.youtube.com/watch?v=BHh654_7Cmw
''' 
def check_win():
    global winning_combo    
    
    row_winner = check_row()
    column_winner = check_column()
    diag_winner = check_diag()

    if row_winner:
        winning_combo = row_winner
    elif column_winner:
        winning_combo = column_winner
    elif diag_winner:
        winning_combo = diag_winner

    if winning_combo == player1:
        print(player1 + " has won this game! Congrats.")
    elif winning_combo == player2:
        print(player2 + " has won this game! Congrats.")
    return
    
'''
    check_diag function checks to see whether the game is drawn or not.
    Game would be drawn if all pieces have been used with no matching rows/columns/diagonals
    Reference: https://www.youtube.com/watch?v=BHh654_7Cmw
''' 
def check_draw():
    if "-" not in tictactoe.board:
        tictactoe.game_active = False
        print("Game has been drawn!")
    return
       
'''
    While the game is still active, all the pieces on the board have not yet been occupied by either player
    After each turn, the game checks to see if there is a winner or not
'''

while tictactoe.game_active:
    check_win()
    check_draw()
    if not check_win() or check_draw():
        tictactoe.add_current_board()   
tictactoe.reset_board()   
        
