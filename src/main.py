from mine import mine
from spaceship import spaceship
from board import board
import utils

field_file = utils.getFile('field_file.txt')
script_file = utils.getFile('script_file.txt')
input_board = []
for line in field_file:
    input_board.append(list(line))
steps = []
for line in script_file:
    steps.append(line.rstrip('\n').split(' '))
my_board = board(input_board)

print('Starting Board')
my_board.printBoard()
print('-------------')
print('Starting Script')
print('-------------')
for step in steps:
    print('step', step)
    my_board.doStep(step)
    my_board.printBoard()
    print('Ship is at (', my_board.getShipPosition()['x'],', ',my_board.getShipPosition()['y'],')')
    print('+++++++++')
    # my_board.evalBoardState()
