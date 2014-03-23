black = { 0, 0, 0}
white = {255,255,255}
sky_blue = {  66,  136, 227}
background_color = {0,153,76}
square_background_color = white
game_width = 1000
game_height = 500
size = {game_width,game_height}
left_margin = 20
top_margin = 20
puzzle_letters_left = left_margin
puzzle_letters_top = top_margin
square_width = 50
spacing = 10
letters_guessed_left = left_margin
letters_guessed_top = top_margin + math.floor(0.1 * game_height) + spacing
goodjob_x = puzzle_letters_left + square_width + spacing
goodjob_y = 200

solved_words_column_width = math.floor(0.1 * game_width)
solved_words_column_padding = math.floor(0.01 * game_width)
solved_words_region_left = left_margin
solved_words_region_top = letters_guessed_top + square_width + spacing
solved_words_height = math.floor(0.01 * game_width)
solved_words_column_length = 15
solved_words_col_margin = 720

status_label_left = left_margin
status_label_top = math.floor(0.8 * game_height)
puzzle_letter_font_size = math.floor(0.03*game_width)
guessed_letter_font_size = math.floor(0.02*game_width)
font_size = math.floor(0.02*game_width)
button_size = {100, 30}
button_width = 100
button_height = 30
--buttons_top = math.floor(0.9 * game_height)
button_top = 10 * puzzle_letters_left + square_width + spacing
--buttons_left = left_margin
button_left = puzzle_letters_top
button_padding = 20
countdown_left = math.floor(0.9 * game_width)
countdown_top = math.floor(0.05 * game_height) 
score_left = math.floor(0.9 * game_width)
score_top = math.floor(0.2 * game_height)
notification_left = math.floor(0.5 * game_width)
notification_top = math.floor(0.95 * game_height)

title = "Letter Lizard"

default_font_size = 20

time_allowed_s = 100

title_font_size = 50
title_screen_left = math.floor(0.3*game_width)
title_screen_top = math.floor(0.1*game_width)
title_screen_option_font_size = 20
title_screen_option_spacing = 10
title_screen_options_left = math.floor(0.3*game_width)
title_screen_options_top = math.floor(0.5*game_height)
title_screen_options_width = 20