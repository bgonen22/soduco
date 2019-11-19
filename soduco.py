import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QGroupBox, QPushButton


class CreateBoard(QWidget):

    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        self.grid = QGridLayout()
        self.error_msg = QLineEdit(self)
        self.error_msg.setEnabled(0)
        self.grid.addWidget(self.error_msg, 4, 0)
        self.board = []
        self.board_tmp = []
        self.title = 'Soduco Solver'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.grid)
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
                        text.textEdited.connect(lambda: self.check_input())
                        self.board[y_group * 3 + y].append(text)

                        # noinspection PyArgumentList
                        grid_group_box.addWidget(text, y, x)

                # noinspection PyArgumentList
                self.grid.addWidget(current_group_box, y_group, x_group)
        self.button_solve = QPushButton('Solve', self)
        self.button_solve.clicked.connect(self.solve)
        self.grid.addWidget(self.button_solve)
        button_clear = QPushButton('Clear', self)
        button_clear.clicked.connect(lambda: self.clear_table(1))
        self.grid.addWidget(button_clear)
        button_clear_solution = QPushButton('Clear Solution', self)
        button_clear_solution.clicked.connect(lambda: self.clear_table(0))
        self.grid.addWidget(button_clear_solution)
        self.show()

    @pyqtSlot()
    def solve(self):
        if not self.check_input():
            self.error_msg.setText("Please fix the red values")
            self.error_msg.setStyleSheet("color:red;")
            return
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
                        text = QLineEdit(self)
                        text.setText("No Solution Found")
                        self.grid.addWidget(text)
                        self.show()
                        return
        self.print_table()

    def get_xy(self, x, y):
        while y >= 0:
            while x >= 0:
                if not self.get_valid_number(y, x):
                    self.board_tmp[y][x] = 0
                    x -= 1
                    if self.board_tmp[y][x] > 10:  # this is the user define value need to go one cell back
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

    def check_input(self):
        self.get_fix_numbers()
        status = 1
        for y in range(9):
            for x in range(9):
                if self.board_tmp[y][x] == 0:
                    self.board[y][x].setStyleSheet("color: black;")
                    continue
                if not self.check_num(self.board_tmp[y][x], x, y):
                    self.board[y][x].setStyleSheet("color: red;")
                    status = 0
                else:
                    self.board[y][x].setStyleSheet("color: green;")
        if status:
            self.error_msg.setText("Ready To Solve")
            self.error_msg.setStyleSheet("color: green;")
            self.button_solve.setEnabled(1)
        else:
            self.error_msg.setText("Please fix the red values")
            self.error_msg.setStyleSheet("color:red;")
            self.button_solve.setEnabled(0)
        return status

    def check_num(self, num, x, y):
        num_list = [num, num + 10]
        for x_c in range(9):
            if x_c == x:
                continue
            if self.board_tmp[y][x_c] in num_list:
                return 0
        for y_c in range(9):
            if y_c == y:
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
        self.board_tmp = []
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
        # self.get_fix_numbers()
        for y in range(9):
            for x in range(9):
                if clear_all:
                    self.board[y][x].clear()
                    self.board_tmp[y][x] = 0
                elif self.board_tmp[y][x] < 10:
                    self.board[y][x].clear()
                    self.board_tmp[y][x] = 0

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
