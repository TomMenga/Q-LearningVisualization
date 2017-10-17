import copy
from QLearning import QLearning


class StandardAgentControl:
    AVAILABLE_COMMAND = ["right", "up", "left", "down"]

    def __init__(self, cords, statesMatrix):
        self.__startState = copy.deepcopy(cords)
        self.currentCords = cords
        self.totalScore = 0
        self.__bumpInWall = False
        self.__statesMatrix = statesMatrix
        self.__matrixSize = (len(statesMatrix), len(statesMatrix[0]))
        self.__learningClass = QLearning(self.__matrixSize[0], self.__matrixSize[1], self.AVAILABLE_COMMAND)

    def choose_action(self):

        if self.__statesMatrix[self.currentCords[0]][self.currentCords[1]].get_type() == "win" or \
                self.__statesMatrix[self.currentCords[0]][self.currentCords[1]].get_type() == "hole":
            print("#### NEXT EPISODE #### \n")
            print(str(self.__startState))
            self.currentCords = copy.deepcopy(self.__startState)
        else:
            action = self.__learningClass.choose_action(self.currentCords)
            self.__execute_action(action)
            self.__evaluate_consequence(self.currentCords[0], self.currentCords[1])

    def __execute_action(self, action):
        self.__bumpInWall = False
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
        else:
            self.__bumpInWall = True

    def __up(self):
        dest_x = self.currentCords[0] - 1
        dest_y = self.currentCords[1]

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[0] -= 1
        else:
            self.__bumpInWall = True

    def __left(self):
        dest_x = self.currentCords[0]
        dest_y = self.currentCords[1] - 1

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[1] -= 1
        else:
            self.__bumpInWall = True

    def __down(self):
        dest_x = self.currentCords[0] + 1
        dest_y = self.currentCords[1]

        if self.__is_in_bound(dest_x, dest_y) and \
                not self.__is_a_wall(dest_x, dest_y):
            self.currentCords[0] += 1
        else:
            self.__bumpInWall = True

    def __is_in_bound(self, x, y):
        return x < self.__matrixSize[0] and x >= 0 \
               and y < self.__matrixSize[1] and y >= 0

    def __is_a_wall(self, x, y):
        return self.__statesMatrix[x][y].get_type() == "wall"

    def __evaluate_consequence(self, x, y):
        if self.__bumpInWall:
            reward = -1
        elif self.__statesMatrix[x][y].get_type() == "win":
            reward = 10
        elif self.__statesMatrix[x][y].get_type() == "hole":
            reward = -5
        else:
            reward = -0.2
        self.__learningClass.take_reward(reward, self.currentCords)
