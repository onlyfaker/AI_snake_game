import pygame,sys

# clock limits how fast our loop runs
# Going over the pygame documentation

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()


test_surface = pygame.Surface((100,100))#size
# test_rect = pygame.Rect(150,200,100,100) #creating a new rect
test_old_rect = test_surface.get_rect(center = (200,200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((100,23,87))
    screen.blit(test_surface,test_old_rect)#position

    # pygame.draw.ellipse(surface=screen,color = "white",rect=test_rect)# drawing with new rect

# pygame.display.flip()	- for larger screen update
    pygame.display.update()
    clock.tick(60)#max 60 fps

pygame.quit()
sys.exit()