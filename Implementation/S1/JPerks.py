import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((375, 250, 50, 50))

run = True
while run:

    screen.fill((34, 139, 34))

    pygame.draw.rect(screen, (0, 0, 255), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -1)
    if key[pygame.K_s]:
        player.move_ip(0, 1)
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    if key[pygame.K_d]:
        player.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
