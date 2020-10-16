"""
Created on Mon Sep 28 22:42:55 2020
@author: mockingbird01001
"""

import pygame, sys
from  pygame.locals import *
from sys import exit
from numpy.random import randint

# quit function
def quitter():
    pygame.display.quit()
    pygame.quit()
    #ssys.exit()
    exit()
    
while True:
    # direction du snake
    up, down, right, left = 1, 2, 3, 4
    # taille du bloc
    step = 20
    block = [step, step]

    x=randint(1,20)
    y=randint(2,22)
    applexy=[]
    snakexy=[int(x*20),int(y*20)]
    snakelist=[[x*20,y*20],[(x-20)*20,(y*20)]]
    
    # initialisation 
    apple=0
    dead=0
    score=0
    
    # direction au moment du start
    direction=right

    #initialisation & taille de la fenetre
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    
    # mise en place du titre de la fenetre
    caption = pygame.display.set_caption("My Snake")
    
    # logo de la fenetre
    pygame.display.set_icon(pygame.image.load("snake.png"))
    
    """ --- Menu Home ---"""
    #chargement de la font1
    f = pygame.font.SysFont("comicsansms", 50)
    text1=f.render("Hungry Snake", True, (0, 255, 0))
    clock=pygame.time.Clock()
    
    # chargement de la font2
    start=pygame.font.SysFont("comicsansms", 30)
    text2=start.render("Press s to start", True, (0, 255, 0))
    text3=start.render("Press q to quit", True, (0, 255, 0))
    
    # Sequence de test pour le snake 
    s = [[300,200],[280,200],[260,200],[240,200],[220,200],[200,200],[180,200],
         [180,220],[160,220],[140,220],[120,220],[120,240],[100,240]]
         
    # position de la pomme dans le test
    a = [100,240]

    # affichage de la pomme
    pygame.draw.rect(screen,(255, 0, 0),Rect(a, block), 0)
    
    # affichage du texte
    screen.blit(text1,(60, 60))
    screen.blit(text2,(300, 300))
    screen.blit(text3,(300, 350))
    
    # affichage du snake
    for i in s:
        pygame.draw.rect(screen, (0, 255, 0),Rect(i, block), 0)
        pygame.display.flip()
        clock.tick(10)
    pygame.display.flip()


    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                quitter()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_q:
                    quitter()
        pressed=pygame.key.get_pressed()
        if pressed[K_q]:
            pygame.quit()
            quitter()
        if pressed[K_s]:
            break


    while not dead:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                quitter()
        # pour recuperer la touche entree
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and direction != right:
            direction = left
        elif pressed[K_RIGHT] and direction != left:
            direction = right
        elif pressed[K_UP] and direction != down:
            direction = up
        elif pressed[K_DOWN] and direction != up:
            direction = down
        if direction == right:
            snakexy[0] = snakexy[0] + step
            if snakexy[0] > 620:
                dead = 1
        elif direction == left:
            snakexy[0] = snakexy[0] - step
            if snakexy[0] < 20:
                dead=1
        elif direction == up:
            snakexy[1] = snakexy[1] - step
            if snakexy[1] < 20:
                dead = 1
        elif direction == down:
            snakexy[1] = snakexy[1] + step
            if snakexy[1] > 460:
                dead = 1
        if snakelist.count(snakexy) > 0:
            dead = 1
        if apple==0:
            x1 = randint(1, 31)
            y1 = randint(2, 22)
            applexy = [int(x1 * step), int(y1 * step)]
            apple = 1
        snakelist.insert(0, list(snakexy))
                
        if snakexy[0] == applexy[0] and snakexy[1] == applexy[1]:
            apple = 0
            score = score + 1
        else:
            snakelist.pop()

        screen.fill((0, 0, 0))
        scr = pygame.font.SysFont("comicsansms", 20)
        text4 = scr.render("Score : %d"%score, True, (0, 255 ,0))
        screen.blit(text4,(500, 10))
        pygame.draw.rect(screen, (255, 0, 0),Rect(applexy, block), 0)
        for i in snakelist:
            pygame.draw.rect(screen,(0,255,0),Rect(i,block))
        pygame.display.flip()
        clock.tick(10)

    if dead == 1:
        screen.fill((0, 0, 0))
        over = pygame.font.SysFont("comicsansms", 40)
        text5 = over.render("GAME OVER", True, (0, 255, 0))
        screen.blit(text5, (50, 50))
        screen.blit(text4, (200, 200))
        pygame.display.flip()

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    quitter()
            pressed = pygame.key.get_pressed()
            if pressed[K_q]:
                quitter()
            if pressed[K_s]:
                break
                                    
                                    
                                    

                                    
                                    
















