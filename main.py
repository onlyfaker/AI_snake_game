import pygame, sys, random, os
from pygame.math import Vector2


# TODO/done - transform the turtle snake logic to pygame snake logic
# TODO/done - snake graphics
# TODO - make my own graphics - change this at the end after AI agents...
# TODO/done - instead of game over, make the snake reset position(reset_snake method)
# TODO/done - pause snake movement until key is pressed after reset
# TODO/done - track high score with text file
# TODO - implement AI
class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)  # Start stationary
        self.next_direction = Vector2(1, 0)  # Default direction when movement starts
        self.is_turning = False  # Flag to prevent multiple turns per move cycle
        self.new_block = False
        self.moving = False  # Flag to control whether snake moves

        self.head_up = pygame.image.load('snake_graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake_graphics/head_down2.png').convert_alpha()
        self.head_right = pygame.image.load('snake_graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake_graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('snake_graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake_graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake_graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake_graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('snake_graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('snake_graphics/body_horizontal.png').convert_alpha()

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
        if self.moving:
            head_turn_point = self.body[1] - self.body[0]
        else:
            # Use next_direction when not moving to show intended direction
            head_turn_point = -self.next_direction

        if head_turn_point == Vector2(1, 0):
            self.head = self.head_left
        elif head_turn_point == Vector2(-1, 0):
            self.head = self.head_right
        elif head_turn_point == Vector2(0, 1):
            self.head = self.head_up
        elif head_turn_point == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_turn_point = self.body[-2] - self.body[-1]
        if tail_turn_point == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_turn_point == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_turn_point == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_turn_point == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        # Only move if the snake is set to moving
        if not self.moving:
            return

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

    def start_moving(self):
        # Start the snake moving and set initial direction
        self.moving = True
        self.direction = self.next_direction

    def change_direction_up(self):
        # Start moving if not already moving
        if not self.moving:
            self.next_direction = Vector2(0, -1)
            self.start_moving()
        # Only change direction if not going in the opposite direction and not already turning
        elif self.direction.y != 1 and not self.is_turning:
            self.next_direction = Vector2(0, -1)
            self.is_turning = True

    def change_direction_down(self):
        if not self.moving:
            self.next_direction = Vector2(0, 1)
            self.start_moving()
        elif self.direction.y != -1 and not self.is_turning:
            self.next_direction = Vector2(0, 1)
            self.is_turning = True

    def change_direction_left(self):
        if not self.moving:
            self.next_direction = Vector2(-1, 0)
            self.start_moving()
        elif self.direction.x != 1 and not self.is_turning:
            self.next_direction = Vector2(-1, 0)
            self.is_turning = True

    def change_direction_right(self):
        if not self.moving:
            self.next_direction = Vector2(1, 0)
            self.start_moving()
        elif self.direction.x != -1 and not self.is_turning:
            self.next_direction = Vector2(1, 0)
            self.is_turning = True
    def reset_snake(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)  # Stop moving
        self.next_direction = Vector2(1, 0)  # Default direction
        self.moving = False  # Snake won't move until key is pressed
        self.new_block = False
        self.is_turning = False


class Food():
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size,
                                 cell_size)  # add int() if there is an error here
        screen.blit(berry, fruit_rect)
        # pygame.draw.rect(screen,(44,44,44),fruit_rect)

    def randomize(self):
        while True:
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.pos = Vector2(self.x, self.y)

            # Check if fruit spawns in UI areas (top row where scores are displayed)
            if self.y == 0 or self.y == 1:
                continue
            break


class HighScore():
    def __init__(self, filename="highscore.txt"):
        self.filename = filename
        self.high_score = self.load_high_score()
    def load_high_score(self):
        # Load high score from file, return 0 if file doesn't exist
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return int(file.read().strip())
            else:
                return 0
        except (ValueError, IOError):
            return 0
    def save_high_score(self, score):
        # Save high score to file if it's a new record
        if score > self.high_score:
            self.high_score = score
            try:
                with open(self.filename, 'w') as file:
                    file.write(str(score))
                return True  # New high score achieved
            except IOError:
                pass  # Couldn't save, but continue playing
        return False  # Not a new high score
    def get_high_score(self):
        return self.high_score


# clock limits how fast our loop runs
# Going over the pygame documentation
class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Food()
        self.high_score_manager = HighScore()

    def update(self):
        self.snake.move_snake()
        self.check_food_collision()
        self.check_collision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_high_score()

        # Draw instruction if snake is not moving
        if not self.snake.moving:
            self.draw_start_instruction()

    def check_food_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
#for rare case where the fruit might spawn inside the snake after avoiding the UI areas...
        # if self.fruit.pos == self.snake.body[0]:
        #     self.fruit.randomize()
        #     # Make sure fruit doesn't spawn on snake body after randomization
        #     while self.fruit.pos in self.snake.body:
        #         self.fruit.randomize()
        #     self.snake.add_block()
        #
        # for block in self.snake.body[1:]:
        #     if block == self.fruit.pos:
        #         self.fruit.randomize()
        #         # Make sure fruit doesn't spawn on snake body after randomization
        #         while self.fruit.pos in self.snake.body:
        #             self.fruit.randomize()

    def check_collision(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                # check for snake collision with itself

    def game_over(self):
        # Calculate current score and check for high score
        current_score = len(self.snake.body) - 3
        self.high_score_manager.save_high_score(current_score)

        # Reset the snake and fruit
        self.snake.reset_snake()
        self.fruit.randomize()

    def draw_grass(self):
        grass_color = (80, 219, 33)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,"black")
        score_x = int(cell_size*cell_number-70)
        score_y = int(cell_size+20)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = berry.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left-3,apple_rect.top+1,apple_rect.width+score_rect.width+6,apple_rect.height)

        pygame.draw.rect(screen, (100, 230, 30), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(berry, apple_rect)
        pygame.draw.rect(screen, 'black', bg_rect, 2)

    def draw_high_score(self):
        high_score_text = f"High: {self.high_score_manager.get_high_score()}"
        high_score_surface = game_font.render(high_score_text, True, "black")
        high_score_x = 70
        high_score_y = int(cell_size + 20)
        high_score_rect = high_score_surface.get_rect(center=(high_score_x, high_score_y))
        bg_rect = pygame.Rect(high_score_rect.left - 4, high_score_rect.top - 2,
                              high_score_rect.width + 5, high_score_rect.height + 4)

        pygame.draw.rect(screen, (100, 230, 30), bg_rect)
        screen.blit(high_score_surface, high_score_rect)
        # pygame.draw.rect(screen, 'black', bg_rect, 2)

    def draw_start_instruction(self):
        instruction_text = "Press arrow key to start!"
        instruction_surface = pygame.font.Font(None, 36).render(instruction_text, True, "white")
        instruction_rect = instruction_surface.get_rect(
            center=(cell_size * cell_number // 2, cell_size * cell_number // 2))

        # Draw semi-transparent background
        bg_rect = pygame.Rect(instruction_rect.left - 10, instruction_rect.top - 5,
                              instruction_rect.width + 20, instruction_rect.height + 10)
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height))
        bg_surface.set_alpha(180)
        bg_surface.fill((0, 0, 0))
        screen.blit(bg_surface, bg_rect)

        screen.blit(instruction_surface, instruction_rect)


pygame.init()
pygame.display.set_caption("Snake")
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
berry = pygame.image.load('graphics/apple.png').convert_alpha()
berry = pygame.transform.scale(berry, (cell_size, cell_size))
game_font = pygame.font.Font(None, 50)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    clock.tick(120)

pygame.quit()
sys.exit()