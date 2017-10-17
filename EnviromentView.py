from tkinter import *

from StateView import StateView
from AgentView import AgentView
from ControlManager import ControlManager
import AppConfig
import time


class EnviromentView:
    STATE_WIDTH = 100

    def __init__(self, states, agent):
        self.__stateViewMatrix = {}
        self.__agentControl = agent
        self.__windowRoot = Tk()
        self.rows = len(states)
        self.columns = len(states[0])
        self.windowHeight = self.rows * self.STATE_WIDTH + 10
        self.windowWidth = self.columns * self.STATE_WIDTH + 10
        frame = Frame(self.__windowRoot, height=self.windowHeight, width=self.windowWidth, borderwidth=2)
        frame.pack()
        self.canvas = Canvas(frame, height=self.windowHeight, width=self.windowWidth)
        self.canvas.pack()
        self.__draw_states(self.rows, self.columns, states)
        self.__place_agent(agent)

    def __draw_states(self, rows, columns, states):

        x = y = 5
        for i in range(rows):
            for j in range(columns):
                squareView = self.canvas.create_rectangle(x, y, x+self.STATE_WIDTH, y+self.STATE_WIDTH)
                self.__stateViewMatrix[i, j] = StateView(states[i][j].get_type(), squareView, self.canvas)
                x += self.STATE_WIDTH
            x = 5
            y += self.STATE_WIDTH

    def __place_agent(self, agent):
        self.__agentView = AgentView(agent, self.__stateViewMatrix, self.canvas)
        self.move_agent()

    def move_agent(self):
        self.__agentView.move()

    def start(self):
        if AppConfig.START_MODE == "auto":
            self.__start_automatic()
        else:
            self.__start_by_click()

    def __start_by_click(self):
        ControlManager(self.__windowRoot, self.flow)
        self.__windowRoot.mainloop()

    def __start_automatic(self):
        while True:
            self.flow(None)
            self.__windowRoot.update()
            time.sleep(AppConfig.SPEED)
        self.__windowRoot.mainloop()

    def flow(self, event):
        self.__agentControl.choose_action()
        self.move_agent()
