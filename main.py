import pygame,sys


pygame.init()
# Going over the pygame documentation
screen = pygame.display.set_mode((1280, 720))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            sys.exit()
    pygame.display.update()