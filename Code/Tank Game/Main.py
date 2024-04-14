import pygame
import random
from pytmx.util_pygame import load_pygame
from player import Player
import Wall
import Menu
import bullet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 666
SCOREBOARD_HEIGHT = 66

redScore = 0
blueScore = 0
fireIndex = 0
trajectoryVar = 0

# Sets screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")
# Below sets arcade style font and color codes each player's score
font = pygame.font.Font('../Assets/PressStart2P-vaV7.ttf', 38)

blueText = font.render(str(blueScore), True, (63, 196, 255))
blueTextRect = blueText.get_rect()
blueTextRect.center = (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 20)

redText = font.render(str(redScore), True, (255, 0, 0))
redTextRect = redText.get_rect()
redTextRect.center = ((SCREEN_WIDTH / 3 * 2), SCREEN_HEIGHT / 20)

gameText = font.render("Tank Game", True, (191, 0, 255))
gameTextRect = gameText.get_rect()
# Plays random track from musicList and loops it
musicList = ["../Assets/Chip Suey.wav", "../Assets/Paper Planes.wav", "../Assets/For What.wav",
             "../Assets/Centuries.wav", "../Assets/Blue.wav"]
pygame.mixer.music.load(musicList[random.randint(0, len(musicList) - 1)])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

clock = pygame.time.Clock()
tmxdata = load_pygame('tankmap1.tmx')

BlueTankImages = [pygame.image.load("../Assets/Blue Tank FaceRight.png").convert_alpha(),
                  pygame.image.load("../Assets/Blue Tank FaceTop.png").convert_alpha(),
                  pygame.image.load("../Assets/Blue Tank FaceLeft.png").convert_alpha(),
                  pygame.image.load("../Assets/Blue Tank FaceBot.png").convert_alpha()]

RedTankImages = [pygame.image.load("../Assets/Red Tank FaceLeft.png").convert_alpha(),
                 pygame.image.load("../Assets/Red Tank FaceTop.png").convert_alpha(),
                 pygame.image.load("../Assets/Red Tank FaceRight.png").convert_alpha(),
                 pygame.image.load("../Assets/Red Tank FaceBot.png").convert_alpha()]

FireImages = [pygame.image.load("../Assets/Fire Frame1.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame2.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame3.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame4.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame5.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame6.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame7.png").convert_alpha(),
              pygame.image.load("../Assets/Fire Frame8.png").convert_alpha()]

player1 = Player(BlueTankImages, 50, SCREEN_HEIGHT / 2 - SCOREBOARD_HEIGHT + 10)
player2 = Player(RedTankImages, SCREEN_WIDTH - 100, SCREEN_HEIGHT / 2 - SCOREBOARD_HEIGHT + 10)

fireSprite = Player(FireImages, -300, (SCREEN_HEIGHT / 20 - (SCOREBOARD_HEIGHT + 28)))
player1bullet = bullet.Bullet(player1.rect.x + 40, player1.rect.y + 2000, (0, 0, 0))
player2bullet = bullet.Bullet(player2.rect.x + 0, player2.rect.y + 2000, (0, 255, 0))


run = True
menu = True
game_over = False
instructions = False

while run:
    if menu:
        Menu.draw_start_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    instructions = True
                elif event.key == pygame.K_x:
                    run = False
                    break

        pygame.display.update()

    elif instructions:
        Menu.draw_instructions_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    instructions = False

    elif game_over:
        Menu.draw_game_over(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    run = True
                elif event.key == pygame.K_x:
                    run = False
                    break

    else:
        screen.fill((34, 139, 34))
        Wall.wall_tiles(screen, tmxdata, SCREEN_HEIGHT, SCOREBOARD_HEIGHT)

        screen.blit(player1.image, (player1.rect.x, player1.rect.y))
        screen.blit(player2.image, (player2.rect.x, player2.rect.y))
        # Below controls the scoreboard and animations
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 10))
        screen.blit(fireSprite.image, fireSprite.rect)
        screen.blit(gameText, gameTextRect)
        screen.blit(blueText, blueTextRect)
        screen.blit(redText, redTextRect)

        gameTextRect.center = (-(fireSprite.rect.x + 1000), SCREEN_HEIGHT / 20)

        fireSprite.updateJumbotron()
        fireSprite.image = pygame.transform.scale(fireSprite.image, (160, 60))

        if fireSprite.rect.x <= SCREEN_WIDTH - 80 and fireSprite.elapsed == 0 or 5:
            fireSprite.moveRight(1)
        if fireSprite.rect.x >= SCREEN_WIDTH + 80:
            fireSprite.rect.x = -2500
        # Below controls key bindings
        key = pygame.key.get_pressed()
        # trajectoryVar looks useless but the dang thing won't work without it.
        if key[pygame.K_v] and player1bullet.cooldown:
            if player1.index == 0:
                player1bullet.direction = 0
                trajectoryVar = player1bullet.direction
                player1bullet = bullet.Bullet(player1.rect.x + 40, player1.rect.y + 20, (0, 0, 255))
            elif player1.index == 1:
                player1bullet.direction = 1
                trajectoryVar = player1bullet.direction
                player1bullet = bullet.Bullet(player1.rect.x + 20, player1.rect.y + 0, (0, 0, 255))
            elif player1.index == 2:
                player1bullet.direction = 2
                trajectoryVar = player1bullet.direction
                player1bullet = bullet.Bullet(player1.rect.x + 0, player1.rect.y + 20, (0, 0, 255))
            elif player1.index == 3:
                player1bullet.direction = 3
                trajectoryVar = player1bullet.direction
                player1bullet = bullet.Bullet(player1.rect.x + 20, player1.rect.y + 40, (0, 0, 255))

