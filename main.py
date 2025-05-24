import pygame,sys,random
from pygame.math import Vector2

# TODO - transform the turtle snake logic to pygame snake logic

class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            body_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(155,15,155),body_rect)
class Food():
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y *cell_size,cell_size,cell_size)#add int() if there is an errror here
        pygame.draw.rect(screen,(44,44,44),fruit_rect)
# clock limits how fast our loop runs
# Going over the pygame documentation

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()

fruit = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((111, 148, 118))

    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
# max 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()