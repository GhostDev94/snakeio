# main.py
import pygame
import math
from game.settings import WIDTH, HEIGHT
from game.arena import draw as draw_arena, get_arena_center, get_arena_radius
from game.snake import Snake
from game.food import Food

def is_collision(pos1, pos2, radius1, radius2):
    # Returns True if two circles (position/radius) intersect.
    return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1]) < (radius1 + radius2)

def check_snake_collision(snake1, snake2, segment_radius=5):
    # Check if snake1's head collides with any segment of snake2 (excluding the head if desired)
    head = snake1.segments[0]
    for idx, seg in enumerate(snake2.segments):
        if idx == 0:
            continue  # Skip head-to-head collisions if you want a different rule for that.
        if is_collision(head, seg, segment_radius, segment_radius):
            return True
    return False

def draw_scores(surface, snake1, snake2):
    font = pygame.font.SysFont("Arial", 24)
    score_text1 = font.render(f"Red Score: {snake1.score}", True, (255, 255, 255))
    score_text2 = font.render(f"Green Score: {snake2.score}", True, (255, 255, 255))
    surface.blit(score_text1, (10, 10))
    surface.blit(score_text2, (10, 40))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnakeIO")
    clock = pygame.time.Clock()

    arena_center = get_arena_center()
    snake1 = Snake((arena_center[0] + 100, arena_center[1]), (255, 0, 0))
    snake2 = Snake((arena_center[0] - 100, arena_center[1]), (0, 255, 0))
    
    # Create a list of food items. We'll start with a single food.
    food_items = [Food()]

    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Control mapping: arrow keys for snake1; A/D keys for snake2.
        turn1 = -1 if keys[pygame.K_LEFT] else 1 if keys[pygame.K_RIGHT] else 0
        turn2 = -1 if keys[pygame.K_a] else 1 if keys[pygame.K_d] else 0

        # --- Update Game State ---
        snake1.update(turn1)
        snake2.update(turn2)
        
        # Check for food collisions.
        # We iterate over a shallow copy of the list so we can remove items as needed.
        for food in food_items[:]:
            if is_collision(snake1.segments[0], food.position, 5, food.radius):
                snake1.grow()  # Increment length and score.
                food_items.remove(food)
                food_items.append(Food())  # Spawn a new food.
            elif is_collision(snake2.segments[0], food.position, 5, food.radius):
                snake2.grow()
                food_items.remove(food)
                food_items.append(Food())

        # Check for snake-to-snake collisions.
        if check_snake_collision(snake1, snake2):
            print("Red snake collided with Green snake!")
            # Insert collision response here (e.g., reduce score, reset game, or mark game over)
        if check_snake_collision(snake2, snake1):
            print("Green snake collided with Red snake!")
        
        # Optional: Check if any snake goes out of the arena.
        for idx, snake in enumerate([snake1, snake2], start=1):
            head = snake.segments[0]
            cx, cy = arena_center
            if ((head[0] - cx) ** 2 + (head[1] - cy) ** 2) > (get_arena_radius() ** 2):
                print(f"Snake {idx} is out of bounds!")
                # Insert reset or game over logic here.

        # --- Rendering ---
        screen.fill((0, 0, 0))  # Clear the screen.
        draw_arena(screen)      # Draw the circular arena.
        snake1.draw(screen)
        snake2.draw(screen)
        for food in food_items:
            food.draw(screen)
        draw_scores(screen, snake1, snake2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
