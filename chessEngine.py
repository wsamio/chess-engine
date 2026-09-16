"""
This class is responsiwle for storing all of the information about the current state of a chess game.
It will also be responsible for determining the valid moves at the current state and 
it will contain a move log.
"""

class GameState():
    def __init__(self):

        # borad is a 8*8 2D list, each element of the list has 2 characters.
        # The first character represents the colour of the piece and the second one represents the type of the piece
        # The "--" represents an empty space on the board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["bR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]  
        ]
        
        self.whiteToMove = True
        self.moveLog = []


