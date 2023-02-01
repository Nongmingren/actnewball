import pygame

pygame.init()

goforb = 0
aim = True
while aim == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                goforb + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.flip()
                aim = False

if goforb == 1:
    print('kuk')

pygame.display.flip()