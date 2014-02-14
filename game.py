import random
import game_generator.game_generator as gg
from config import *
class Game:
    def __init__(self):
        scramble, solutions = gg.generate_game('easy', 9)
        self.scramble = scramble
        self.solutions = solutions
        self.words_guessed_correct = []
        self.puzzle_letters = [l for l in scramble]
        self.puzzle_letters_displayed = self.puzzle_letters[:]
        self.letters_guessed = []
        self.current_score = 0
        self.words_guessed_correct = []
        self.message = ''
    
    def __guess_word(self, word):
        if ( word in self.solutions):
            if (word not in self.words_guessed_correct):
                self.words_guessed_correct.append(word)
                self.puzzle_letters_displayed = self.puzzle_letters[:]
                self.current_score += len(word)
                self.message = "Great!"
                self.letters_guessed = []
                #return True
            else:
                self.message = "You already guessed that word"
        else:
            self.message = "Incorrect word"
    
    def guess(self):
        self.__guess_word(''.join(self.letters_guessed))
        
    def process_backspace(self):
        self.message = ""
        if (len(self.letters_guessed) >= 1):
            letter_to_delete = self.letters_guessed[len(self.letters_guessed) - 1]
            del self.letters_guessed[len(self.letters_guessed) - 1]
            self.puzzle_letters_displayed[self.puzzle_letters_displayed.index('')] = letter_to_delete
    def shuffle(self):
        self.message = ""
        random.shuffle(self.puzzle_letters_displayed)
        
    def process_letter(self, letter):
        self.message = ""
        if (letter in self.puzzle_letters_displayed):
            self.letters_guessed.append(letter)
            self.puzzle_letters_displayed[self.puzzle_letters_displayed.index(letter)] = ''
    
    def draw(self, screen):
        your_score_label = puzzle_letter_font.render("Your score: " + str(self.current_score), 1, black)
        screen.blit(your_score_label, (correct_words_left, top_margin))
        
        status_label = puzzle_letter_font.render(self.message, 1, black)
        screen.blit(status_label, (status_label_left, status_label_top))

        
        for i in range(len(self.letters_guessed)):
            letter = self.letters_guessed[i]
            x = letters_guessed_left + i * square_width + i * spacing
            y = letters_guessed_top
            letter_label = guessed_letter_font.render(letter, 1, black)
            pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 1)
            screen.blit(letter_label, (x + square_width/4, y + square_width/5))
        
        for i in range(len(self.puzzle_letters_displayed)):
            letter = self.puzzle_letters_displayed[i]
            x = puzzle_letters_left + i * square_width + i * spacing
            y = puzzle_letters_top
            letter_label = puzzle_letter_font.render(letter, 1, black)
            if (letter != ''):
                pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 1)
            screen.blit(letter_label, (x + square_width/4, y + square_width/5))
            
        for i in range(len(self.words_guessed_correct)):
            word = self.words_guessed_correct[i]
            word_label = puzzle_letter_font.render(word, 1, black)
            #pygame.draw.rect(screen, black, (correct_words_left, correct_words_top ,square_width,square_width), 1)
            screen.blit(word_label, (correct_words_left, correct_words_top + i*square_width))