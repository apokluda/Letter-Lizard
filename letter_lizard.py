#!/usr/bin/env python
# Import a library of functions called 'pygame'
import pygame
import random
from pygame.locals import *
import pygbutton

class Letter:
	def __Letter__(self, letter):
		pass
		


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Initialize the game engine
pygame.init()

black = [ 0, 0, 0]
white = [255,255,255]
sky_blue = [  66,  136, 227]

# Set the height and width of the screen
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

buttons_top = int(0.8 * game_height)
buttons_left = left_margin



screen = pygame.display.set_mode(size)
pygame.display.set_caption("Letter Lizard")

clock = pygame.time.Clock()

#Loop until the user clicks the close button.
done = False


#hard code in a sample game
puzzle_letters = ['a', 'b', 'g', 'e', 'c', 'r', 'l', 's', 'g']
puzzle_letters_displayed = puzzle_letters[:] #make a copy of the array
solutions = ['bag', 'bear', 'sear', 'lag', 'car']


puzzle_letter_font = pygame.font.SysFont("Arial", puzzle_letter_font_size, bold=True)
guessed_letter_font = pygame.font.SysFont("Arial", guessed_letter_font_size, bold=True)

letter_pressed = ''
num_letters_pressed = 0


letters_guessed = []

words_guessed_correct = []

current_score = 0
game_status = ''

button_size = (50, 50)

all_buttons = []
button_main_menu = pygbutton.PygButton((button_size[0], button_size[1], buttons_left, buttons_top, 'Main Menu'))
all_buttons.append(button_main_menu)


while done == False:

	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
			# User pressed down on a key
		
		elif event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_RETURN):
				guessed_word = ''.join(letters_guessed)
				if ( guessed_word in solutions):
					if (guessed_word not in words_guessed_correct):
						words_guessed_correct.append(guessed_word)
						letters_guessed = []
						puzzle_letters_displayed = puzzle_letters[:]
						current_score += len(guessed_word)
					else:
						game_status = "You already found that word"
				else:
					game_status = "Incorrect"
					print "wrong"
				#print "hello"
			elif (event.key == pygame.K_BACKSPACE):
				if (len(letters_guessed) >= 1):
					letter_to_delete = letters_guessed[len(letters_guessed) - 1]
					del letters_guessed[len(letters_guessed) - 1]
					puzzle_letters_displayed[puzzle_letters_displayed.index('')] = letter_to_delete
			elif (event.key == pygame.K_SPACE):
				random.shuffle(puzzle_letters_displayed)
			elif (event.key in range(256)):
				letter = chr(event.key)
				if (letter in puzzle_letters_displayed):
					letters_guessed.append(letter)
					puzzle_letters_displayed[puzzle_letters_displayed.index(letter)] = ''
					num_letters_pressed += 1
			elif 'click' in button_main_menu.handleEvent(event):
				#windowBgColor = WHITE
			
	# ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


	# ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT


	# ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT 
			
	
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	
		
    # Set the screen background
	screen.fill(sky_blue)
	
	your_score_label = puzzle_letter_font.render("Your score: " + str(current_score), 1, black)
	screen.blit(your_score_label, (correct_words_left, top_margin))
	
	status_label = puzzle_letter_font.render(game_status, 1, black)
	screen.blit(status_label, (status_label_left, status_label_top))
	
	for i in range(len(letters_guessed)):
		letter = letters_guessed[i]
		x = letters_guessed_left + i * square_width + i * spacing
		y = letters_guessed_top
		letter_label = guessed_letter_font.render(letter, 1, black)
		pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 1)
		screen.blit(letter_label, (x + square_width/4, y + square_width/5))
	
	for i in range(len(puzzle_letters_displayed)):
		letter = puzzle_letters_displayed[i]
		x = puzzle_letters_left + i * square_width + i * spacing
		y = puzzle_letters_top
		letter_label = puzzle_letter_font.render(letter, 1, black)
		if (letter != ''):
			pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 1)
		screen.blit(letter_label, (x + square_width/4, y + square_width/5))
		
	for i in range(len(words_guessed_correct)):
		word = words_guessed_correct[i]
		word_label = puzzle_letter_font.render(word, 1, black)
		#pygame.draw.rect(screen, black, (correct_words_left, correct_words_top ,square_width,square_width), 1)
		screen.blit(word_label, (correct_words_left, correct_words_top + i*square_width))
    # Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(20)
            
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

