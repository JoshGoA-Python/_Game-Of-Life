##UNDONE: Improve "insertBoard" function

#Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

#Cell atributes (position: y, x; value: 0, 1)
class cell:
    def __init__(self, y, x, temp_board):
        self.y = y
        self.x = x
        self.value = temp_board[self.y, self.x]

#Analize current_cell neighbor_cells
def neighbor_array(current_cell, board, temp_board):
    neighbors = 0
    for neighbor_y in range(current_cell.y-1, current_cell.y+2):
        for neighbor_x in range(current_cell.x-1, current_cell.x+2):
        	#Do not count current_cell as neighbor
            if not ((neighbor_y == current_cell.y) and (neighbor_x == current_cell.x)):
                neighbor_cell = cell(neighbor_y, neighbor_x, temp_board)
                #Count neighbor_cell as neighbor if neighbor_cell.value = 1
                if(neighbor_cell.value == 1):
                    neighbors += 1
    #Modify current_cell values based on neighbor_cells
    if(current_cell.value == 0):
        death_cell(current_cell, neighbors, board)
    if(current_cell.value == 1):
        alive_cell(current_cell, neighbors, board)

#Death cell (current_cell.value = 0)
def death_cell(current_cell, neighbors, board):
    if(neighbors == 3):
        board[current_cell.y, current_cell.x] = 1
    else:
        board[current_cell.y, current_cell.x] = 0

#Alive cell (current_cell.value = 1)
def alive_cell(current_cell, neighbors, board):
    if((neighbors == 2) or (neighbors == 3)):
        board[current_cell.y, current_cell.x] = 1
    else:
        board[current_cell.y, current_cell.x] = 0

#Manually select cell position (y*x)
def selectCells(board):
    max_cells = int(input("Input max_cells: "))
    for select in range(0, max_cells):
        select_y, select_x = input(str(select + 1) + ": ").split("*")
        select_y = int(select_y) + 1
        select_x = int(select_x) + 1
        board[select_y, select_x] = 1
    return board

#Insert none valued arrays to board
def insertBoard(board, max_y, max_x):
    board = np.insert(board, 0, 0, axis = 1)
    board = np.insert(board, max_x+1, 0, axis = 1)
    board = np.insert(board, 0, 0, axis = 0)
    board = np.insert(board, max_y+1, 0, axis = 0)
    return board

#Define board area
max_x = max_y = 50
#Define numpy arrays
board = np.random.randint(2, size = (max_y, max_x))
board = insertBoard(board, max_y, max_x)
temp_board = board.copy()
#Define matplotlib instances
fig, ax = plt.subplots()
im = ax.imshow(board, cmap = mcolors.ListedColormap(['White', 'Black']))
plt.axis('off')

#Board animation (change board value repeatedly)
def animate(i):
    #Save board for next generation
    temp_board = board.copy()
    for y in range(1, max_y+1):
        for x in range(1, max_x+1):
            current_cell = cell(y, x, temp_board)
            neighbor_array(current_cell, board, temp_board)
    #Save animation
    im.set_data(temp_board)
    return [im]

#Draw board
anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 10, blit = False, repeat = True)
plt.show()