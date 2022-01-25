import pygame
import pickle
import os
from network import Network
from player import Player
from ball import Ball
pygame.font.init()

#color
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0, 255, 0)

#size of width and height
width = 700
height = 500
size = (width,height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong Multiplayer")

#change split the tuples
def readPosition(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5])

#make it to tuples
def makePosition(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3]) + "," + str(tup[4]) + "," + str(tup[5])



#Main function
def main():
    run = True 
    n = Network()

    #initialize score
    scoreA = 0
    scoreB = 0

    # intialize for ball,player1 and player2 for colour, width of paddle and height of paddle
    ball = Ball(black, 10, 10)
    p = Player(blue, 10, 100)
    p2 = Player(red, 10, 100)

    startPos = readPosition(n.getP())

    # insert position player 1 paddle and ball position
    p.rect.x = startPos[0]
    p.rect.y = startPos[1]
    ball.rect.x = startPos[2]
    ball.rect.y = startPos[3]
    scoreA = startPos[4]
    scoreB = startPos[5]

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2Pos = readPosition(n.send(makePosition((p.rect.x,p.rect.y,ball.rect.x,ball.rect.y, scoreA, scoreB))))

        # insert position player 1 paddle and ball position
        p2.rect.x = p2Pos[0]
        p2.rect.y = p2Pos[1]
        ball.rect.x = p2Pos[2]
        ball.rect.y = p2Pos[3]
        scoreA = p2Pos[4]
        scoreB = p2Pos[5]



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        #initilize spirte group
        all_sprites_list = pygame.sprite.Group()

        #add ball, player1 and player2  to sprite group
        all_sprites_list.add(p)
        all_sprites_list.add(p2)
        all_sprites_list.add(ball)

        #player 1 control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p.up(5)
        if keys[pygame.K_DOWN]:
            p.down(5)
        #player 2 control
        if keys[pygame.K_UP]:
            p2.up(5)
        if keys[pygame.K_DOWN]:
            p2.down(5)

        #update sprites lis
        all_sprites_list.update()

        # Check if the ball bouncing in the wall
        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # Detect collisions
        if pygame.sprite.collide_mask(ball, p) or pygame.sprite.collide_mask(ball, p2):
            ball.bounce()


        screen.fill(white)

        # Draw the net
        pygame.draw.line(screen, black, [349, 0], [349, 500], 5)

        #draw the sprites
        all_sprites_list.draw(screen)

        #font scoreboard
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, black)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, black)
        screen.blit(text, (420, 10))

        #decide winner
        font = pygame.font.SysFont("comicsans", 90)
        if scoreA == 21:
            text = font.render("You Won!", 1, (255, 0, 0))
        elif scoreB == 21:
            text = font.render("You Lost...", 1, (255, 0, 0))




        pygame.display.flip()



main()