# game/arena.py
import pygame
from game import settings
import math

def get_arena_center():
    return (settings.WIDTH // 2, settings.HEIGHT // 2)

def get_arena_radius():
    # Ensure the arena fits nicely within the window.
    return min(settings.WIDTH, settings.HEIGHT) // 2 - settings.ARENA_MARGIN

def draw(surface):
    center = get_arena_center()
    radius = get_arena_radius()
    arena_color = (50, 50, 50)  # Dark gray outline for the arena.
    pygame.draw.circle(surface, arena_color, center, radius, 5)

