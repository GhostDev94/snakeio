# game/food.py
import pygame
import random
import math
from game.arena import get_arena_center, get_arena_radius

class Food:
    def __init__(self, color=(255, 255, 255), radius=5):
        self.color = color
        self.radius = radius
        self.position = self.generate_position()
    
    def generate_position(self):
        center = get_arena_center()
        arena_radius = get_arena_radius() - 10  # keep some margin
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, arena_radius)
        x = center[0] + r * math.cos(angle)
        y = center[1] + r * math.sin(angle)
        return (x, y)
    
    def draw(self, surface):
        pygame.draw.circle(
            surface, 
            self.color, 
            (int(self.position[0]), int(self.position[1])), 
            self.radius
        )
