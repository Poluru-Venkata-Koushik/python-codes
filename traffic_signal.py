import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((102,246,210))
    pygame.draw.circle(screen,(255,0,0),(250,250),100)
    pygame.display.flip()

pygame.quit()