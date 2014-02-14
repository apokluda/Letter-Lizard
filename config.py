import pygame
from pygame.locals import *
from pygame import time

#SET CONFIGURATION VALUES
black = [ 0, 0, 0]
white = [255,255,255]
sky_blue = [  66,  136, 227]
game_width = 1000
game_height = 600
size = [game_width,game_height]
left_margin = 20
top_margin = 20
puzzle_letters_left = left_margin
puzzle_letters_top = top_margin
square_width = 50
spacing = 30
letters_guessed_left = left_margin
letters_guessed_top = game_height/2
correct_words_left = int(0.75 * game_width)
correct_words_top = int(0.2 * game_height)
status_label_left = left_margin
status_label_top = int(0.7 * game_height)
puzzle_letter_font_size = int(0.03*game_width)
guessed_letter_font_size = int(0.02*game_width)
font_size = int(0.02*game_width)
button_size = (100, 50)
buttons_top = int(0.8 * game_height)
buttons_left = left_margin
button_padding = 20
countdown_left = int(0.75 * game_width)
countdown_top = int(0.12 * game_height) 
notification_left = int(0.5 * game_width)
notification_top = int(0.8* game_height)

title = "Letter Lizard"

puzzle_letter_font = pygame.font.SysFont("Arial", puzzle_letter_font_size, bold=True)
guessed_letter_font = pygame.font.SysFont("Arial", guessed_letter_font_size, bold=True)