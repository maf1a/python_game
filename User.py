from RectangleClass import Rectangle
import colors

class User:
    bullets = []

    def __init__(self, pygame, windowSurface):
        self.pygame = pygame
        self.windowSurface = windowSurface
        self.shape = Rectangle(pygame, windowSurface, colors.BLUE, 100, 380, 20, 20)
    
    def goLeft(self): 
        self.shape.setX(self.shape.vCenter.x - 10)

    def goRight(self): 
        self.shape.setX(self.shape.vCenter.x + 10)

    def shoot(self):
        bullet = Rectangle(self.pygame, self.windowSurface, colors.RED, self.shape.vCenter.x, self.shape.vCenter.y, 6, 6)
        self.bullets.append(bullet)

    def update(self, enemies):
        for bullet in self.bullets:
            y = bullet.vCenter.y - 10
            bullet.setY(y)
            bullet.draw()

            for enemy in enemies: 
                if enemy.alive == True:
                    enemy.target(bullet)

    def draw(self):
        self.shape.draw()
