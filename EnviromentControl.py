from random import randint

from EnviromentView import EnviromentView
from StateControl import StateControl


class EnviromentControl:

    ALL_TYPES = ["win", "hole", "wall", "floor"]
    STATE_TYPES = ["hole", "floor"]

    def __init__(self, rows, columns):

        self.__generate_random_matrix(rows, columns)
        EnviromentView(self.statesMatrix)

    def __generate_random_matrix(self, rows, columns):
        self.statesMatrix = [[StateControl(i, j, self.STATE_TYPES[randint(0, len(self.STATE_TYPES)-1)])
                              for j in range(columns)] for i in range(rows)]
        self.statesMatrix[randint(0, rows-1)][randint(0, columns-1)].set_type("win")
