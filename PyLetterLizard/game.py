import random
import game_generator as gg
from config import *

class Game:
    def __init__(self, difficulty):
        scramble, solutions = gg.generate_game(difficulty.lower())
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
        word_lengths = [len(w) for w in words]
        return dict([(length, word_lengths.count(length)) for length in set(word_lengths)])
            
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
        status_label = puzzle_letter_font.render(self.message, 1, black)
        screen.blit(status_label, (status_label_left, status_label_top))
        score_label = default_font.render("Score: " + str(self.current_score), 1, black)
        screen.blit(score_label, (score_left, score_top))
        for i in range(len(self.letters_guessed)):
            letter = self.letters_guessed[i]
            x = letters_guessed_left + i * square_width + i * spacing
            y = letters_guessed_top
            letter_label = guessed_letter_font.render(letter, 1, black)
            pygame.draw.rect(screen, white, (x, y ,square_width,square_width), 0)
            pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 3)
            screen.blit(letter_label, (x + square_width/4, y + square_width/5))
        
        for i in range(len(self.puzzle_letters_displayed)):
            letter = self.puzzle_letters_displayed[i]
            x = puzzle_letters_left + i * square_width + i * spacing
            y = puzzle_letters_top
            letter_label = puzzle_letter_font.render(letter, 1, black)
            if (letter != ''):
                pygame.draw.rect(screen, white, (x, y ,square_width,square_width), 0)
                pygame.draw.rect(screen, black, (x, y ,square_width,square_width), 3)
            screen.blit(letter_label, (x + square_width/4, y + square_width/5))

        words_to_write = []
        for length in sorted(self.length_counts.keys()):
            count = self.length_counts[length]
            for word in self.words_guessed_correct_by_length[length]:
                words_to_write.append(word)
            for j in range(count - len(self.words_guessed_correct_by_length[length])):
                hyphens = '- ' * length
                words_to_write.append(hyphens)
        for i in range(len(words_to_write)):
            word = words_to_write[i]
            label = default_font.render(word, 10, black)
            column = i / solved_words_column_length
            row = i % solved_words_column_length
            left = solved_words_region_left +  column * ( solved_words_column_width + solved_words_column_padding)
            top = solved_words_region_top + row * (solved_words_height + solved_words_column_padding)
            screen.blit(label, (left, top))
            
def main():
    game = Game()
    print sorted(game.solutions, key = lambda w : len(w))
    print game.length_counts

if __name__ == '__main__':
    main()
        
