import pygame,sys,random
from pygame.math import Vector2

# TODO/done - transform the turtle snake logic to pygame snake logic
# TODO - snake graphics!

class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.next_direction = Vector2(1, 0)
        self.is_turning = False  # Flag to prevent multiple turns per move cycle
        self.new_block = False

        self.head_up = pygame.image.load('snake_graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake_graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake_graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake_graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('snake_graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake_graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake_graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake_graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('snake_graphics/body_vertical.png').convert_alpha()
        self.body_horizontal= pygame.image.load('snake_graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('snake_graphics/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('snake_graphics/body_topleft.png').convert_alpha()
        self.body_bl = pygame.image.load('snake_graphics/body_bottomleft.png').convert_alpha()
        self.body_br = pygame.image.load('snake_graphics/body_bottomright.png').convert_alpha()
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index - 1]- block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_br,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_tl,block_rect)

    def update_head_graphics(self):
        head_turn_point = self.body[1] - self.body[0]
        if head_turn_point == Vector2(1,0): self.head = self.head_left
        elif head_turn_point == Vector2(-1,0): self.head = self.head_right
        elif head_turn_point == Vector2(0,1): self.head = self.head_up
        elif head_turn_point == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_turn_point = self.body[-2] - self.body[-1]
        if tail_turn_point == Vector2(1,0): self.tail = self.tail_left
        elif tail_turn_point == Vector2(-1,0): self.tail = self.tail_right
        elif tail_turn_point == Vector2(0,1): self.tail = self.tail_up
        elif tail_turn_point == Vector2(0,-1): self.tail = self.tail_down
    def move_snake(self):
        if self.direction != self.next_direction:
            self.direction = self.next_direction
        if self.new_block == True:
            body_copy = self.body[:]  # slicing
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]#slicing
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body = body_copy
        self.is_turning=False
    def add_block(self):
        self.new_block = True

    def change_direction_up(self):
        # Only change direction if not going in the opposite direction and not already turning
        if self.direction.y != 1 and not self.is_turning:
            self.next_direction = Vector2(0, -1)
            self.is_turning = True

    def change_direction_down(self):
        if self.direction.y != -1 and not self.is_turning:
            self.next_direction = Vector2(0, 1)
            self.is_turning = True

    def change_direction_left(self):
        if self.direction.x != 1 and not self.is_turning:
            self.next_direction = Vector2(-1, 0)
            self.is_turning = True

    def change_direction_right(self):
        if self.direction.x != -1 and not self.is_turning:
            self.next_direction = Vector2(1, 0)
            self.is_turning = True


class Food():
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y *cell_size,cell_size,cell_size)#add int() if there is an errror here
        screen.blit(berry,fruit_rect)
        #pygame.draw.rect(screen,(44,44,44),fruit_rect)


    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
# clock limits how fast our loop runs
# Going over the pygame documentation
class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Food()

    def update(self):
        self.snake.move_snake()
        self.check_food_collision()
        self.check_collision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_food_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_collision(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number :
            self.game_over()

        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
                #chechk for snake collsion with itself
    def game_over(self):
        running = False
        pygame.quit()
        sys.exit()
    def draw_grass(self):
        grass_color = (80, 219, 33)
        for row in range(cell_number):
            if row % 2==0:
                for col in range(cell_number):
                    if col%2==0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()
berry = pygame.image.load('graphics/apple.png').convert_alpha()
berry = pygame.transform.scale(berry, (cell_size, cell_size))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = Main()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.change_direction_up()
            if event.key == pygame.K_DOWN:
                main_game.snake.change_direction_down()
            if event.key == pygame.K_LEFT:
                main_game.snake.change_direction_left()
            if event.key == pygame.K_RIGHT:
                main_game.snake.change_direction_right()

    screen.fill((80, 224, 32))
    main_game.draw_elements()
    pygame.display.update()
# max 60 fps
    clock.tick(60)

pygame.quit()
sys.exit()