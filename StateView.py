
class StateView:

    def __init__(self, stateType, squareView, canvas):
        self.stateType = stateType
        self.squareView = squareView
        rect = canvas.bbox(squareView)
        rectCenter = (rect[2] - rect[0])/2
        self.center_x = rect[0] + rectCenter
        self.center_y = rect[1] + rectCenter
        self.canvas = canvas
        if stateType == "hole":
            canvas.itemconfig(squareView, fill='black')
        elif stateType == "win":
            canvas.itemconfig(squareView, fill='green')
        elif stateType == "wall":
            canvas.itemconfig(squareView, fill='grey')
        elif stateType == "floor":
            canvas.itemconfig(squareView, fill='white')

