#UNDONE: Make grid

#Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

#Board atributes (current_genBoard, next_genBoard, max_N)
class board:

    #Initialize boards with random integer numbers (0, 1) padded with 0
    def __init__(self, max_N):
        temp_board = np.random.randint(2, size = (max_N, max_N))
        temp_board = np.pad(temp_board, 1, mode='constant')
        self.current_genBoard = temp_board
        self.next_genBoard = temp_board.copy()
        self.max_N = max_N

    #Save board changes
    def advanceGen(self):
        #Advance board to next generation
        self.current_genBoard = self.next_genBoard.copy()

    #Range board
    def rangeBoard(self):
        self.advanceGen()
        for y in range(1, self.max_N+1):
            for x in range(1, self.max_N+1):
                #Save current cell atributes
                current_cell = cell(boards, y, x)
                self.reproduceBoard(current_cell, self.countNeighbors(current_cell))
        return self.next_genBoard

    #Range current cells neighbors
    def countNeighbors(self, current_cell):
        count_neighbors = 0
        for neighbor_y in range(current_cell.y-1, current_cell.y+2):
            for neighbor_x in range(current_cell.x-1, current_cell.x+2):
                #Save neighbor cell atributes
                neighbor_cell = cell(boards, neighbor_y, neighbor_x)
                #Do not count current cell as neighbor cell
                if not ((neighbor_cell.y == current_cell.y) and (neighbor_cell.x == current_cell.x)):
                    #Only count neighbor if neighbor cell is alive
                    if(neighbor_cell.value == 1):
                        count_neighbors += 1
        return count_neighbors

    #Modify current_cell values based on neighbor_cells
    def reproduceBoard(self, current_cell, count_neighbors):
        #Death cell
        if(current_cell.value == 0):
            if(count_neighbors == 3):
                self.next_genBoard[current_cell.y, current_cell.x] = 1
            else:
                self.next_genBoard[current_cell.y, current_cell.x] = 0
        #Alive cell
        elif(current_cell.value == 1):
            if((count_neighbors == 2) or (count_neighbors == 3)):
                self.next_genBoard[current_cell.y, current_cell.x] = 1
            else:
                self.next_genBoard[current_cell.y, current_cell.x] = 0

#Cell atributes (y, x, value)
class cell:

    #Initialize cell with position and value
    def __init__(self, boards, y, x):
        self.y = y
        self.x = x
        self.value = boards.current_genBoard[self.y, self.x]

    #Count number of living cells
    @staticmethod
    def countCell():
        aliveCell_count = 0
        for temp_y in range(1, boards.max_N+1):
            for temp_x in range(1, boards.max_N+1):
                tempCell = cell(boards, temp_y, temp_x)
                if(tempCell.value == 1):
                    aliveCell_count += 1
        return aliveCell_count

#Board area
max_N = 50
#Figure area
figsize_N = 5
#Animations frame per second
fps = 100
#Interval between aniimation
interval = 10
#Plot axis show
axis_show = 'off'   #'on' 'off'
#Plot grid show
grid_show = True    #True False

#Boards
boards = board(max_N)
#Animation
fig, ax = plt.subplots(1, figsize = (figsize_N, figsize_N))
im = ax.imshow(boards.next_genBoard, cmap = mcolors.ListedColormap(['White', 'Black']))
plt.axis(axis_show)

#Board animation (change board value repeatedly)
def animate(i):
    im.set_data(boards.rangeBoard())
    return [im]

#Draw board
anim = animation.FuncAnimation(fig, animate, frames = fps, interval = interval, blit = False, repeat = True)
plt.show()
