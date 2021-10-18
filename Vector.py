import copy

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCords(self):
        return copy.deepcopy(self)
    
    def setCords(self, x, y):
        self.x = x
        self.y = y