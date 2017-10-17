import AppConfig
from random import randint
from EnviromentView import EnviromentView
from StateControl import StateControl
from StandardAgentControl import StandardAgentControl


class EnviromentControl:

    ALL_TYPES = ["win", "hole", "wall", "floor"]
    STATE_TYPES = ["floor"] #Tipi accettati nella partita
    AGENT_START_POSITION = [0, 0]

    def __init__(self, rows, columns):

        self.__generate_matrix(rows, columns)
        self.__create_agent(self.AGENT_START_POSITION)
        self.__enviroment_view = EnviromentView(self.statesMatrix, self.agentControl)
        self.__enviroment_view.start()

    def __generate_matrix(self, rows, columns):
        self.statesMatrix = [[StateControl(i, j, self.STATE_TYPES[randint(0, len(self.STATE_TYPES)-1)])
                              for j in range(columns)] for i in range(rows)]
        if AppConfig.ENVIROMENT_TYPE == "free":
            self.__free(rows, columns)
        elif AppConfig.ENVIROMENT_TYPE == "labirinto":
            self.__labirinto(rows, columns)
        elif AppConfig.ENVIROMENT_TYPE == "big":
            self.__big()

    def __labirinto(self, rows, columns):
        self.statesMatrix[rows - 1][columns - 1].set_type("win")
        self.statesMatrix[1][1].set_type("wall")
        self.statesMatrix[2][1].set_type("wall")

        self.statesMatrix[1][4].set_type("wall")
        self.statesMatrix[1][3].set_type("wall")

        self.statesMatrix[2][0].set_type("hole")
        self.statesMatrix[0][4].set_type("hole")

    def __free(self, rows, columns):
        self.statesMatrix[rows - 1][columns - 1].set_type("win")

    def __big(self):
        rows = 5
        columns = 7
        self.statesMatrix = [[StateControl(i, j, self.STATE_TYPES[randint(0, len(self.STATE_TYPES) - 1)])
                              for j in range(columns)] for i in range(rows)]

        self.statesMatrix[rows - 1][columns - 1].set_type("win")

        self.statesMatrix[2][1].set_type("wall")
        self.statesMatrix[2][2].set_type("wall")
        self.statesMatrix[3][2].set_type("wall")
        self.statesMatrix[4][2].set_type("wall")
        self.statesMatrix[2][3].set_type("wall")
        self.statesMatrix[2][4].set_type("wall")
        self.statesMatrix[3][6].set_type("hole")
        self.statesMatrix[4][0].set_type("hole")

    def __create_agent(self, cords):
        self.agentControl = StandardAgentControl(cords, self.statesMatrix)
