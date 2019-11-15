import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QGroupBox


class CreateBoard(QWidget):
    board = []

    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        board = []
        grid = QGridLayout()
        self.setLayout(grid)

        for y_group in range(3):
            for x_group in range(3):
                current_group_box = QGroupBox()
                grid_group_box = QGridLayout()
                current_group_box.setLayout(grid_group_box)

                for y in range(3):
                    board.append([])
                    for x in range(3):
                        text = QLineEdit(self)
                        text.setMaxLength(1)
                        text.setFixedWidth(15)
                        # text.setFrame()
                        # text.move(40, 20)
                        # text.resize(280, 40)
                        board[y].append(text)

                        # noinspection PyArgumentList
                        grid_group_box.addWidget(text, x, y)

                # noinspection PyArgumentList
                grid.addWidget(current_group_box, x_group, y_group)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateBoard()
    sys.exit(app.exec_())


#         for y in range (0,9):
#             board.append([])
#             padY = 0
#             if y % 3 == 0:
#                 padY = 5
#             for x in range(0, 9):
#                 board[y].append(textbox = QLineEdit(self))
#                 padX = 0
#                 if x%3 == 0:
#                     padX = 5
#                 board[y][x].grid(row=x, column=y, padx = padX, pady = padY)
#         B = Button(master, text ="Solve",  bd = '5', command = print ("solev"))
#         B.grid(row=10,column=5)
# mainloop()
def solve():
    print("solve")
