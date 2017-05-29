
class StateView:

    def __init__(self, stateType, squareView, canvas):
        self.stateType = stateType
        self.squareView = squareView
        self.canvas = canvas
        if stateType == "hole":
            canvas.itemconfig(squareView, fill='black')
        elif stateType == "win":
            canvas.itemconfig(squareView, fill='green')
        elif stateType == "wall":
            canvas.itemconfig(squareView, fill='grey')
        elif stateType == "floor":
            canvas.itemconfig(squareView, fill='white')

