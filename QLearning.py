from random import randint
from random import choice


class QLearning:

    INITIAL_VALUE = 0

    def __init__(self, rows, columns, actions):
        self.matrix = {}
        self.actions = actions
        for i in range(rows):
            for j in range(columns):
                self.matrix[i, j] = {}
                for act in actions:
                    self.matrix[i, j][act] = self.INITIAL_VALUE
        #self.print_matrix(rows, columns)

    def print_matrix(self, rows, columns):
        for i in range(rows):
            for j in range(columns):
                rowprint = "[" + str(i) + ", " + str(j) + "]" + "   " + str(self.matrix[i, j])
                print(rowprint)

    def choose_action(self, currentState):
        x = currentState[0]
        y = currentState[1]
        bestActions = []
        maxValue = -99999
        availableMoves = self.matrix[x, y]
        for i in range(len(self.actions)):
            if availableMoves[self.actions[i]] > maxValue:
                maxValue = availableMoves[self.actions[i]]
                bestActions = []
                bestActions.append(self.actions[i])
            elif availableMoves[self.actions[i]] == maxValue:
                bestActions.append(self.actions[i])
        print("choosen moves: " + str(bestActions))
        return choice(bestActions)
