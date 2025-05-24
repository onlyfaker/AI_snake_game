import pygame
from pygame.math import Vector2

class Food():
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)


    def draw_fruit(self):
        # create a rectangle
        #draw a rectangle