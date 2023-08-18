import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird dimensions and position
bird_width = 40
bird_height = 40
bird_x = SCREEN_WIDTH // 3
bird_y = SCREEN_HEIGHT // 2

# Gravity
gravity = 0.8
bird_velocity = 0
bird_jump = -12

# Pipe dimensions and position
pipe_width = 60
pipe_gap = 200
pipe_x = SCREEN_WIDTH
pipe_y = random.randint(pipe_gap, SCREEN_HEIGHT - pipe_gap)

# Pipe movement speed
pipe_speed = 5

# Score
score = 0

def draw_bird(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, bird_width, bird_height))

def draw_pipe(x, y):
    pygame.draw.rect(screen, BLACK, (x, 0, pipe_width, y))
    pygame.draw.rect(screen, BLACK, (x, y + pipe_gap, pipe_width, SCREEN_HEIGHT - y - pipe_gap))

def display_score(score):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (20, 20))

def game_over():
    global pipe_x, pipe_y, bird_y, bird_velocity, score

    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
    display_score(score)
    pygame.display.update()
    pygame.time.wait(2000)

    # Reset the game variables
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_y = random.randint(pipe_gap, SCREEN_HEIGHT - pipe_gap)
    score = 0

def main():
    global bird_velocity, bird_y, pipe_x, pipe_y, score

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bird_y > 0:
                        bird_velocity = bird_jump

        bird_velocity += gravity
        bird_y += bird_velocity

        if bird_y <= 0 or bird_y >= SCREEN_HEIGHT - bird_height:
            game_over()

        pipe_x -= pipe_speed
        if pipe_x <= -pipe_width:
            pipe_x = SCREEN_WIDTH
            pipe_y = random.randint(pipe_gap, SCREEN_HEIGHT - pipe_gap)
            score += 1

        # Check for collision with the pipe
        if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
            if bird_y < pipe_y or bird_y + bird_height > pipe_y + pipe_gap:
                game_over()

        screen.fill(WHITE)
        draw_bird(bird_x, bird_y)
        draw_pipe(pipe_x, pipe_y)
        display_score(score)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
