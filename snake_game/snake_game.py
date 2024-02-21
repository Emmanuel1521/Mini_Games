import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake attributes
snake_block = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont(None, 30)

# Function to display score
def display_score(score):
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [0, 0])

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Main function
def snake_game():
    game_over = False
    game_close = False

    # Initial position of snake
    x, y = width / 2, height / 2

    # Initial length of snake
    snake_list = []
    length = 1

    # Initial position of food
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Initial direction of snake
    dx, dy = 0, 0

    # Initial score
    score = 0

    clock = pygame.time.Clock()

    # Game loop
    while not game_over:
        while game_close:
            screen.fill(white)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        # Update snake's position
        x += dx
        y += dy

        # Wrap snake around the screen
        if x >= width:
            x = 0
        elif x < 0:
            x = width - snake_block
        elif y >= height:
            y = 0
        elif y < 0:
            y = height - snake_block

        screen.fill(white)

        # Draw food
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Draw snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(score)

        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
snake_game()
