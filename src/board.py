from mine import mine
from spaceship import spaceship
import math

class board:
    def __init__(self, start_board):
        self.starting_board = start_board
        self.mines = self.buildMinesArray()
        self.num_mines = len(self.mines)
        self.ship = spaceship()
        self.ship_start_position = self.getShipPosition()
        self.current_board = start_board
        self.MOVES = ['north', 'south', 'east', 'west']
        self.PATTERNS = ['alpha', 'beta', 'gamma', 'delta']
        self.ship_position = self.getShipPosition()
        self.move_count = 0
        self.fire_count = 0
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
        #delegate ship positioning to ship object
        pos_x = self.ship.x
        pos_y = self.ship.y
        return {'x': pos_x, 'y': pos_y}
    def printBoard(self):
        board = self.current_board
        for row in range(len(board)):
            for col in range(len(board[row])):
                print(board[row][col], end='')
    def doStep(self, step):
        #we should be able to manage our inputs better for now these if statements are satsifactory
        fire = step[0] if step[0] in self.PATTERNS else False
        move = False
        if  not fire:
            move = step[0] if step[0] in self.MOVES else False
        elif len(step) == 2:
            move = step[1] if step[1] in self.MOVES else False
        if fire:
            self.fire_torpedos(fire)
        if move:
            self.move_ship(move)
    def fire_torpedos(self, pattern):
        #TODO: DEFINE HELPER FUNCTION AFTER DECIDING COORDINATE SYSTEM
        position = self.getShipPosition()
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
        position = self.getShipPosition()

        if move == 'north':
            self.ship.north()
            move_count = self.ship.increment_moves()
            print('north')
        elif move == 'south':
            self.ship.south()
            move_count = self.ship.increment_moves()
            print('south')
        elif move == 'east':
            self.ship.east()
            mvoe_count = self.ship.increment_moves()
            print('east')
        elif move == 'west':
            self.ship.west()
            move_count = self.ship.increment_moves()
            print('west')
        else:
            print('NONE')
