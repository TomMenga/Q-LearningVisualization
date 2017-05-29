
class StateControl:

    def __init__(self, xCord, yCord, stateType):
        self.xCord = xCord
        self.yCord = yCord
        self.stateType = stateType

    def __str__(self):
        return str(self.xCord) + "." + str(self.yCord)

    def get_type(self):
        return self.stateType

    def set_type(self, stateType):
        self.stateType = stateType
