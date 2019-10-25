# GAME OF LIFE
Game Of Life algorithm visualization

**CODE EXPLANATION**

Import necessary modules:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
```
Define board and cell objects
- Board counts number of generations with "num_gen" class variable
- Cell stores number of living cells in each generation with "cellPer_i class" variable
```python
class board
    num_gen = 0
class cell
    cellPer_i = dict()
```
1. Board class:
Each board initializes itself with a previously randomly created temporal board
   - current_genBoard: board containing current generation cells (one to be ranged)
   - next_genBoard: board containing next generation cells (reproduction changes stored here)
```python
def __init__(self, max_N):
    temp_board = np.random.randint(2, size = (max_N, max_N))
    temp_board = np.pad(temp_board, 1, mode='constant')
    self.current_genBoard = temp_board
    self.next_genBoard = temp_board.copy()
    self.max_N = max_N
```
Save cell reproduction changes and advance one generation
```python
def advanceGen(self):
    self.current_genBoard = self.next_genBoard.copy()
```
Range current generation board and return reproduced cell changes of next generation board whilist
   - current_cell: current cell atributes
```python
def rangeBoard(self):
    self.advanceGen()
    for y in range(1, self.max_N+1):
        for x in range(1, self.max_N+1):
            current_cell = cell(boards, y, x)
            self.reproduceBoard(current_cell, self.countNeighbors(current_cell))
    boards.num_gen += 1
    cell.countCell()
    return self.next_genBoard
```
Count number of alive neighbors and returns that value
   - count_neighbors: number of alive neighbors
   - neighbor_cell: neighbor cell atributes
```python
def countNeighbors(self, current_cell):
    count_neighbors = 0
    for neighbor_y in range(current_cell.y-1, current_cell.y+2):
        for neighbor_x in range(current_cell.x-1, current_cell.x+2):
            neighbor_cell = cell(boards, neighbor_y, neighbor_x)
            if not ((neighbor_cell.y == current_cell.y) and (neighbor_cell.x == current_cell.x)):
                if(neighbor_cell.value == 1):
                    count_neighbors += 1
    return count_neighbors
```
Reproduce board
   - Any live cell with fewer than two live neighbours dies, as if by underpopulation
   - Any live cell with two or three live neighbours lives on to the next generation
   - Any live cell with more than three live neighbours dies, as if by overpopulation
   - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
```python
def reproduceBoard(self, current_cell, count_neighbors):
    if(current_cell.value == 0):
        if(count_neighbors == 3):
            self.next_genBoard[current_cell.y, current_cell.x] = 1
        else:
            self.next_genBoard[current_cell.y, current_cell.x] = 0
    elif(current_cell.value == 1):
        if((count_neighbors == 2) or (count_neighbors == 3)):
            self.next_genBoard[current_cell.y, current_cell.x] = 1
        else:
            self.next_genBoard[current_cell.y, current_cell.x] = 0
```
2. Cell class:
Each cell initializes itself with its position and value
```python
def __init__(self, boards, y, x):
    self.y = y
    self.x = x
    self.value = boards.current_genBoard[self.y, self.x]
```
Static method to count number of alive cell in current generation board and store it in "cellPer_i"
```python
@staticmethod
def countCell():
    aliveCell_count = 0
    for temp_y in range(1, boards.max_N+1):
        for temp_x in range(1, boards.max_N+1):
            tempCell = cell(boards, temp_y, temp_x)
            if(tempCell.value == 1):
                aliveCell_count += 1
    cell.cellPer_i[boards.num_gen] = aliveCell_count
```
