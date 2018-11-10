from mine import mine
from spaceship import spaceship
from board import board
import utils

field_file = utils.getFile('field_file.txt')
script_file = utils.getFile('script_file.txt')
input_board = []
for line in field_file:
    input_board.append(list(line))

my_board = board(input_board)

print('Starting Board')
my_board.printBoard()
