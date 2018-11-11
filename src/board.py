from mine import mine
from spaceship import spaceship
import math


#TODO: it may be possible to refactor this into several smaller classes to reduce file size and code cleaner
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
        self.z_position = 0
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
                    mines.append(mine(x_coordinate, y_coordinate, val, row, col))
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
            # add ending whitespace to make cleaner output
            print('')
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
        self.z_position = self.z_position + 1
        self.updateBoard()
    def doAlpha(self, position):
        mines = self.mines
        x = position['x']
        y = position['y']

        for mine in mines:
            #if it's a dead mine go next
            if not mine.is_alive:
                continue
            if mine.x == (x-1) and mine.y == (y+1):
                mine.is_alive = False
            elif mine.x == (x+1) and mine.y == (y+1):
                mine.is_alive = False
            elif mine.x == (x-1) and mine.y == (y-1):
                mine.is_alive = False
            elif mine.x == (x+1) and mine.y == (y-1):
                mine.is_alive = False
        return mines
    def doBeta(self, position):
        mines = self.mines
        x = position['x']
        y = position['y']

        for mine in mines:
            #if it's a dead mine go next
            if not mine.is_alive:
                continue
            if mine.x == x and mine.y == (y+1):
                mine.is_alive = False
            elif mine.x == (x+1) and mine.y == y:
                mine.is_alive = False
            elif mine.x == (x-1) and mine.y == y:
                mine.is_alive = False
            elif mine.x == x and mine.y == (y-1):
                mine.is_alive = False
        return mines
    def doGamma(self, position):
        mines = self.mines
        x = position['x']
        y = position['y']

        for mine in mines:
            if not mine.is_alive:
                continue
            if mine.x == (x-1) and mine.y == y:
                mine.is_alive = False
            if mine.x == x and mine.y == y:
                mine.is_alive = False
            if mine.x == (x+1) and mine.y == y:
                mine.is_alive = False
        return mines
    def doDelta(self, position):
        mines = self.mines
        x = position['x']
        y = position['y']

        for mine in mines:
            if not mine.is_alive:
                continue
            if mine.x == x and mine.y == (y-1):
                mine.is_alive = False
            if mine.x == x and mine.y == y:
                mine.is_alive = False
            if mine.x == x and mine.y == (y+1):
                mine.is_alive = False
        return mines
    def fire_torpedos(self, pattern):
        #TODO: DEFINE HELPER FUNCTION AFTER DECIDING COORDINATE SYSTEM
        position = self.getShipPosition()
        mines = self.mines

        #we manage firing in board class because it alters board state more than ship state
        if pattern == 'alpha':
            #do alpha X pattern
            self.fire_count = self.ship.increment_shots()
            #brute force check mine placement. Can be optimized?
            self.mines = self.doAlpha(position)
            print('alpha')
        elif pattern == "beta":
            #do beta + pattern
            self.fire_count = self.ship.increment_shots()
            self.mines = self.doBeta(position)
            print('beta')
        elif pattern == "gamma":
            #do gamma - pattern
            self.fire_count = self.ship.increment_shots()
            self.mines = self.doGamma(position)
            print('gamma')
        elif pattern == "delta":
            #do delta | pattern
            self.fire_count = self.ship.increment_shots()
            self.mines = self.doDelta(position)
            print('delta')
        else:
            #do nothing
            print('NONE')
    def move_ship(self, move):
        position = self.getShipPosition()

        if move == 'north':
            self.ship.north()
            self.move_count = self.ship.increment_moves()
            print('north')
        elif move == 'south':
            self.ship.south()
            self.move_count = self.ship.increment_moves()
            print('south')
        elif move == 'east':
            self.ship.east()
            self.move_count = self.ship.increment_moves()
            print('east')
        elif move == 'west':
            self.ship.west()
            self.move_count = self.ship.increment_moves()
            print('west')
        else:
            print('NONE')
    def evalBoardState(self):
        mines = self.mines
        z_pos = self.z_position
        #check for missed mines
        for mine in mines:
            if not mine.is_alive:
                continue
            if mine.dist < z_pos:
                #we missed this mine and it is live
                return 'FAIL'
        #check if all mines dead
        live_mines = [m for m in mines if m.is_alive]
        if len(live_mines) == 0:
            return 'PASS'
        else:
            return True
    def updateBoard(self):
        #update the visual aspect of the board
        board = self.current_board
        mines = self.mines
        position = self.getShipPosition()
        x = position['x']
        y = position['y']
        max_x = 0
        max_y = 0
        for mine in mines:
            if mine.is_alive:
                #move the mines closer
                mine.dist = mine.dist - 1
                mine.convertToChar()

                #trim/grow the board
                #to do this we find the longest horizontal and vertical distance to a mine
                #double and add 1 to it to generate the distance
                max_x = max_x if max_x > abs(x-mine.x) else abs(x-mine.x)
                max_y = max_y if max_y > abs(y-mine.y) else abs(y-mine.y)

                #update mine coordinates
                row = mine.row if mine.row<len(board) else len(board)-1
                col = mine.col if mine.col<len(board[0]) else len(board[0])-1
                board[row][col] = mine.z_dist
        #generate a new board
        new_board = [['.' for i in range(2*max_x+1)] for j in range(2*max_y+1)]
        #populate mines in new board
        # for mine in mines:
        #     new_board[max_y - mine.y]
        self.current_board = new_board
        self.mines = mines
