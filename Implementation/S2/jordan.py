# used tutorial from https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Tank Game")
    screen = pygame.display.set_mode((840, 630))

    # define vars
    bgColor = (255, 255, 255)
    circColor = (255, 0, 0)
    circPos = (420, 315)
    circRad = 50

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(bgColor)
        pygame.draw.circle(screen, circColor, circPos, circRad)
        pygame.display.flip()


if __name__ == "__main__":
    main()
