import pygame,sys
# TODO - transform the turtle snake logic to pygame snake lodgic

# clock limits how fast our loop runs
# Going over the pygame documentation

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

#size
test_surface = pygame.Surface((100,100))

#taking rect(position) from surface, and setting its new position
test_rect = test_surface.get_rect(center = (200,200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((111, 148, 118))

    pygame.display.update()
# max 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()