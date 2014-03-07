import pygame
import pygbutton
import sys
from pygame.locals import *
from pygame import time
from pygame import font
from pygame import mouse

#SET CONFIGURATION VALUES
black = [ 0, 0, 0]
white = [255,255,255]
sky_blue = [  66,  136, 227]
background_color = [0,153,76]
game_width = 1000
game_height = 500
size = [game_width,game_height]
left_margin = 20
top_margin = 20
puzzle_letters_left = left_margin
puzzle_letters_top = top_margin
square_width = 50
spacing = 30
letters_guessed_left = left_margin
letters_guessed_top = int(0.3 * game_height)

solved_words_column_width = int(0.1 * game_width)
solved_words_column_padding = int(0.01 * game_width)
solved_words_region_left = int(0.7 * game_width)
solved_words_region_top = int(0.1 * game_width)
solved_words_height = int(0.01 * game_width)

status_label_left = left_margin
status_label_top = int(0.7 * game_height)
puzzle_letter_font_size = int(0.03*game_width)
guessed_letter_font_size = int(0.02*game_width)
font_size = int(0.02*game_width)
button_size = (100, 30)
buttons_top = int(0.9 * game_height)
buttons_left = left_margin
button_padding = 20
countdown_left = int(0.9 * game_width)
countdown_top = int(0.05 * game_height) 
notification_left = int(0.5 * game_width)
notification_top = int(0.8* game_height)

title = "Letter Lizard"

default_font_size = 20

puzzle_letter_font = pygame.font.SysFont("Arial", puzzle_letter_font_size, bold=True)
guessed_letter_font = pygame.font.SysFont("Arial", guessed_letter_font_size, bold=True)
default_font = pygame.font.SysFont("Arial", default_font_size, bold=True)

time_allowed_s = 120

solved_words_column_length = 10

#title screen
title_font_size = 50
title_font = pygame.font.SysFont("Arial", title_font_size, bold=True)
title_screen_left = int(0.3*game_width)
title_screen_top = int(0.1*game_width)
title_screen_option_font_size = 20
title_screen_option_font = pygame.font.SysFont("Arial", title_screen_option_font_size, bold=True)
title_screen_option_spacing = 10
title_screen_options_left = int(0.3*game_width)
title_screen_options_top = int(0.5*game_height)
title_screen_options_width = 20


