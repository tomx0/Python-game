from turtle import Screen, color
import pygame
from pygame.locals import *
import sys
import random

WIDTH = 1920
HEIGHT = 1080
FPS = 60
pygame.init()

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

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Classes
class Player:
    def __init__(self, color, size):
        self.color = GREEN
        self.size = size #size je cislo popisujici delku strany ctverce, kterym je hrac
        self.alive = True 


#Text
def draw_text(text, surface, pos, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    surface.blit(text_surface, text_rect)

    #namaluje ctverec(hrac) do prostred pole
def draw_player(surface):
    pygame.draw.rect(surface, Player.color, pygame.Rect(30, 30, 60, 60))


def enemies():
    object_size = random.randint(20, 50)
    object_pos = [random.randint(0, WIDTH - object_size), 0]
    object_speed = random.randint(3, 8)
    object_color = random.choice([WHITE, YELLOW, GRAY_1, GRAY_2,GREEN,CYAN])
    return object_pos, object_size, object_speed, object_color
    
# Main
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Dodger", screen, [WIDTH // 2, HEIGHT // 4], 300, RED)
        draw_text("Press SPACE to play", screen, [WIDTH // 2, HEIGHT // 2], 80, YELLOW)
        draw_text("Press ESC to quit", screen, [WIDTH // 2, HEIGHT * 3 // 4], 80, YELLOW)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game()
                if event.key == pygame.K_ESCAPE:
                    end_game()

if __name__ == '__main__':
    main_menu()

def start_game(): #ted me jeste nenapadlo,co sem napsat 
        screen.fill(BLACK)
        draw_player(Screen)

#Ends the game
def end_game():
    pygame.quit()
    exit()

