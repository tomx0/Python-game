from turtle import color
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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Classes
class Player:
    __init__(self, color, size):
        self.color = color
        self.size = size #size je cislo popisujici delku strany ctverce, kterym je hrac
        self.alive = true 


#Text
def draw_text(text, surface, pos, size, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    surface.blit(text_surface, text_rect)

# Main
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Dodger", screen, [WIDTH // 2, HEIGHT // 4], 60, WHITE)
        draw_text("Press SPACE to play", screen, [WIDTH // 2, HEIGHT // 2], 30, WHITE)
        draw_text("Press ESC to quit", screen, [WIDTH // 2, HEIGHT * 3 // 4], 30, WHITE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    end_game()

main_menu()

#Ends the game
def end_game():
    pygame.quit()
    exit()

