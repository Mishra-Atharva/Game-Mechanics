import pygame

player_1 = pygame.image.load("player_1.png")
player_2 = pygame.image.load("player_2.png")
player_3 = pygame.image.load("player_3.png")
player_walk = [player_1, player_2, player_3]
attack_1 = pygame.image.load('attack1.png')
attack_2 = pygame.image.load('attack2.png')
player_index = 0
player_image = player_walk[player_index]
player_rect = player_image.get_rect(midbottom = (150, 150))

def key(key, move, direction):
    global player_index, player_image, player_rect

    if key == 'right':
        player_rect.left += 1
        
    if key == 'left':
        player_rect.right -= 1
        
    if key == 'down':
        player_rect.bottom += 1
    
    if key == 'up':
        player_rect.top -= 1
    
    if key == 'attack':
        player_image = attack_2 
    
    if key == 'stop':
        player_index = 0
        player_image = player_walk[player_index]

    if player_index != 2 and not(player_index > 2) and move:
        player_index += 0.1
        player_image = player_walk[int(player_index)]
    else:
        player_index = 0
        player_image = player_walk[player_index]   
    
    if direction == 'Left':
        player_image = pygame.transform.flip(player_image, True, False)
    
    elif direction == 'Right': 
        player_image = pygame.transform.flip(player_image, False, False)

    return player_image
