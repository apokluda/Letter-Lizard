#!/usr/bin/env python
# Import a library of functions called 'pygame'
import pygame
import random

# Initialize the game engine
pygame.init()

black = [ 0, 0, 0]
white = [255,255,255]
sky_blue = [  66,  136, 227]

# Set the height and width of the screen
size = [1000,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Letter Lizard")

clock = pygame.time.Clock()

#Loop until the user clicks the close button.
done = False

puzzle_letters = ['a', 'b', 'g', 'e', 'c', 'r', 'l', 's']
solutions = ['bag', 'bear', 'sear', 'lag', 'car']
square_width = 50
left_margin = 20
spacing = 30

correct_words_left = 800
correct_words_top = 100

puzzle_letter_font = pygame.font.SysFont("Arial", 30, bold=True)
guessed_letter_font = pygame.font.SysFont("Arial", 20, bold=True)

letter_pressed = ''
num_letters_pressed = 0

letters_guessed_left_margin = 20
letters_guessed_top_margin = 300
letters_guessed = []

words_guessed_correct = []

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
					words_guessed_correct.append(guessed_word)
					letters_guessed = []
				else:
					print "wrong"
				#print "hello"
			elif (event.key == pygame.K_BACKSPACE):
				if (len(letters_guessed) >= 1):
					del letters_guessed[len(letters_guessed) - 1]
			elif (event.key == pygame.K_SPACE):
				random.shuffle(puzzle_letters)
			elif (event.key in range(256)):
				letter = chr(event.key)
				letters_guessed.append(letter)
				num_letters_pressed += 1
			
	# ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


	# ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT


	# ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT 
			
	
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	
		
    # Set the screen background
	screen.fill(sky_blue)
	
	for i in range(len(letters_guessed)):
		letter = letters_guessed[i]
		x = letters_guessed_left_margin + i * square_width + i * spacing
		y = letters_guessed_top_margin
		letter_label = guessed_letter_font.render(letter, 1, black)
		pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 1)
		screen.blit(letter_label, (x + square_width/4, y + square_width/5))
	
	for i in range(len(puzzle_letters)):
		letter = puzzle_letters[i]
		x = left_margin + i * square_width + i * spacing
		y = 20
		letter_label = puzzle_letter_font.render(letter, 1, black)
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

