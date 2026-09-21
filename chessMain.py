'''
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
'''


import pygame as p
import chessEngine

WIDTH = HEIGHT = 512    # 400 is good too

DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15

IMAGES = {}

'''
Initialize a global diretionary of images. This will be called exactly once in main.
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale (p.image.load("images/"+ piece + '.png'), (SQ_SIZE, SQ_SIZE))

'''
This will be our main driver. This will handle user input and updating the graphics.
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = chessEngine.GameState()
    loadImages() # only do this once , before the while loop

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)

        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics within a current game
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


'''
Draw the squares on the board. Top left square is always white.
'''
def drawBoard(screen):
    colors = [p.image.load("images/square brown light_png_128px.png"), p.image.load("images/square brown dark_png_128px.png")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            screen.blit(color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the boad using the current GameState.board.
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()