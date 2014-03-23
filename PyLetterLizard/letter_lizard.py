#!/usr/bin/env python
# Import a library of functions called 'pygame'
from config import *
from game import *


class LetterLizard:
    def __init__(self):
        pass

def doexit():
    pygame.quit()
    sys.exit()

def new_game():
    global game_state
    game_state = GAME_STATES.PLAYING
    global game
    game = Game()
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
    title_screen_options = ['NEW GAME', 'HIGH SCORES', 'OPTIONS', 'EXIT']
    title_label = title_font.render("Letter Lizard!", 1, black)
    selected_option = 0 
    while done == False:
        if (game_state == GAME_STATES.SPLASH_SCREEN):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        # option = title_screen_options[selected_option]
                        # if (option == "NEW GAME"):
                        game_state = GAME_STATES.OPTIONS
                        new_game()
            screen.blit(splash_screen_img, (0, 0))
                # game.draw(screen)
        elif (game_state == GAME_STATES.OPTIONS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            screen.blit(options_screen_img, (0, 0))
            num_rounds_lbl = default_font.render("Number of Rounds: ", 1, black)
            time_per_round_lbl = default_font.render("Time per round: ", 1, black)
            seconds_lbl = default_font.render("seconds", 1, black)
            difficult_lbl = default_font.render("Difficulty: ", 1, black)
            #screen.blit(num_rounds_lbl, )
            #new_game()        
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
                    new_game()
                elif 'click' in button_main_menu.handleEvent(event):
                    game_state = GAME_STATES.SPLASH_SCREEN
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
