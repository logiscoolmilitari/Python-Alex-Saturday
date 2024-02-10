import pygame
x = 50
y = 250
q = 700
z = 280
FPS = 240
VEL = 15
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
gameing = True
while gameing:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= VEL
            if event.key == pygame.K_s:
                y += VEL
            if event.key == pygame.K_a:
                x -= VEL
            if event.key == pygame.K_d:
                x += VEL
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                z -= VEL
            if event.key == pygame.K_DOWN:
                z += VEL
            if event.key == pygame.K_LEFT:
                q -= VEL
            if event.key == pygame.K_RIGHT:
                q += VEL

    screen.fill((163, 170, 229))
    pygame.draw.rect(screen, (255, 0, 0 ), (x, y, 75, 75))
    pygame.draw.circle(screen, (85, 255, 0 ), (q, z), 45)
    pygame.draw.line(screen, (255, 255, 255), (50, 60),(750, 60), 75)
    pygame.draw.line(screen, (255, 255, 255), (100, 140), (700, 140), 75)
    pygame.display.update()




