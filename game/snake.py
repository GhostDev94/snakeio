# game/snake.py
import pygame
import math

class Snake:
    def __init__(self, pos, color, speed=3, turn_rate=0.1):
        self.color = color
        self.segments = [pos]  # each segment is an (x, y) tuple
        self.direction = 0     # in radians; 0 means to the right
        self.speed = speed
        self.turn_rate = turn_rate
        self.grow_counter = 0  # when > 0, we skip removing the tail segment
        self.score = 0         # score increases as the snake eats food

    def update(self, turn_direction=0):
        # Update heading based on user input
        self.direction += turn_direction * self.turn_rate
        
        # Calculate new head position
        head_x, head_y = self.segments[0]
        new_x = head_x + self.speed * math.cos(self.direction)
        new_y = head_y + self.speed * math.sin(self.direction)
        new_head = (new_x, new_y)
        
        # Insert the new head at the beginning of the segments list
        self.segments.insert(0, new_head)
        
        # If we have growth pending, skip removing the tail; else remove the last element.
        if self.grow_counter > 0:
            self.grow_counter -= 1
        else:
            self.segments.pop()

    def grow(self, amount=5):
        # Increases the snake's length (by delaying tail removal)
        self.grow_counter += amount
        self.score += 1

    def draw(self, surface):
        for seg in self.segments:
            pygame.draw.circle(surface, self.color, (int(seg[0]), int(seg[1])), 5)
