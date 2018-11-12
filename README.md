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

   Intialized Variables
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
  <summary>doAlpha(), doBeta(), doGamma(), doDelta()</summary>
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

### spaceship.py class:
<details>
  <summary>Constructor</summary>
  Creates a spaceship object, tracking it's x-y position and the number of moves executed and shots fired
</details>
<details>
  <summary>increment_moves()</summary>
  Increment the moves_executed attribute
</details>
<details>
  <summary>increment_shots()</summary>
  Increment the shots_fired attribute
</details>
<details>
  <summary>north(), south(), east(), west()</summary>
  Increment the x-y positions of the ship in accordance with the correct N/S/E/W function
</details>

### mine.py class:
<details>
  <summary>Constructor</summary>
  Initialize the x, y coordinates of the mine and its 'depth' in the cuboid
  Also initialize the mine's live/dead state and helper variables for calculations
</details>
<details>
  <summary>convertToDist()</summary>
  Convert a character input value into a numeric distance based on ASCII code
</details>
<details>
  <summary>convertToChar()</summary>
  Reverse conversion used to calculate mine updated distance and build a character
</details>

## Thought Process of Solution
On initial inspection of the problem statement, it was clear that at some level, this was an array manipulation problem where the data would be represented as a 2D array. However, it then occurred to me to see if it would be possible to limit usage of the array data structure purely to display and then to represent the state of the cuboid by only the position of the mines and the position of the ship. It is in this way that I decided to implement the majority of the codebase.

The board class contains the majority of the code to represent functionality in the project. This is because the board controls almost all of the state necessary for functionality. It also contains a series of mine objects and a single spaceship object. State associated with these objects was then delegated to them. EX: Mine live/dead state.

Intuitively, the initial design required a class for board, ship and mine. I also included a utils library for any helper functions that I would see the need for.

Once I had a general idea of how the logic flow of the main execution loop would behave, I set about implementing the methods to do every step. I decided that rather than centering the ship at its position in the matrix (math.floor(len(board))/2) I would center the board at its x-y coordinate, (0,0). In this way we make movement calculations more intuitive as they become simple increments and decrements.

Once the coordinate system was properly converted, the necessary commands were then implemented. Firing the ship and movement were originally both located in the board object but when I thought about it, I figured the firing would be a board responsibility and the movement would be a ship responsibility. This is because the former is more related to the state of the board, mines being dead/alive, while the latter is more related to ship state, its position in the coordinate plane.

Next to be implemented was the checker for PASS/FAIL state and how I wanted to handle the logic for arriving at that state and the scoring. I delegated the point scoring to the main execution context.

Finally, to update the board we had to expand/contract the board so that it only showed the necessary area. This was an interesting problem where I had to puzzle out the best way to avoid overflowing the length of the list as it got shorter.
## Justification of Technologies Used
There were only a couple significant pieces used here:

First and foremost the programming language I chose to implement this in was python3.
Python allows for rapid prototyping and as such, required minimal setup. Intuitively, when designing the project, it clicked more for me in python as well.

Secondly I employed a Vagrant virtualbox to ssh into an Ubuntu environment rather than running my code on my local Windows machine.
This is reflected in the Vagrantfile configuration file located in the repository.
## Afterthoughts/Post-Mortem
The code I wrote has some definite inefficiencies that I observed while implementing and during the write up of this information. Some notes as follows:

    - A lot of redundant variables and object attributes were created that I could definitely slim down upon refactoring.
    - There is probably a better way to handle the commands that are given instead of writing 8 different functions. However, the brute force method seems the most straightforward.
    - I did notice that my board.py file got extremely large and I strongly believe there should be a way to slim down all the code in there.
    - One significant thing I noted was that were it not necessary to print the array after every step, this entire script could be done without needing that data structure as we would only need the positions of the mines and their distances to properly compute the success/failure of the script given input.
    - I had difficulty deciding how I wanted to represent the location of the ship on the coordinate plane: As an x-y pair or as its location in the board matrix. In the end I feel as though I made the correct decision selecting the former. This particular piece took up a significant portion of my time as I weighed its justifications.
    - Once again I am reminded the importance of properly reading a problem. My initial few readthroughs left me baffled as to how to construct a solution, but upon stricter examination it became clear that the implementation would be relatively straightforward.
    - I did not remove mines from the list of mines, rather I set their boolean alive state to False. I wonder if it would be more effective to simply remove the mines from the array as it would make iteration through the list simpler. I wasn't confident I could find a solution I would be OK with for mines that are missed if I were to do so though.
    - I strongly disagree with some of the criteria regarding representing missed mines with a \*. I feel like, and I did implement my script representing this, a FAIL/PASS should be given at the most immediate possible time to avoid slowdown at scale.
    - There were quite a few restrictions that I placed on inputs. Such as Assumptions 1 and 3. I did this to create a simpler implementation. I figure, in the future it is relatively trivial to implement some sort of method to clean inputs so they are properly read in.
    - I found it remarkably helpful to plan out my prototyping in a notebook before actually going to the keyboard. It definitely helped me to write everything out before diving in and implementing.
    - As a follow up, writing up my thoughts is easier when I have that scrawled on paper as little notes.
