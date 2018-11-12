# Starfleet Mine Clearing Exercise Evaluator

The problem statement can be found [here](Problem.txt)

## Getting Started:
To run the program execute:
    `python3 main.py`
To alter the inputs, modify src/field_file.txt and src/script_file.txt
## Assumptions:
1. We can assume for simplicity of implementation that our input board will always have odd rows/columns
   - We may write a helper method to clean even row/col inputs
2. Assume the ship ALWAYS fires before moving if possible
3. Assume an N x N input board for simplicity of implementation
   - We may also clean this with a helper method
4. Ship coordinates begin in the center of the board at (0, 0) even though that is not the index of the array structured input
5. Once we miss a mine we break out of the routine and immediately fail the script
   - By doing this we omit the need to print asterisk (\*) characters


## Function Documentation:
### Board.py class:
<details>
  <summary>Constructor</summary>
   The constructor takes in an input start_board object which we create from a .txt file.
   The start_board object is a 2 d array

    ##### Intialized Variables
      - self.starting_board: Local storage of the starting board
      - self.mines: Given the starting board, we call the buildMinesArray() method to create a list of Mine objects
      - self.num_mines: A count of the mines list
      - self.ship: An object of type spaceship
      - self.ship_start_position: Simply a dict with (0,0) x-y coordinates we generate by calling getShipPosition()
      - self.current_board: We preserve board state here, initialized to a copy of starting_board
      - self.MOVES: A list of possible ship movements
      - self.PATTERNS: A list of possible firing patterns
      - self.ship_position: The ship's current position, initialized to getShipPosition() at (0,0)
      - self.z_position: The ship's depth in the cuboid, initialized to 0
      - self.move_count: The ship's movement count, initialized to 0
      - self.fire_count: The ship's fire count, initialized to 0      
</details>
<details>
  <summary>buildMinesArray()</summary>
  Builds the list of mines on the starting board, populates them with Mine objects to represent attributes of the mine
</details>
<details>
  <summary>getShipPosition()</summary>
  Returns the x, y coordinates of the ship
</details>
<details>
  <summary>printBoard()</summary>
  Prints the board as an ASCII representation
</details>
<details>
  <summary>doStep(step)</summary>
  Primary step action controller, given an input step list does the steps in the list
  Restricted by assumption 2
</details>
<details>
  <summary>doAlpha()</summary>
  Does firing pattern Alpha. The methods for Beta, Gamma, and Delta are nearly identical
</details>
<details>
  <summary>fire_torpedos(pattern)</summary>
  Implementation of the action of firing torpedos. Deprecates action to the proper firing pattern methods
</details>
<details>
  <summary>move_ship(move)</summary>
  Moves the position of the ship, deprecates movement to the ship's movement methods
</details>
<details>
  <summary>evalBoardState()</summary>
  Evaluates the board state and returns a PASS/FAIL string if those requirements are met
</details>
<details>
  <summary>updateBoard()</summary>
  Updates the visual representation of the board and associated board state
</details>

## Thought Process of Solution
## Afterthoughts/Post-Mortem
