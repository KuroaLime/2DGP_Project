from stage import *

class Camera:
    def __init__(self):
        self.WID, self.HEI = WID//2+400, HEI//2
    def __getstate__(self):
        state = {'x':self.WID, 'y':self.HEI}
        return state
    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)
    def update(self):
        pass

    def draw(self):
        pass
