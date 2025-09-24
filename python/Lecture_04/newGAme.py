import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
SIZE = 20
WIDTH = 800
HEIGHT = 600
SNAKE_COLOR = (0, 255, 0)  # Green
APPLE_COLOR = (255, 0, 0)   # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(100, 100)]
        self.direction = (SIZE, 0)  # Start moving to the right

    def move(self):
        head_x, head_y = self.positions[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def change_direction(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], SIZE, SIZE))

    def get_head_position(self):
        return self.positions[0]

    def increase_length(self):
        self.length += 1

# Apple class
class Apple:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // SIZE) - 1) * SIZE,
                         random.randint(0, (HEIGHT // SIZE) - 1) * SIZE)

    def spawn(self):
        self.position = (random.randint(0, (WIDTH // SIZE) - 1) * SIZE,
                         random.randint(0, (HEIGHT // SIZE) - 1) * SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, APPLE_COLOR, pygame.Rect(self.position[0], self.position[1], SIZE, SIZE))

# Game class
class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -SIZE))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, SIZE))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-SIZE, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((SIZE, 0))

            self.snake.move()

            # Check for collision with apple
            if self.snake.get_head_position() == self.apple.position:
                self.snake.increase_length()
                self.apple.spawn()
                self.score += 1

            # Check for collision with walls or self
            head_x, head_y = self.snake.get_head_position()
            if (head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT or
                self.snake.positions[0] in self.snake.positions[1:]):
                running = False

            # Draw everything
            self.surface.fill(BACKGROUND_COLOR)
            self.snake.draw(self.surface)
            self.apple.draw(self.surface)
            pygame.display.flip()

            # Control the game speed
            self.clock.tick(10)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()