import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QGroupBox, QPushButton


class CreateBoard(QWidget):

    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        self.board = []
        self.board_tmp = []
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        grid = QGridLayout()
        self.setLayout(grid)
        for board_y in range(9):
            self.board.append([])
        for y_group in range(3):
            for x_group in range(3):
                current_group_box = QGroupBox()
                grid_group_box = QGridLayout()
                current_group_box.setLayout(grid_group_box)
                for y in range(3):
                    for x in range(3):
                        text = QLineEdit(self)
                        text.setMaxLength(1)
                        text.setFixedWidth(15)
                        text.setValidator(QIntValidator())
                        self.board[y_group * 3 + y].append(text)

                        # noinspection PyArgumentList
                        grid_group_box.addWidget(text, y, x)

                # noinspection PyArgumentList
                grid.addWidget(current_group_box, y_group, x_group)
        button_solve = QPushButton('Solve', self)
        button_solve.clicked.connect(self.solve)
        grid.addWidget(button_solve)
        button_clear = QPushButton('Clear', self)
        button_clear.clicked.connect(lambda: self.clear_table(1))
        grid.addWidget(button_clear)
        button_clear_solution = QPushButton('Clear Solution', self)
        button_clear_solution.clicked.connect(lambda: self.clear_table(0))
        grid.addWidget(button_clear_solution)
        self.show()

    @pyqtSlot()
    def solve(self):
        self.board_tmp = []
        self.get_fix_numbers()
        # print_table()
        y = -1
        while y < 8:
            y += 1
            x = -1
            while x < 8:
                x += 1
                if not self.get_valid_number(y, x):
                    (x, y) = self.get_xy(x, y)
                    if x == -1:
                        return
        self.print_table()

    def get_xy(self, x, y):
        # x = curr_x
        # y = curr_y
        while (y >= 0):
            while(x >= 0):
                if not self.get_valid_number(y, x):
                    self.board_tmp[y][x] = 0
                    x -= 1
                else:
                    return x, y
            x = 8
            y -= 1
        return -1, -1

    def get_valid_number(self, y, x):
        if self.board_tmp[y][x] > 9:
            return 1
        for current_num in range(self.board_tmp[y][x] + 1, 10):
            if self.check_num(current_num, x, y):
                self.board_tmp[y][x] = current_num
                return 1
        return 0

    def check_num(self, num, x, y):
        num_list = [num, num + 10]
        bad_num = 0
        for x_c in range(9):
            if x_c == x:
                continue
            if self.board_tmp[y][x_c] in num_list:
                return 0
        for y_c in range(9):
            if (y_c == y):
                continue
            if self.board_tmp[y_c][x] in num_list:
                return 0
        min_y = int(y / 3) * 3
        min_x = int(x / 3) * 3
        for y_c in range(min_y, min_y + 3):
            for x_c in range(min_x, min_x + 3):
                if x_c == x and y_c == y:
                    continue
                if self.board_tmp[y_c][x_c] in num_list:
                    return 0
        else:
            return 1

    # create the board_tmp with the user define numbers
    def get_fix_numbers(self):
        for y in range(9):
            self.board_tmp.append([])
            for x in range(9):
                text = self.board[y][x].text()
                if text == "":
                    self.board_tmp[y].append(0)
                else:
                    num = int(text) + 10
                    self.board_tmp[y].append(num)

    def clear_table(self, clear_all):
        self.get_fix_numbers()
        for y in range(9):
            for x in range(9):
                if clear_all:
                    self.board[y][x].clear()
                elif self.board_tmp[y][x] < 10:
                    self.board[y][x].clear()

    def print_table(self):
        for y in range(len(self.board_tmp)):
            for x in range(len(self.board_tmp)):
                # print(self.board_tmp[y][x])
                num = self.board_tmp[y][x]
                if num > 10:
                    num -= 10
                self.board[y][x].setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreateBoard()
    sys.exit(app.exec_())
