import pygame,sys

# clock limits how fast our loop runs
# Going over the pygame documentation

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()


test_surface = pygame.Surface((100,200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((100,23,87))
    screen.blit(test_surface,(200,150))
# pygame.display.flip()	- for larger screen update
    pygame.display.update()
    clock.tick(60)#max 60 fps

pygame.quit()
sys.exit()