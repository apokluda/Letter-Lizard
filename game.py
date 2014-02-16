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
        self.message = ''
        self.length_counts = self.__find_length_counts(solutions)
        self.words_guessed_correct_by_length = {k : [] for k in self.length_counts.keys()}
        self.words_guessed_correct = set([])
    
    def __guess_word(self, word):
        if ( word in self.solutions):
            if (word not in self.words_guessed_correct):
                self.words_guessed_correct_by_length[len(word)].append(word)
                self.puzzle_letters_displayed = self.puzzle_letters[:]
                self.current_score += len(word)
                self.message = "Great!"
                self.letters_guessed = []
                self.words_guessed_correct.add(word)
            else:
                self.message = "You already guessed that word"
        else:
            self.message = "Incorrect word"
        print self.words_guessed_correct_by_length
            
    def __partition_words_by_length(self, words):
        lengths_to_words = {}
        for w in words:
            n = len(w)
            if n not in lengths_to_words:
                lengths_to_words[n] = [w]
            else:
                lengths_to_words[n].append(w)
        return lengths_to_words
    
    def __find_length_counts(self, words):
        lengths_to_counts = {}
        for w in words:
            n = len(w)
            if n not in lengths_to_counts:
                lengths_to_counts[n] = 1
            else:
                lengths_to_counts[n] += 1
        return lengths_to_counts
            
    
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
            
#         for i in range(len(self.words_guessed_correct)):
#             word = self.words_guessed_correct[i]
#             word_label = puzzle_letter_font.render(word, 1, black)
#             #pygame.draw.rect(screen, black, (correct_words_left, correct_words_top ,square_width,square_width), 1)
#             screen.blit(word_label, (correct_words_left, correct_words_top + i*square_width))
#
        i = 0
        for length in sorted(self.length_counts.keys()):
            count = self.length_counts[length]
            for word in self.words_guessed_correct_by_length[length]:
                word_label = default_font.render(word, 1, black)
                screen.blit(word_label, (correct_words_left, correct_words_top + i*square_width))
                i += 1
            for j in range(count - len(self.words_guessed_correct_by_length[length])):
                hyphens = '- ' * length
                word_label = default_font.render(hyphens, 1, black)
                cw_top = correct_words_top1
                cw_left = correct_words_left1
                if (cw_top + 10 > game_height):
                    cw_left = correct_words_left2
                    cw_top = correct_words_top2
                    i = 0
                left = correct_words_left1
                top = correct_words_top1 + i*square_width

                screen.blit(word_label, (correct_words_left, correct_words_top + i*square_width))
                i += 1
                
def main():
    game = Game()
    print sorted(game.solutions, key = lambda w : len(w))
    print game.length_counts
    

if __name__ == '__main__':
    main()
        