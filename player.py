import pygame
white = (255,255,255)

class Player(pygame.sprite.Sprite):

    # initialize image for paddle
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    #function for paddle move up
    def up(self, vel):

        self.rect.y -= vel
        if self.rect.y < 0:
            self.rect.y = 0

    # function for paddle move down
    def down(self, vel):
        self.rect.y += vel
        if self.rect.y > 400:
            self.rect.y = 400
