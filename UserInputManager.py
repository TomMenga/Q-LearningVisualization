from msvcrt import getch


class UserInputManager:

    def __init__(self, windowsRoot, action):
        self.__subscribe_button(windowsRoot, action)

    def __subscribe_button(self, windowsRoot, action):
        windowsRoot.bind("<Button-1>", action)
