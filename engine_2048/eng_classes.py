#
# from engine_2048 import gameboard
#

class GameDefinitions:

    def __init__(self, board_size=4):
        self.__boardSize = board_size  # a square size __boardSize
        self.__number_2_probability = 90  # percentage
        self.__number_4_probability = 10  # percentage

    def get_board_size(self) -> int:
        return self.__boardSize

    def get_2_probability(self) -> int:
        return self.__number_2_probability

    def get_4_probability(self) -> int:
        return self.__number_4_probability


class GameStatus:

    def __init__(self):
        self.__game_over = False
        self.__score = 0

    def set_score(self, score):
        self.__score += score

    def reset_score(self):
        self.__score = 0

    def set_game_over(self, game_over):
        self.__game_over = game_over

    def get_score(self):
        return self.__score

    def get_game_over(self):
        return self.__game_over


class Position:

    def __init__(self):
        self.value: int = None
        self.x: int = None  # x is the line starting from upper-side
        self.y: int = None  # y is the column starting from left-side

    def set_value(self, value: int):
        self.value = value

    def get_value(self):
        return self.value

    def get_position(self) -> [int, int]:
        return [self.x, self.y]

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Neighbors(Position):
    left_neighbor = Position()
    right_neighbor = Position()
    up_neighbor = Position()
    down_neighbor = Position()

    def __init__(self, xy_index, board_size):
        Position.__init__(self)
        # Setting Cell's Positions
        self.x = int(xy_index / board_size)
        self.y = xy_index - board_size * self.x
        self.xy_index = xy_index
        # setting Default Neighbors
        self.is_left_border_cell = False
        self.is_right_border_cell = False
        self.is_up_border_cell = False
        self.is_down_border_cell = False

    def find_neighbors(self, cells):
        for obj in cells:
            if (self.y - 1 == obj.y) and (self.x == obj.x):
                # Neighbor at left
                self.left_neighbor = obj
            if (self.y + 1 == obj.y) and (self.x == obj.x):
                # Neighbor at right
                self.right_neighbor = obj
            if (self.y == obj.y) and (self.x - 1 == obj.x):
                # Neighbor at up
                self.up_neighbor = obj
            if (self.y == obj.y) and (self.x + 1 == obj.x):
                # Neighbor at up
                self.down_neighbor = obj

    def get_neighborhood(self):
        return [self.left_neighbor.get_position(),
                self.right_neighbor.get_position(),
                self.up_neighbor.get_position(),
                self.down_neighbor.get_position()]

    def set_neighborhood(self, obj_left, obj_right, obj_up, obj_down):
        self.left_neighbor = obj_left
        self.right_neighbor = obj_right
        self.up_neighbor = obj_up
        self.down_neighbor = obj_down

    def get_left_neighbor(self):
        return self.left_neighbor

    def get_right_neighbor(self):
        return self.right_neighbor

    def get_up_neighbor(self):
        return self.up_neighbor

    def get_down_neighbor(self):
        return self.down_neighbor

    def set_left_neighbor(self, obj_left):
        self.left_neighbor = obj_left

    def set_right_neighbor(self, obj_right):
        self.right_neighbor = obj_right

    def set_up_neighbor(self, obj_up):
        self.up_neighbor = obj_up

    def set_down_neighbor(self, obj_down):
        self.down_neighbor = obj_down

    def find_your_border_set(self):
        self.is_left_border_cell = True if self.left_neighbor.get_position() == [None, None] else False
        self.is_right_border_cell = True if self.right_neighbor.get_position() == [None, None] else False
        self.is_up_border_cell = True if self.up_neighbor.get_position() == [None, None] else False
        self.is_down_border_cell = True if self.down_neighbor.get_position() == [None, None] else False


