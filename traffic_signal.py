import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

Screen_Width=1000
Screen_Height=500

screen=pygame.display.set_mode((Screen_Width,Screen_Height))

running=True
while running:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running=False

    screen.fill((255,255,255))
    surf=pygame.Surface((50,50))
    surf.fill((0,0,0))
    rect=surf.get_rect()
    surf_center = ((Screen_Width - surf.get_width()) / 2,(Screen_Height - surf.get_height()) / 2)
    screen.blit(surf,surf_center)

    pygame.display.flip()