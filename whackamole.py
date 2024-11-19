import pygame
import random

pygame.init()

SIZE = 32
ROWS = 20
COLUMNS = 16
COLOR = (245, 152, 66)
BG_COLOR = (255, 255, 245)

def main():
    screen = pygame.display.set_mode((ROWS * SIZE, COLUMNS * SIZE)) #

    try:

        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft = (0,0))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))

        #screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #checks for mouse clicking mole
                    if mole_rect.collidepoint(event.pos):
                        new_x = random.randrange(0,ROWS) * SIZE
                        new_y = random.randrange(0, COLUMNS) * SIZE
                        mole_rect.topleft = (new_x, new_y)
            screen.fill("light green")


            # grid drawn
            for x in range(0, ROWS * SIZE, SIZE):
                pygame.draw.line(screen, COLOR, (x, 0), (x, COLUMNS * SIZE))
            for y in range(0, COLUMNS * SIZE, SIZE):
                pygame.draw.line(screen, COLOR, (0, y), (ROWS * SIZE, y))

            #draw mole
            screen.blit(mole_image, mole_rect)

            #display update
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
