# Solving Sudoku Puzzle Game
Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game. If you play Sudoku daily, you will soon start to see improvements in your concentration and overall brain power.

In this project, I'll apply some AI algorithms to solve Sudoku game.

# How to play a Sudoku Game
The goal of Sudoku is to fill in a 9×9 grid with digits so that each column, row, and 3×3 section contain the numbers between 1 to 9. At the beginning of the game, the 9×9 grid will have some of the squares filled in. Your job is to use logic to fill in the missing digits and complete the grid. Don’t forget, a move is incorrect if:

- Any row contains more than one of the same number from 1 to 9
- Any column contains more than one of the same number from 1 to 9
- Any 3×3 grid contains more than one of the same number from 1 to 9

# Install
- You'll need **Python 3.5** to run the code
- You will need [pygame](https://www.pygame.org/) to visualize the game board
- Install all of the require packages
```
pip install -r requirements.txt
```

# How to use the code
- You must have a 9x9 grid of a sudoku game to solve, encode as a string with the length of 81.
```
grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
```
- A number [1->9] represent the box value. A dot (`.`) represent the unsolve box.
- Import code from `solution.py`
```
from solution import solve
from utils import display

result = solve(grid)
display(result)

2 6 7 |9 4 5 |3 8 1
8 5 3 |7 1 6 |2 4 9
4 9 1 |8 2 3 |5 7 6
------+------+------
5 7 6 |4 3 8 |1 9 2
3 8 4 |1 9 2 |6 5 7
1 2 9 |6 5 7 |4 3 8
------+------+------
6 4 2 |3 7 9 |8 1 5
9 3 5 |2 8 1 |7 6 4
7 1 8 |5 6 4 |9 2 3
```
# Demo
```javascript
python solution.py
```