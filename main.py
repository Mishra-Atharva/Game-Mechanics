import pygame
from user import *

#controls
# Movement = W A S D
# Attack = Left Control Key

pygame.init()
pygame.event.pump()

alive = True
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('First Game')
fps = pygame.time.Clock()

image = player_image
rect = player_rect
cooldown = False
direction = 'Right'

while alive:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    

    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_d]:
        image = key('right', True, 'Right')
        direction = 'Right'

    if key_press[pygame.K_a]:
        image = key('left', True, 'Left')
        direction = 'Left' 

    if key_press[pygame.K_s]:
        image = key('down', True, direction)

    if key_press[pygame.K_w]:
        image = key('up', True, direction)      

    if key_press[pygame.K_LCTRL]:
        image = attack_2
        if direction == 'Left':
            image = pygame.transform.flip(image, True, False)
        
    if event.type == pygame.KEYUP:
        image = key('stop', False, direction)

    screen.fill('green')
    screen.blit(image, rect)
    pygame.display.update()
    fps.tick(60)