# Below controls player1's bullet direction and cooldown
        if player1bullet.time < 300:

            player1bullet.direction = trajectoryVar

            if player1bullet.direction == 0:
                player1bullet.x_pos += 3
                player1bullet.cooldown = False
                pygame.draw.circle(screen, player1bullet.color, (player1bullet.x_pos, player1bullet.y_pos), player1bullet.radius)
            elif player1bullet.direction == 1:
                player1bullet.y_pos -= 3
                player1bullet.cooldown = False
                pygame.draw.circle(screen, player1bullet.color, (player1bullet.x_pos, player1bullet.y_pos), player1bullet.radius)
            elif player1bullet.direction == 2:
                player1bullet.x_pos -= 3
                player1bullet.cooldown = False
                pygame.draw.circle(screen, player1bullet.color, (player1bullet.x_pos, player1bullet.y_pos), player1bullet.radius)
            elif player1bullet.direction == 3:
                player1bullet.y_pos += 3
                player1bullet.cooldown = False
                pygame.draw.circle(screen, player1bullet.color, (player1bullet.x_pos, player1bullet.y_pos), player1bullet.radius)

        if player1bullet.time >= 300:
            player1bullet.cooldown = True
        # Controls player2's hit box dimensions and hit registry
        if player2.rect.x <= player1bullet.x_pos <= player2.rect.x + 40 \
                and player2.rect.y <= player1bullet.y_pos <= player2.rect.y + 40:

            blueScore += 1
            blueText = font.render(str(blueScore), True, (63, 196, 255))
            blueTextRect = blueText.get_rect()
            blueTextRect.center = (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 20)
            player1bullet = bullet.Bullet(player1.rect.x + 40, player1.rect.y + 2000, (0, 0, 0))
            # Controls player2's respawn
            spawnPointX = [50, 50, 50, SCREEN_WIDTH - 100, SCREEN_WIDTH - 100, SCREEN_WIDTH - 100,
                           SCREEN_WIDTH / 2 - 15, SCREEN_WIDTH / 2 - 15]
            spawnPointY = [SCREEN_HEIGHT / 2 + 10, SCREEN_HEIGHT - SCOREBOARD_HEIGHT, SCOREBOARD_HEIGHT + 25,
                           SCREEN_HEIGHT / 2 + 10, SCREEN_HEIGHT - SCOREBOARD_HEIGHT, SCOREBOARD_HEIGHT + 25,
                           SCREEN_HEIGHT / 2 + 160, SCREEN_HEIGHT / 2 - 140]
            setSpawn = random.randint(0, 7)
            player2.rect.x = spawnPointX[setSpawn]
            player2.rect.y = spawnPointY[setSpawn]

        player1bullet.time += 1

        if key[pygame.K_m] and player2bullet.cooldown:
            if player2.index == 0:
                player2bullet.direction = 0
                trajectoryVar = player2bullet.direction
                player2bullet = bullet.Bullet(player2.rect.x + 0, player2.rect.y + 20, (255, 0, 0))
            elif player2.index == 1:
                player2bullet.direction = 1
                trajectoryVar = player2bullet.direction
                player2bullet = bullet.Bullet(player2.rect.x + 20, player2.rect.y + 0, (255, 0, 0))
            elif player2.index == 2:
                player2bullet.direction = 2
                trajectoryVar = player2bullet.direction
                player2bullet = bullet.Bullet(player2.rect.x + 40, player2.rect.y + 20, (255, 0, 0))
            elif player2.index == 3:
                player2bullet.direction = 3
                trajectoryVar = player2bullet.direction
                player2bullet = bullet.Bullet(player2.rect.x + 20, player2.rect.y + 40, (255, 0, 0))

        # Below controls player2's bullet direction and cooldown
        if player2bullet.time < 300:

            player2bullet.direction = trajectoryVar

            if player2bullet.direction == 0:
                player2bullet.x_pos -= 3
                player2bullet.cooldown = False
                pygame.draw.circle(screen, player2bullet.color, (player2bullet.x_pos, player2bullet.y_pos),
                                   player2bullet.radius)
            elif player2bullet.direction == 1:
                player2bullet.y_pos -= 3
                player2bullet.cooldown = False
                pygame.draw.circle(screen, player2bullet.color, (player2bullet.x_pos, player2bullet.y_pos),
                                   player2bullet.radius)
            elif player2bullet.direction == 2:
                player2bullet.x_pos += 3
                player2bullet.cooldown = False
                pygame.draw.circle(screen, player2bullet.color, (player2bullet.x_pos, player2bullet.y_pos),
                                   player2bullet.radius)
            elif player2bullet.direction == 3:
                player2bullet.y_pos += 3
                player2bullet.cooldown = False
                pygame.draw.circle(screen, player2bullet.color, (player2bullet.x_pos, player2bullet.y_pos),
                                   player2bullet.radius)

        if player2bullet.time >= 300:
            player2bullet.cooldown = True
        # Controls player1's hit box dimensions and hit registry
        if player1.rect.x <= player2bullet.x_pos <= player1.rect.x + 40 \
                and player1.rect.y <= player2bullet.y_pos <= player1.rect.y + 40:

            redScore += 1
            redText = font.render(str(redScore), True, (255, 0, 0))
            redTextRect = redText.get_rect()
            redTextRect.center = ((SCREEN_WIDTH / 3 * 2), SCREEN_HEIGHT / 20)
            player2bullet = bullet.Bullet(player1.rect.x + 0, player1.rect.y + 2000, (0, 0, 0))
        # Controls player1's respawn
            spawnPointX = [50, 50, 50, SCREEN_WIDTH - 100, SCREEN_WIDTH - 100, SCREEN_WIDTH - 100,
                           SCREEN_WIDTH / 2 - 15, SCREEN_WIDTH / 2 - 15]
            spawnPointY = [SCREEN_HEIGHT / 2 + 10, SCREEN_HEIGHT - SCOREBOARD_HEIGHT, SCOREBOARD_HEIGHT + 25,
                           SCREEN_HEIGHT / 2 + 10, SCREEN_HEIGHT - SCOREBOARD_HEIGHT, SCOREBOARD_HEIGHT + 25,
                           SCREEN_HEIGHT / 2 + 160, SCREEN_HEIGHT / 2 - 140]
            setSpawn = random.randint(0, 7)
            player1.rect.x = spawnPointX[setSpawn]
            player1.rect.y = spawnPointY[setSpawn]

        player2bullet.time += 1

        if key[pygame.K_w]:
            if Wall.can_move_to(tmxdata, player1.rect, 0, -1, SCOREBOARD_HEIGHT):
                player1.moveForward(1)
            if player1.detectCollision(player2):
                player1.moveBack(1)
            player1.update(1)
            player1.image = pygame.transform.scale(player1.image, (40, 40))
        elif key[pygame.K_s]:
            if Wall.can_move_to(tmxdata, player1.rect, 0, 1, SCOREBOARD_HEIGHT):
                player1.moveBack(1)
            if player1.detectCollision(player2):
                player1.moveForward(1)
            player1.update(3)
            player1.image = pygame.transform.scale(player1.image, (40, 40))
        elif key[pygame.K_a]:
            if Wall.can_move_to(tmxdata, player1.rect, -1, 0, SCOREBOARD_HEIGHT):
                player1.moveLeft(1)
            if player1.detectCollision(player2):
                player1.moveRight(1)
            player1.update(2)
            player1.image = pygame.transform.scale(player1.image, (40, 40))
        elif key[pygame.K_d]:
            if Wall.can_move_to(tmxdata, player1.rect, 1, 0, SCOREBOARD_HEIGHT):
                player1.moveRight(1)
            if player1.detectCollision(player2):
                player1.moveLeft(1)
            player1.update(0)
            player1.image = pygame.transform.scale(player1.image, (40, 40))
        # Used until other game over logic is implemented (Press 5 to end game)
        if key[pygame.K_5]:
            game_over = True

        if key[pygame.K_UP]:
            if Wall.can_move_to(tmxdata, player2.rect, 0, -1, SCOREBOARD_HEIGHT):
                player2.moveForward(1)
            if player2.detectCollision(player1):
                player2.moveBack(1)
            player2.update(1)
            player2.image = pygame.transform.scale(player2.image, (40, 40))
        elif key[pygame.K_DOWN]:
            if Wall.can_move_to(tmxdata, player2.rect, 0, 1, SCOREBOARD_HEIGHT):
                player2.moveBack(1)
            if player2.detectCollision(player1):
                player2.moveForward(1)
            player2.update(3)
            player2.image = pygame.transform.scale(player2.image, (40, 40))
        elif key[pygame.K_RIGHT]:
            if Wall.can_move_to(tmxdata, player2.rect, 1, 0, SCOREBOARD_HEIGHT):
                player2.moveRight(1)
            if player2.detectCollision(player1):
                player2.moveLeft(1)
            player2.update(2)
            player2.image = pygame.transform.scale(player2.image, (40, 40))
        elif key[pygame.K_LEFT]:
            if Wall.can_move_to(tmxdata, player2.rect, -1, 0, SCOREBOARD_HEIGHT):
                player2.moveLeft(1)
            if player2.detectCollision(player1):
                player2.moveRight(1)
            player2.update(0)
            player2.image = pygame.transform.scale(player2.image, (40, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(120)

pygame.quit()
