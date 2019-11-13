from tkinter import *
master = Tk()
#Label(master, text='First Name').grid(row=0)
#Label(master, text='Last Name').grid(row=1)
board = []
for y in range (0,9):
    board.append([])
    padY = 0
    if y % 3 == 0:
        padY = 5
    for x in range(0, 9):
        board[y].append(Entry(master,width = 3,bd = 5))
        padX = 0
        if x%3 == 0:
            padX = 5
        board[y][x].grid(row=x, column=y, padx = padX, pady = padY)
B = Button(master, text ="Solve",  bd = '5', command = print ("solev"))
B.grid(row=10,column=5)
mainloop()
def solve():
    print ("solve")
