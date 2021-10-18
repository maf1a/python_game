from RectangleClass import Rectangle
import colors
from random import random

class Enemy:
    alive = True

    def __init__(self, pygame, windowSurface):
        self.shape = Rectangle(pygame, windowSurface, colors.GREEN, random() * 500, 0, 30, 30)

    def target(self, bullet):
        if bullet.isRemoved == True:
            return False

        vs = self.shape.vCenter
        vb = bullet.vCenter

        if vs.x - 15 > vb.x + 3:
            return False

        if vs.x + 15 < vb.x - 3:
            return False

        if vs.y - 15 > vb.y + 3:
            return False

        if vs.y + 15 < vb.y - 3:
            return False

        bullet.remove()
        self.becomeKilled()

    def becomeKilled(self):
        self.alive = False

    def update(self):
        self.shape.setY(self.shape.vCenter.y + 2)

    def draw(self):
        if self.alive == True:
            self.shape.draw()
