class AgentView:

    def __init__(self, agentControl, states, canvas):
        self.__agentControl = agentControl
        self.__statesMatrix = states
        self.__canvas = canvas
        self.__draw_agent()

    def move(self):
        self.__canvas.delete(self.__agentCircle)
        self.__draw_agent()

    def __draw_agent(self):
        state = self.__statesMatrix[self.__agentControl.currentCords[0], self.__agentControl.currentCords[1]]
        self.__agentCircle = self.__create_circle(state.center_x, state.center_y, 30)

    def __create_circle(self, x, y, r):
        return self.__canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
