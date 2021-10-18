from Vector import Vector

class Rectangle:
    isRemoved = False

    def __init__(self, pygame, windowSurface, color, centerX, centerY, width, height):
        self.pygame = pygame
        self.windowSurface = windowSurface
        self.color = color
        self.width = width
        self.height = height
        self.vCenter = Vector(centerX, centerY)

    def remove(self):
        self.isRemoved = True

    def setCenter(self, x, y):
        self.vCenter.setCords(x, y)

    def setX(self, x):
        self.vCenter.setCords(x, self.vCenter.y)

    def setY(self, y):
        self.vCenter.setCords(self.vCenter.x, y)

    def draw(self):
        if self.isRemoved == True:
            return

        center = self.vCenter.getCords()

        lt = Vector(center.x - self.width / 2, center.y - self.height / 2)
        rt = Vector(center.x + self.width / 2, center.y - self.height / 2)
        lb = Vector(center.x - self.width / 2, center.y + self.height / 2)
        rb = Vector(center.x + self.width / 2, center.y + self.height / 2)

        self.pygame.draw.polygon(self.windowSurface, self.color, ((lt.x, lt.y),(rt.x, rt.y),(lb.x, lb.y),(rb.x, rb.y)))
