#!/usr/bin/env python
from config import *
from game import *

def doexit():
    pygame.quit()
    sys.exit()

def new_game(difficulty, time_s):
    global time_allowed_s
    time_allowed_s = time_s
    global game_state
    game_state = GAME_STATES.PLAYING
    global game
    game = Game(difficulty)
    global time_remaining_s
    time_remaining_s = time_allowed_s
    global start_time_ms
    start_time_ms = time.get_ticks()

def convert_to_time_string(time_remaining_s):
    time_remaining_str = ''
    mins = time_remaining_s/60
    secs = time_remaining_s % 60
    if (mins < 10): time_remaining_str += '0'
    time_remaining_str += str(mins)
    time_remaining_str += ':'
    if (secs < 10): time_remaining_str += '0'
    time_remaining_str += str(secs)
    return time_remaining_str

def main():
    pygame.init()
    if not pygame.font: print 'Warning, fonts disabled'
    if not pygame.mixer: print 'Warning, sound disabled'
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    done = False
    game_state = GAME_STATES.SPLASH_SCREEN
    all_buttons = []
    button_main_menu = pygbutton.PygButton((buttons_left, buttons_top, button_size[0], button_size[1]), 'Main Menu')
    button_exit = pygbutton.PygButton((buttons_left + button_padding + button_size[0], buttons_top, button_size[0], button_size[1]), 'Exit')
    button_new_game = pygbutton.PygButton((buttons_left + 2*(button_padding + button_size[0]), buttons_top, button_size[0], button_size[1]), 'New Game')
    all_buttons.append(button_main_menu)
    all_buttons.append(button_exit)
    all_buttons.append(button_new_game)
    option_row = 0
    NUM_OPTIONS = 3
    NUM_VALUES_PER_OPTION = 3
    option_choices = [[3,5,7], [60,90,120], ['EASY', 'MEDIUM', 'HARD']]
    selected_options = [0,0,0]
    num_games = 3
    while done == False:
        if (game_state == GAME_STATES.SPLASH_SCREEN):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        game_state = GAME_STATES.OPTIONS
            screen.blit(splash_screen_img, (0, 0))
        elif (game_state == GAME_STATES.OPTIONS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        game_state = GAME_STATES.PLAYING
                        difficulty = option_choices[2][selected_options[2]]
                        time_s = int(option_choices[1][selected_options[1]])
                        num_games = int(option_choices[0][selected_options[0]])
                        new_game(difficulty, time_s)
                    elif (event.key == pygame.K_DOWN):
                        if (option_row < NUM_OPTIONS - 1):
                            option_row += 1
                    elif (event.key == pygame.K_UP):
                        if (option_row > 0):
                            option_row -= 1
                    elif (event.key == pygame.K_RIGHT):
                        if (selected_options[option_row] < NUM_VALUES_PER_OPTION - 1):
                            selected_options[option_row] += 1
                    elif (event.key == pygame.K_LEFT):
                        if (selected_options[option_row] > 0):
                            selected_options[option_row] -= 1
            option_labels = []
            for i in range(NUM_OPTIONS):
                choice = selected_options[i]
                row = []
                for j in range(NUM_VALUES_PER_OPTION):
                    s = str(option_choices[i][j])
                    if (choice == j):
                        if (option_row == i):
                            row.append(default_font.render(s, 1, blue))
                        else:
                            row.append(default_font.render(s, 1, red))
                    else:
                        row.append(default_font.render(s, 1, black))
                option_labels.append(row)
            screen.blit(options_screen_img, (0, 0))
            for i in range(3):
                screen.blit(option_labels[0][i], (num_rounds_left + i * 40, num_rounds_top))
            for i in range(3):
                screen.blit(option_labels[1][i], (time_per_round_left + i * 40, time_per_round_top))
            for i in range(3):
                screen.blit(option_labels[2][i], (difficulty_left + i * 120, difficulty_top))
        elif (game_state == GAME_STATES.PLAYING):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif 'click' in button_exit.handleEvent(event):
                    doexit()
                elif 'click' in button_new_game.handleEvent(event):
                    new_game()
                elif 'click' in button_main_menu.handleEvent(event):
                    game_state = GAME_STATES.SPLASH_SCREEN
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_RETURN and game_state == GAME_STATES.PLAYING):
                        game.guess()
                    elif (event.key == pygame.K_BACKSPACE):
                        game.process_backspace()
                    elif (event.key == pygame.K_SPACE):
                        game.shuffle()
                    elif (event.key in range(256)):
                        letter = chr(event.key).upper()
                        game.process_letter(letter)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        print pos
            elapsed_time_ms = time.get_ticks() - start_time_ms
            elapsed_time_s = elapsed_time_ms / 1000
            time_remaining_s = time_allowed_s - elapsed_time_s
            time_remaining_str = convert_to_time_string(time_remaining_s)
            if (time_remaining_s <= 0):
                game_state = GAME_STATES.GAME_OVER
            screen.fill(background_color)
            for b in all_buttons:
                b.draw(screen)
            countdown_label = puzzle_letter_font.render(str(time_remaining_str), 1, black)
            screen.blit(countdown_label, (countdown_left, countdown_top))
            game.draw(screen)
        elif (game_state == GAME_STATES.GAME_OVER):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif 'click' in button_exit.handleEvent(event):
                    doexit()
                elif 'click' in button_new_game.handleEvent(event):
                    game_state = GAME_STATES.PLAYING
                    new_game(difficulty, time_s)
                elif 'click' in button_main_menu.handleEvent(event):
                    game_state = GAME_STATES.SPLASH_SCREEN
            if (num_games > 0):
                num_games -= 1
                game_state = GAME_STATES.PLAYING
                new_game(difficulty, time_s)
                
            screen.fill(background_color)
            for b in all_buttons:
                b.draw(screen)
            countdown_label = puzzle_letter_font.render(str(time_remaining_str), 1, black)
            screen.blit(countdown_label, (countdown_left, countdown_top))
            game.draw(screen)
        pygame.display.flip()
    pygame.quit ()
if __name__ == "__main__":
    main()