import pygame
from random import randint

white = (255, 255, 255)


class Ball(pygame.sprite.Sprite):

    #initialize image for ball
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    #function to update position of ball
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    #function for to ball to bounce in the screen
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)