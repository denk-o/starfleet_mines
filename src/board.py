from mine import mine
from spaceship import spaceship
import math

class board:
    def __init__(self, start_board):
        self.starting_board = start_board
        self.mines = self.buildMinesArray()
        self.num_mines = len(self.mines)
        self.ship_start_position = self.getShipPosition()
        self.current_board = board
        self.ship = spaceship()
        self.MOVES = ['north', 'south', 'east', 'west']
        self.PATTERNS = ['alpha', 'beta', 'gamma', 'delta']
        self.ship_position = self.getShipPosition()
    def buildMinesArray(self):
        board = self.starting_board
        board_y_size = len(self.starting_board)
        board_x_size = len(self.starting_board[0])
        mines = []
        #assume square input matricies so we don't need two inputs
        #at a later point we can add a helper function to clean our inputs
        #so every input matrix can be set to be square
        midpoint = math.floor(board_x_size/2)
        #mine coordinates should be centered around ship
        for row in range(board_y_size):
            for col in range(board_x_size):
                #convert from array indicies into cartesian coordinates
                #check if value is a mine
                val = self.starting_board[row][col]
                if val != '.':
                    x_coordinate = col - midpoint
                    y_coordinate = midpoint - row
                    mines.append(mine(x_coordinate, y_coordinate, val))
        return mines
    def getShipPosition(self):
        pos_x = 0
        pos_y = 0
        #TODO: decide whether to center ship at center of array or 0 center it
        #lets just return the midpoint of the array for now we can adjsut in other methods

        return {'x': pos_x, 'y': pos_y}
    def printBoard(self):
        board = self.current_board
        for row in range(len(board)):
            for col in range(len(board[row])):
                print(board[row][col] + ' ')
            print('\n')
    def doStep(self, step):
        move = step.move if step.move in self.MOVES else None
        fire = step.fire if step.fire in self.PATTERNS else None
        if fire:
            self.ship.fire(fire)
            self.fire_torpedos(fire)
        if move:
            self.ship.move(move)
            self.move_ship(move)
    def fire_torpedos(self, pattern):
        #TODO: DEFINE HELPER FUNCTION AFTER DECIDING COORDINATE SYSTEM
        position = self.getShipPosition()
        x = position.x
        y = position.y
        if pattern == 'alpha':
            #do alpha
            print('alpha')
        elif pattern == "beta":
            #do beta
            print('beta')
        elif pattern == "gamma":
            #do gamma
            print('gamma')
        elif pattern == "delta":
            #do delta
            print('delta')
        else:
            #do nothing
            print('end')
    def move_ship(self, move):
        #TODO: DEFINE HELPER FUNCTION AFTER DECIDING COORDINATE SYSTEM
        position = self.getShipPosition()
        x = position.x
        y = position.y
        if move == 'north':
            print('north')
        elif move == 'south':
            print('south')
        elif move == 'east':
            print('east')
        elif move == 'west':
            print('west')
        else:
            print('end')
        self.center_board()
