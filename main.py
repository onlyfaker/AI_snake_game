import pygame,sys,random
from pygame.math import Vector2

# TODO - transform the turtle snake logic to pygame snake logic

class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            body_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(155,15,155),body_rect)

    def move_snake(self):
        body_copy = self.body[:-1]#slicing
        body_copy.insert(0,body_copy[0]+ self.direction)
        self.body = body_copy
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
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key ==pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key ==pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key ==pygame.K_RIGHT:
                snake.direction = Vector2(1,0)

    screen.fill((111, 148, 118))

    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
# max 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()