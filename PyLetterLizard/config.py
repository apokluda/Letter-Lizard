import pygame
import pygbutton
import sys
from pygame.locals import *
from pygame import time
from pygame import font
from pygame import mouse

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


#SET CONFIGURATION VALUES
black = [ 0, 0, 0]
white = [255,255,255]
sky_blue = [  66,  136, 227]
background_color = [0,153,76]
square_background_color = white
game_width = 1023
game_height = 576
size = [game_width,game_height]
left_margin = 20
top_margin = 20
puzzle_letters_left = left_margin
puzzle_letters_top = top_margin
square_width = 50
spacing = 30
letters_guessed_left = left_margin
letters_guessed_top = top_margin + int(0.1 * game_height) + spacing

solved_words_column_width = int(0.1 * game_width)
solved_words_column_padding = int(0.01 * game_width)
solved_words_region_left = left_margin
solved_words_region_top = letters_guessed_top + square_width + spacing
solved_words_height = int(0.01 * game_width)
solved_words_column_length = 15

status_label_left = left_margin
status_label_top = int(0.8 * game_height)
puzzle_letter_font_size = int(0.03*game_width)
guessed_letter_font_size = int(0.02*game_width)
font_size = int(0.02*game_width)
button_size = (100, 30)
buttons_top = int(0.9 * game_height)
buttons_left = left_margin
button_padding = 20
countdown_left = int(0.9 * game_width)
countdown_top = int(0.05 * game_height) 
score_left = int(0.9 * game_width)
score_top = int(0.2 * game_height)
#notification_left = int(0.5 * game_width)
#notification_top = int(0.95 * game_height)

title = "Letter Lizard"

default_font_size = 20

puzzle_letter_font = pygame.font.SysFont("Arial", puzzle_letter_font_size, bold=True)
guessed_letter_font = pygame.font.SysFont("Arial", guessed_letter_font_size, bold=True)
default_font = pygame.font.SysFont("Arial", default_font_size, bold=True)

time_allowed_s = 100



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

splash_screen_img_name = "splash.png"
splash_screen_img = pygame.image.load(splash_screen_img_name)

options_screen_img_name = "options.png"
options_screen_img = pygame.image.load(options_screen_img_name)
#splash_screen_img = splash_screen_img.convert()

GAME_STATES = Enum(['PLAYING', 'GAME_OVER', 'SPLASH_SCREEN', 'OPTIONS'])


# def load_image(name, colorkey=None):
#     fullname = os.path.join('data', name)
#     try:
#         image = pygame.image.load(fullname)
#     except pygame.error, message:
#         print 'Cannot load image:', name
#         raise SystemExit, message
#     image = image.convert()
#     if colorkey is not None:
#         if colorkey is -1:
#             colorkey = image.get_at((0,0))
#         image.set_colorkey(colorkey, RLEACCEL)
#     return image, image.get_rect()
           
