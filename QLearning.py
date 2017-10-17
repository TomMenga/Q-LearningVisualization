import AppConfig
from random import choice


class QLearning:

    INITIAL_VALUE = 0
    TOTAL_SCORE = 0

    def __init__(self, rows, columns, actions):
        self.matrix = {}
        self.__currentTurn = []
        self.__rows = rows
        self.__columns = columns
        self.actions = actions
        for i in range(rows):
            for j in range(columns):
                self.matrix[i, j] = {}
                for act in actions:
                    self.matrix[i, j][act] = self.INITIAL_VALUE

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
                bestActions.append(i)
            elif availableMoves[self.actions[i]] == maxValue:
                bestActions.append(i)
        choosedAction = self.actions[choice(bestActions)]
        self.__currentTurn = [x, y, choosedAction]
        self.__print_choosen_moves(bestActions)
        print("Choosed action: " + choosedAction)
        return choosedAction

    def take_reward(self, reward, nextState):
        x = self.__currentTurn[0]
        y = self.__currentTurn[1]
        action = self.__currentTurn[2]
        self.matrix[x, y][action] = AppConfig.ALPHA * reward + AppConfig.GAMMA * self.__getMaxQ(nextState)
        print("Reward for action: " + str(reward))
        self.__print_matrix()

    def __getMaxQ(self, state):
        x = state[0]
        y = state[1]
        maxQ = -99999
        allMoves = self.matrix[x, y]
        for i in range(len(self.actions)):
            if allMoves[self.actions[i]] > maxQ:
                maxQ = allMoves[self.actions[i]]
        print(str(maxQ) + " of " + str(state))
        return maxQ

    def __print_choosen_moves(self, choosenMoves):
        rowprint = "Best actions: "
        for move in choosenMoves:
            rowprint += str(self.actions[move]) + " "
        print(rowprint)

    def __print_matrix(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                rowprint = "[" + str(i) + ", " + str(j) + "]" + "   " + str(self.matrix[i, j])
                #rowprint = str(elem)
                print(rowprint)
