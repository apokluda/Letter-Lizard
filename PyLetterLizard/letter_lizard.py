#!/usr/bin/env python
# Import a library of functions called 'pygame'
from config import *
from game import *

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

class LetterLizard:
    def __init__(self):
        pass

def doexit():
    pygame.quit()
    sys.exit()

def new_game():
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
    GAME_STATES = Enum(['PLAYING', 'GAME_OVER', 'SPLASH_SCREEN'])
    game_state = GAME_STATES.SPLASH_SCREEN
    all_buttons = []
    button_main_menu = pygbutton.PygButton((buttons_left, buttons_top, button_size[0], button_size[1]), 'Main Menu')
    button_exit = pygbutton.PygButton((buttons_left + button_padding + button_size[0], buttons_top, button_size[0], button_size[1]), 'Exit')
    button_new_game = pygbutton.PygButton((buttons_left + 2*(button_padding + button_size[0]), buttons_top, button_size[0], button_size[1]), 'New Game')
    all_buttons.append(button_main_menu)
    all_buttons.append(button_exit)
    all_buttons.append(button_new_game)

    #title_screen_options = ['']
    title_screen_options = ['NEW GAME', 'HIGH SCORES', 'OPTIONS', 'EXIT']
    #title_screen_options = Enum(title_screen_option_list)
    title_label = title_font.render("Letter Lizard!", 1, black)
    selected_option = 0 
    #title_screen_option.NEW_GAME
    #selected_option = title_screen_options.NEW_GAME
    #new_game()
    while done == False:
        if (game_state == GAME_STATES.SPLASH_SCREEN):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE):
                        option = title_screen_options[selected_option]
                        if (option == "NEW GAME"):
                            game_state = GAME_STATES.PLAYING
                            new_game()
                        elif (option == 'EXIT'):
                            doexit()
                        pass
                    elif (event.key == pygame.K_UP):
                        if (selected_option > 0): 
                            selected_option -= 1
                    elif (event.key == pygame.K_DOWN):
                        if (selected_option < len(title_screen_options) - 1):
                            selected_option += 1
                        #game.guess()
                
                screen.fill(background_color)
                #title_screen_labels = []
                #for i in title_screen_options:
#                     if (x != selected_option):
#                         label = title_screen_option_font.render(title_screen_options[selected_option], 1,black)
#                         title_screen_labels.append(label)
                for i in range(len(title_screen_options)):
                    #label = title_screen_labels[i]
                    color = black
                    if (i == selected_option):
                        color = white
                    label = title_screen_option_font.render(title_screen_options[i], 1,color)
                    left = title_screen_options_left
                    top = title_screen_options_top + i * (title_screen_option_spacing + title_screen_options_width)
                    screen.blit(label, (left, top))
                
                screen.blit(title_label, (title_screen_left, title_screen_top))
                # game.draw(screen)
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
            if (game_state == GAME_STATES.PLAYING):
                elapsed_time_ms = time.get_ticks() - start_time_ms
                elapsed_time_s = elapsed_time_ms / 1000
                time_remaining_s = time_allowed_s - elapsed_time_s
                time_remaining_str = convert_to_time_string(time_remaining_s)
                if (time_remaining_s == 0):
                    game_state = GAME_STATES.GAME_OVER

            screen.fill(background_color)

            for b in all_buttons:
                b.draw(screen)


            countdown_label = puzzle_letter_font.render(str(time_remaining_str), 1, black)
            screen.blit(countdown_label, (countdown_left, countdown_top))

            game.draw(screen)

        pygame.display.flip()
                #clock.tick(20)

    pygame.quit ()

if __name__ == "__main__":
    main()
