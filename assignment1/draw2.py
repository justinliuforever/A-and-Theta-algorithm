from tkinter import Tk, Canvas, Frame, BOTH
from array import *
# 4x3
T = [[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0],
     [2, 1, 0], [2, 2, 1], [2, 3, 0], [2, 4, 0],
     [3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0]]
#print(T[0][0])


'''
Tblock  = [[0 for c in range(4)] for r in range(3)]
for i in range(len(Tblock)):
  for j in range(len(Tblock[i])):
    print(Tblock[i][j])
'''

root = Tk()
root.title('Assignment1')
root.geometry("550x550")



# INPUT: how many in x, how many in y
Nx = 6; Ny = 4;
gridSize = 50
# width, height distance
Pwidth = Nx*gridSize; Pheight = Ny*gridSize


my_canvas = Canvas(root, width=Pwidth, height=Pheight)
my_canvas.pack()

x = 0; x1 = 0+gridSize
y = 0+gridSize; y1 = 0
i = 0; j = 0; r = 0

##
# adjust the value into the grid_size, in a bid to mach x,y value
for i in range(len(T)):
    for j in range(len(T[i])-1):
        T[i][j] = T[i][j]*gridSize
    print(T[i])


for i in range(len(T)):
    if (T[i][2]==1):
        my_canvas.create_rectangle(T[i][1]-gridSize, T[i][0], T[i][1], T[i][0]-gridSize, fill='black')
    else:
        my_canvas.create_rectangle(T[i][1] - gridSize, T[i][0], T[i][1], T[i][0] - gridSize, fill='white')
##
'''
while j < Ny:

    while i < Nx:

        my_canvas.create_rectangle(x, y, x1, y1,  fill='white')
        #print(x, y, x1, y1)
        x = x + gridSize
        x1 = x1 + gridSize
        i = i + 1
    x = 0; x1 = 0 +gridSize
    y = y + gridSize; y1 = y1 + gridSize
    j = j + 1
    i = 0
'''

root.mainloop()