# game/snake.py
import pygame
import math

class Snake:
    def __init__(self, pos, color, speed=3, turn_rate=0.1):
        self.color = color
        self.segments = [pos]  # Each segment is an (x, y) coordinate.
        self.direction = 0     # Direction in radians. 0 = right.
        self.speed = speed
        self.turn_rate = turn_rate

    def update(self, turn_direction=0):
        # Update the snake's direction
        self.direction += turn_direction * self.turn_rate

        # Calculate new head position.
        head_x, head_y = self.segments[0]
        new_x = head_x + self.speed * math.cos(self.direction)
        new_y = head_y + self.speed * math.sin(self.direction)
        new_head = (new_x, new_y)
        
        # Add new head and remove the last segment.
        self.segments.insert(0, new_head)
        self.segments.pop()

    def draw(self, surface):
        for seg in self.segments:
            pygame.draw.circle(surface, self.color, (int(seg[0]), int(seg[1])), 5)

