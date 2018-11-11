from mine import mine
from spaceship import spaceship
from board import board
import utils

field_file = utils.getFile('field_file.txt')
script_file = utils.getFile('script_file.txt')
input_board = []
for line in field_file:
    input_board.append(list(line.rstrip('\n')))
steps = []
for line in script_file:
    steps.append(line.rstrip('\n').split(' '))
my_board = board(input_board)

print('-------------')
print('Starting Script')
print('-------------')
step_count = 0
for step in steps:
    print('step', step)
    my_board.printBoard()
    my_board.doStep(step)
    res = my_board.evalBoardState()

    print('Ship is at (', my_board.getShipPosition()['x'],', ',my_board.getShipPosition()['y'],')')
    print('+++++++++')
    step_count = step_count+1
    if res == "FAIL" or res == "PASS":
        #if res is not a string result we must stop the steps and go to the next
        print(res)
        break
#after breaking loop we must eval the score if it's a pass
score = 0
if res == "PASS":
    if len(steps) - step_count != 0:
        score = 1
    else:
        #10 times the initial number of mines in the cuboid
        score = (10*my_board.num_mines)
        #-5 points for every shot fired but no more than 5x initial mines
        shots_fired_diff = my_board.fire_count*5 if my_board.fire_count*5 <= my_board.num_mines*5 else my_board.num_mines*5
        #-2 points for every km moved but no more than 3x initial mines
        moves_executed_diff = my_board.move_count*2 if my_board.move_count*2 <= my_board.num_mines*3 else my_board.num_mines*3
        score = score - shots_fired_diff - moves_executed_diff
print('Score is:', score)
