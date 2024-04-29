import pygame
import sys
import random

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKBLUE = (0, 4, 53)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY_1 = (72, 72, 72)
GRAY_2 = (114, 114, 114)

# Classes
class Player:
    def __init__(self, color, size, posx, posy):
        self.color = color
        self.size = size  
        self.alive = True
        self.x = posx
        self.y = posy

# Text
def draw_text(text, surface, pos, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    surface.blit(text_surface, text_rect)

# Function to draw player
def draw_player(surface, x, y, color, size):
    pygame.draw.rect(surface, color, (x, y, size, size))

# Function to create enemies
def create_object():
    object_size = random.randint(20, 50)
    object_pos = [random.randint(0, WIDTH - object_size), 0]
    object_speed = random.randint(3, 8)
    object_color = random.choice([WHITE, YELLOW, GRAY_1, GRAY_2, GREEN, CYAN])
    return object_pos, object_size, object_speed, object_color

# Main game loop
def game(screen):
    clock = pygame.time.Clock()
    objects = []

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        if random.randint(0, 100) < 5:
            objects.append(create_object())

        for obj in objects:
            pygame.draw.rect(screen, obj[3], (obj[0][0], obj[0][1], obj[1], obj[1]))
            obj[0][1] += obj[2]

        draw_player(screen, player.x, player.y, player.color, player.size)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= 5
        if keys[pygame.K_d] and player.x < WIDTH - player.size:
            player.x += 5
        if keys[pygame.K_s] and player.y < HEIGHT - player.size:
            player.y += 5

        pygame.display.flip()
        clock.tick(FPS)

# Main menu
def main_menu():
    global player
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    draw_text("Dodger", screen, [WIDTH // 2, HEIGHT // 4], 300, RED)
    draw_text("Press SPACE to play", screen, [WIDTH // 2, HEIGHT // 2], 80, YELLOW)
    draw_text("Press ESC to quit", screen, [WIDTH // 2, HEIGHT * 3 // 4], 80, YELLOW)
    player = Player(GREEN, 60, 930, HEIGHT - 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game(screen)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main_menu()
