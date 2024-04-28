from pickle import GLOBAL
from turtle import Screen, color
import pygame
from pygame.locals import *
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
GRAY_1 = (72,72,72)
GRAY_2 = (114,114,114)


#Classes
class Player:
    def __init__(self, color, size, posx, posy):
        self.color = color
        self.size = size #size je cislo popisujici delku strany ctverce, kterym je hrac
        self.alive = True 
        self.x = posx
        self.y = posy


#Text
def draw_text(text, surface, pos, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    surface.blit(text_surface, text_rect)

    #namaluje ctverec hrace ve tvaru ctverce
def draw_player(x, y):
    pygame.draw.rect(screen, player.color, (x, y, player.size, player.size))



def enemies():
    object_size = random.randint(20, 50)
    object_pos = [random.randint(0, WIDTH - object_size), 0]
    object_speed = random.randint(3, 8)
    object_color = random.choice([WHITE, YELLOW, GRAY_1, GRAY_2,GREEN,CYAN])
    return object_pos, object_size, object_speed, object_color


def game():
    clock = pygame.time.Clock()
    objects = []

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                end_game()

        if random.randint(0, 100) < 5:
            objects.append(create_object())

        for obj in objects:
            pygame.draw.rect(screen, obj[3], (obj[0][0], obj[0][1], obj[1], obj[1]))
            obj[0][1] += obj[2]

        pygame.display.flip()
        clock.tick(FPS)
    
# Main
def main_menu():
    global player, screen, has_started, player_x, player_y
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    draw_text("Dodger", screen, [WIDTH // 2, HEIGHT // 4], 300, RED)
    draw_text("Press SPACE to play", screen, [WIDTH // 2, HEIGHT // 2], 80, YELLOW)
    draw_text("Press ESC to quit", screen, [WIDTH // 2, HEIGHT * 3 // 4], 80, YELLOW)
    has_started = False
    player_x = 930
    player_y = 510
    player = Player(GREEN, 60, 930, 510)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if has_started == False:
                        start_game()
                if event.key == pygame.K_LEFT:
                    player_x = player_x - 5
                    screen.fill(BLACK)
                    draw_player(player_x, player_y)
                if event.key == pygame.K_RIGHT:
                    player_x = player_x + 5
                    screen.fill(BLACK)
                    draw_player(player_x, player_y)
                if event.key == pygame.K_ESCAPE:
                    end_game()
            pygame.display.update()


def start_game(): #work in progress
    has_started = True
    screen.fill(BLACK)
    draw_player(930, 510)

#Ends the game
def end_game():
    pygame.quit()
    exit()

if __name__ == '__main__':
    main_menu()
