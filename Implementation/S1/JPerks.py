import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")

clock = pygame.time.Clock()
#img = pygame.image.load("Atari Combat Blue Tank.png").convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("Atari Combat Blue Tank.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveRight(self, pixels):
        self.rect.x += pixels
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    def moveForward(self, pixels):
        self.rect.y -= pixels
    def moveBack(self, pixels):
        self.rect.y += pixels


player1 = Player((0, 0, 255), 50, 275, 40, 40)

run = True
while run:

    screen.fill((34, 139, 34))
    screen.blit(player1.image, (player1.rect.x, player1.rect.y))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1.moveForward(1)
    if key[pygame.K_s]:
        player1.moveBack(1)
    if key[pygame.K_a]:
        player1.moveLeft(1)
        player1.image = pygame.transform.rotate(player1.image, 1)
    if key[pygame.K_d]:
        player1.moveRight(1)
        player1.image = pygame.transform.rotate(player1.image, -1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(120)

pygame.quit()
