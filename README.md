# Starfleet Mine Clearing Exercise Evaluator

The problem statement can be found [here](Problem.txt)

## Assumptions:
1. We can assume for simplicity of implementation that our input board will always have odd rows/columns
  - We may write a helper method to clean even row/col inputs
2. Assume the ship ALWAYS fires before moving if possible
3. Assume an N x N board for simplicity of implementation
  - We may also clean this with a helper method
4. Ship coordinates begin in the center of the board at (0, 0) even though that is not the index of the array structured input
5. Once we miss a mine we break out of the routine and immediately fail the script


## Function Documentation:
### Board.py class:
<details>
  <summary>Constructor</summary>
</details>
