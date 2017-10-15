from random import randint
from QLearning import QLearning


class StandardAgentControl:
    AVAILABLE_COMMAND = ["right", "up", "left", "down"]

    def __init__(self, cords, statesMatrix):
        self.currentCords = cords
        self.__statesMatrix = statesMatrix
        self.__matrixSize = (len(statesMatrix), len(statesMatrix[0]))
        self.__learningClass = QLearning(self.__matrixSize[0], self.__matrixSize[1], self.AVAILABLE_COMMAND)

    def choose_action(self):
        #userà l'algoritmo Q-learning
        #action = self.AVAILABLE_COMMAND[randint(0, len(self.AVAILABLE_COMMAND)-1)]
        action = self.__learningClass.choose_action(self.currentCords)
        print(action)
        self.__execute_action(action)

    def __execute_action(self, action):
        if action == "right":
            self.__right()
        elif action == "up":
            self.__up()
        elif action == "left":
            self.__left()
        else:
            self.__down()

    def __right(self):
        dest_x = self.currentCords[0]
        dest_y = self.currentCords[1] + 1

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[1] += 1

        self.__evaluate_consequence()

    def __up(self):
        dest_x = self.currentCords[0] - 1
        dest_y = self.currentCords[1]

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[0] -= 1

        self.__evaluate_consequence()

    def __left(self):
        dest_x = self.currentCords[0]
        dest_y = self.currentCords[1] - 1

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[1] -= 1

        self.__evaluate_consequence()

    def __down(self):
        dest_x = self.currentCords[0] + 1
        dest_y = self.currentCords[1]

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[0] += 1

        self.__evaluate_consequence()

    def __is_in_bound(self, x, y):
        return x < self.__matrixSize[0] and x >= 0 \
               and y < self.__matrixSize[1] and y >= 0

    def __is_a_wall(self, x, y):
        return self.__statesMatrix[x][y].get_type() == "wall"

    def __evaluate_consequence(self):
        return  0
