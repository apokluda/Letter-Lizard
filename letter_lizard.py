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
	
def exit():
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
	game_state = GAME_STATES.PLAYING
	all_buttons = []
	button_main_menu = pygbutton.PygButton((buttons_left, buttons_top, button_size[0], button_size[1]), 'Main Menu')
	button_exit = pygbutton.PygButton((buttons_left + button_padding + button_size[0], buttons_top, button_size[0], button_size[1]), 'Exit')
	button_new_game = pygbutton.PygButton((buttons_left + 2*(button_padding + button_size[0]), buttons_top, button_size[0], button_size[1]), 'New Game')
	all_buttons.append(button_main_menu)
	all_buttons.append(button_exit)
	all_buttons.append(button_new_game)
	
	
	new_game()
	while done == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				done = True
			elif 'click' in button_exit.handleEvent(event):
				exit()
			elif 'click' in button_new_game.handleEvent(event):
				new_game()
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
					
		if (game_state == GAME_STATES.PLAYING):
			elapsed_time_ms = time.get_ticks() - start_time_ms
			elapsed_time_s = elapsed_time_ms / 1000
			time_remaining_s = time_allowed_s - elapsed_time_s
			time_remaining_str = convert_to_time_string(time_remaining_s)
			if (time_remaining_s == 0):
				game_state = GAME_STATES.GAME_OVER
	
		screen.fill(sky_blue)
		
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

