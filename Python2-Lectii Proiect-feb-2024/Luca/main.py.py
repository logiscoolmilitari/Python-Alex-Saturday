import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

GAME = True
CLOCK = pygame.time.Clock()
FPS = 120
VEL = 10d
x = 250
y = 250
while GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= VEL
            if event.key == pygame.K_s:
                y += VEL
            if event.key == pygame.K_d:
                x += VEL
            if event.key == pygame.K_a:
                x -= VEL

    WINDOW.fill((255, 255, 255))

    pygame.draw.rect(WINDOW, (50, 255, 110), (x, y, 50, 100))
    pygame.display.update()


pygame.quit()

