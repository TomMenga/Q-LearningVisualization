from random import randint

from EnviromentView import EnviromentView
from StateControl import StateControl
from StandardAgentControl import StandardAgentControl
from ControlManager import ControlManager


class EnviromentControl:

    ALL_TYPES = ["win", "hole", "wall", "floor"]
    STATE_TYPES = ["floor"] #Tipi accettati nella partita
    AGENT_START_POSITION = [0, 0]

    def __init__(self, rows, columns):

        self.__generate_random_matrix(rows, columns)
        self.__create_agent(self.AGENT_START_POSITION)
        self.__enviroment_view = EnviromentView(self.statesMatrix, self.agentControl)
        self.__enviroment_view.start()

    def __generate_random_matrix(self, rows, columns):
        self.statesMatrix = [[StateControl(i, j, self.STATE_TYPES[randint(0, len(self.STATE_TYPES)-1)])
                              for j in range(columns)] for i in range(rows)]
        #self.statesMatrix[randint(0, rows-1)][randint(0, columns-1)].set_type("win")
        self.statesMatrix[rows-1][columns-1].set_type("win")
        #self.statesMatrix[0][3].set_type("wall")

    def __create_agent(self, cords):
        self.agentControl = StandardAgentControl(cords, self.statesMatrix)
