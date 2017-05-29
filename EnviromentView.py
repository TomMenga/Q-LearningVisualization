from tkinter import *

from StateView import StateView


class EnviromentView:
    STATE_WIDTH = 100

    def __init__(self, states):
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
        self.__windowRoot.mainloop()

    def __draw_states(self, rows, columns, states):

        x = y = 5
        for i in range(rows):
            for j in range(columns):
                squareView = self.canvas.create_rectangle(x, y, x+self.STATE_WIDTH, y+self.STATE_WIDTH)
                StateView(states[i][j].get_type(), squareView, self.canvas)
                x += self.STATE_WIDTH
            x = 5
            y += self.STATE_WIDTH
