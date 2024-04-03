import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

redScore = 0
blueScore = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")

font = pygame.font.Font('PressStart2P-vaV7.ttf', 38)

blueText = font.render(str(blueScore), True, (0, 0, 255))
blueTextRect = blueText.get_rect()
blueTextRect.center = (SCREEN_WIDTH/3, SCREEN_HEIGHT/20)

redText = font.render(str(redScore), True, (255, 0, 0))
redTextRect = redText.get_rect()
redTextRect.center = ((SCREEN_WIDTH/3 * 2), SCREEN_HEIGHT/20)

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.sprites = images
        self.index = 0
        self.image = self.sprites[self.index]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, index):
        self.index = index

        if self.index >= len(self.sprites):
            self.index = 0

        self.image = self.sprites[self.index]

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels):
        self.rect.y -= pixels

    def moveBack(self, pixels):
        self.rect.y += pixels


BlueTankImages = [pygame.image.load("Blue Tank FaceRight.png").convert_alpha(),
                  pygame.image.load("Blue Tank FaceTop.png").convert_alpha(),
                  pygame.image.load("Blue Tank FaceLeft.png").convert_alpha(),
                  pygame.image.load("Blue Tank FaceBot.png").convert_alpha()]

RedTankImages = [pygame.image.load("Red Tank FaceLeft.png").convert_alpha(),
                 pygame.image.load("Red Tank FaceTop.png").convert_alpha(),
                 pygame.image.load("Red Tank FaceRight.png").convert_alpha(),
                 pygame.image.load("Red Tank FaceBot.png").convert_alpha()]

player1 = Player(BlueTankImages, 50, 275)
player2 = Player(RedTankImages, 700, 275)

run = True
while run:

    screen.fill((34, 139, 34))
    screen.blit(player1.image, (player1.rect.x, player1.rect.y))
    screen.blit(player2.image, (player2.rect.x, player2.rect.y))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT/10))
    screen.blit(blueText, blueTextRect)
    screen.blit(redText, redTextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1.moveForward(1)
        player1.update(1)
        player1.image = pygame.transform.scale(player1.image, (50, 50))
    elif key[pygame.K_s]:
        player1.moveBack(1)
        player1.update(3)
        player1.image = pygame.transform.scale(player1.image, (50, 50))
    elif key[pygame.K_a]:
        player1.moveLeft(1)
        player1.update(2)
        player1.image = pygame.transform.scale(player1.image, (50, 50))
    elif key[pygame.K_d]:
        player1.moveRight(1)
        player1.update(0)
        player1.image = pygame.transform.scale(player1.image, (50, 50))

    if key[pygame.K_SPACE]:
        player1.image = pygame.transform.rotate(player1.image, 2)

    if key[pygame.K_UP]:
        player2.moveForward(1)
        player2.update(1)
        player2.image = pygame.transform.scale(player2.image, (50, 50))
    elif key[pygame.K_DOWN]:
        player2.moveBack(1)
        player2.update(3)
        player2.image = pygame.transform.scale(player2.image, (50, 50))
    elif key[pygame.K_RIGHT]:
        player2.moveRight(1)
        player2.update(2)
        player2.image = pygame.transform.scale(player2.image, (50, 50))
    elif key[pygame.K_LEFT]:
        player2.moveLeft(1)
        player2.update(0)
        player2.image = pygame.transform.scale(player2.image, (50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(120)

pygame.quit()
