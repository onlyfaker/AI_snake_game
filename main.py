import pygame,sys
from pygame.math import Vector2

# TODO - transform the turtle snake logic to pygame snake logic
class Food():
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y *cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(44,44,44),fruit_rect)
# clock limits how fast our loop runs
# Going over the pygame documentation

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()

fruit = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((111, 148, 118))
    fruit.draw_fruit()
    pygame.display.update()
# max 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()