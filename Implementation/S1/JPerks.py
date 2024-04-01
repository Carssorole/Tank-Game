import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

player = pygame.Rect((375, 250, 40, 40))
wall = pygame.Rect((393, 270, 5, 40))

run = True
while run:

    clock.tick(120)
    screen.fill((34, 139, 34))

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (0, 0, 255), wall)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -1)
        wall.move_ip(0, -1)
    if key[pygame.K_s]:
        player.move_ip(0, 1)
        wall.move_ip(0, 1)
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
        wall.move_ip(-1, 0)
    if key[pygame.K_d]:
        player.move_ip(1, 0)
        wall.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
