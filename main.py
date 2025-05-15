# main.py
import pygame
from game.settings import WIDTH, HEIGHT
from game.arena import draw as draw_arena, get_arena_center, get_arena_radius
from game.snake import Snake

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnakeIO")
    clock = pygame.time.Clock()

    # Create snakes with distinct colors at starting positions
    arena_center = get_arena_center()
    snake1 = Snake((arena_center[0] + 100, arena_center[1]), (255, 0, 0))
    snake2 = Snake((arena_center[0] - 100, arena_center[1]), (0, 255, 0))

    # Control mapping:
    # - Snake 1 uses arrow keys: Left/Right to turn.
    # - Snake 2 uses A/D keys: A to turn left, D to turn right.
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Determine turning inputs for Snake 1
        turn1 = -1 if keys[pygame.K_LEFT] else 1 if keys[pygame.K_RIGHT] else 0
        # Determine turning inputs for Snake 2
        turn2 = -1 if keys[pygame.K_a] else 1 if keys[pygame.K_d] else 0

        # --- Update Game State ---
        snake1.update(turn1)
        snake2.update(turn2)

        # Optional: Check if a snake goes out of the circular arena.
        # For instance, you could use the arena's center and radius to decide if the snake's head is too far:
        for idx, snake in enumerate([snake1, snake2], start=1):
            head_x, head_y = snake.segments[0]
            cx, cy = arena_center
            if ((head_x - cx) ** 2 + (head_y - cy) ** 2) > (get_arena_radius() ** 2):
                print(f"Snake {idx} is out of bounds!")
                # Reset or end game logic here if needed.

        # --- Rendering ---
        screen.fill((0, 0, 0))  # Clear the screen with black.
        draw_arena(screen)      # Draw the circular arena.
        snake1.draw(screen)
        snake2.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS.

    pygame.quit()

if __name__ == "__main__":
    main()