class GameCell(Neighbors):

    def __init__(self, xy_index, board_size):
        Neighbors.__init__(self, xy_index, board_size)
        self.cellPositionClassification = None
        # print(xyIndex)

    def start_join_your_neighbor(self, navigation, status):
        if navigation.keyPress['left'] and self.is_left_border_cell:
            # print(f'{self.getPosition()}: I am a LeftBorder Cell and I am going to start the Reconfiguration')
            if (self.get_value() is not None) and (self.get_value() == self.right_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.right_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.right_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['right'] and self.is_right_border_cell:
            # print(f'{self.getPosition()}: I am a rightBorder Cell and I am going to start the Reconfiguration')
            if (self.get_value() is not None) and (self.get_value() == self.left_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.left_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.left_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['up'] and self.is_up_border_cell:
            # print(f'{self.getPosition()}: I am a upBorder Cell and I am going to start the Reconfiguration')
            if (self.get_value() is not None) and (self.get_value() == self.down_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.down_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.down_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['down'] and self.is_down_border_cell:
            # print(f'{self.getPosition()}: I am a downBorder Cell and I am going to start the Reconfiguration')
            if (self.get_value() is not None) and (self.get_value() == self.up_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.up_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.up_neighbor.join_your_neighbor(navigation, status)

    def start_push_value(self, navigation):
        if navigation.keyPress['left'] and self.is_right_border_cell:
            if self.left_neighbor.value is None:
                self.left_neighbor.value, self.value = self.value, self.left_neighbor.value
            self.left_neighbor.push_value(navigation)
        #
        if navigation.keyPress['right'] and self.is_left_border_cell:
            if self.right_neighbor.value is None:
                self.right_neighbor.value, self.value = self.value, self.right_neighbor.value
            self.right_neighbor.push_value(navigation)

        if navigation.keyPress['up'] and self.is_down_border_cell:
            if self.up_neighbor.value is None:
                self.up_neighbor.value, self.value = self.value, self.up_neighbor.value
            self.up_neighbor.push_value(navigation)

        if navigation.keyPress['down'] and self.is_up_border_cell:
            if self.down_neighbor.value is None:
                self.down_neighbor.value, self.value = self.value, self.down_neighbor.value
            self.down_neighbor.push_value(navigation)

    def push_value(self, navigation):
        if navigation.keyPress['left'] and not self.is_left_border_cell:
            if self.left_neighbor.value is None:
                self.left_neighbor.value, self.value = self.value, self.left_neighbor.value
            self.left_neighbor.push_value(navigation)

        if navigation.keyPress['right'] and not self.is_right_border_cell:
            if self.right_neighbor.value is None:
                self.right_neighbor.value, self.value = self.value, self.right_neighbor.value
            self.right_neighbor.push_value(navigation)

        if navigation.keyPress['up'] and not self.is_up_border_cell:
            if self.up_neighbor.value is None:
                self.up_neighbor.value, self.value = self.value, self.up_neighbor.value
            self.up_neighbor.push_value(navigation)

        if navigation.keyPress['down'] and not self.is_down_border_cell:
            if self.down_neighbor.value is None:
                self.down_neighbor.value, self.value = self.value, self.down_neighbor.value
            self.down_neighbor.push_value(navigation)

    def join_your_neighbor(self, navigation, status):
        if navigation.keyPress['left'] and (not self.is_right_border_cell):
            if (self.get_value() is not None) and (self.get_value() == self.right_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.right_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.right_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['right'] and (not self.is_left_border_cell):
            if (self.get_value() is not None) and (self.get_value() == self.left_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.left_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.left_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['up'] and (not self.is_down_border_cell):

            if (self.get_value() is not None) and (self.get_value() == self.down_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.down_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.down_neighbor.join_your_neighbor(navigation, status)

        if navigation.keyPress['down'] and (not self.is_up_border_cell):
            if (self.get_value() is not None) and (self.get_value() == self.up_neighbor.get_value()):
                self.set_value(2 * self.get_value())
                self.up_neighbor.set_value(None)
                status.set_score(self.get_value())
            #
            self.up_neighbor.join_your_neighbor(navigation, status)

    def find_game_over(self, status):
        if self.value is not None:
            if self.left_neighbor.value == self.value or self.right_neighbor.value == self.value or \
                    self.up_neighbor.value == self.value or self.down_neighbor.value == self.value:
                status.set_game_over(False)
