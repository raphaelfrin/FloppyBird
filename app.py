import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
window_width = 400
window_height = 600

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Configuration de la fenêtre
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird')

# Horloge pour contrôler la vitesse de rafraîchissement
clock = pygame.time.Clock()

# Variables de jeu
bird_x = 50
bird_y = 300
bird_width = 40
bird_height = 40
bird_velocity = 0
gravity = 0.5
jump = -10

pipe_width = 70
pipe_height = random.randint(200, 400)
pipe_gap = 200
pipe_x = window_width
pipe_velocity = -3

score = 0

font = pygame.font.SysFont(None, 35)

bird=pygame.image.load("bird.png")
birdlow=pygame.transform.scale(bird,(bird_width, bird_height))

def draw_bird(x, y):
    window.blit(birdlow, [x, y, bird_width, bird_height])

def draw_pipe(x, height):
    pygame.draw.rect(window, green, [x, 0, pipe_width, height])
    pygame.draw.rect(window, green, [x, height + pipe_gap, pipe_width, window_height])

def message(msg, color):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [window_width / 6, window_height / 3])

def game_loop():
    global bird_y, bird_velocity, pipe_height, pipe_x, score

    bird_y = 300
    bird_velocity = 0
    pipe_height = random.randint(200, 400)
    pipe_x = window_width
    score = 0

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            window.fill(white)
            message("Game Over! Press Space to Restart", black)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump

        bird_velocity += gravity
        bird_y += bird_velocity

        if bird_y > window_height - bird_height or bird_y < 0:
            game_close = True

        pipe_x += pipe_velocity

        if pipe_x < -pipe_width:
            pipe_x = window_width
            pipe_height = random.randint(200, 400)
            score += 1

        if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
            if bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap:
                game_close = True

        window.fill(white)
        draw_bird(bird_x, bird_y)
        draw_pipe(pipe_x, pipe_height)
        
        score_text = font.render(f"Score: {score}", True, black)
        window.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()