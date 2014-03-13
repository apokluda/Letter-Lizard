#!/usr/bin/python

from __future__ import print_function
from __future__ import with_statement
import argparse
import fileinput
import random
import os

# Parameters:
# Difficulty: 'easy', 'medium', 'hard', or 'insane'
# Game size (number of scrambled letters)
# Number of games to generate

# Dictionaries to Load (lists are cumulative, so when loading
# dictionaries for the 'medium' dictionaries, the 'easy' dictionaries
# must be loaded too):
# 'easy'
#   - english-words.10
#   - engilsh-words.20
#   - english-words.35
#   - canadian-words.10
#   - canadian-words.20
#   - canadian-words.35
# 'medium'
#   - english-words.40
#   - engilsh-words.50
#   - canadian-words.40
#   - canadian-words.50
# 'hard'
#   - english-words.55
#   - english-words.60
#   - eniglsh-words.70
#   - canadian-words.55
#   - canadian-words.60
#   - canadian-words.70
# 'insane'
#   - english-words.80
#   - engilsh-words.95
#   - canadian-words.80
#   - canadian-words.95

# Algorithm Analysis:
#
# Number of words in each dictionary set:
# easy:    49,762
# medium:  80,541
# hard:   135,539
# insane: 501,002
#
# Number of possible 'words' that could be formed from a set of letters:
# 6 letters:          1,956
# 7 letters:         13,699
# 8 letters:        109,600
# 9 letters:        986,409
# 10 letters:     9,864,100
# 11 letters:   108,505,111
# 12 letters: 1,302,061,344
#
# There are two ways to find all the valid dictionary words that
# can be generated from a set of scrambled letters: 1) generate all possible
# combinations of a subset of letters and check if that combination of
# letters is in the dictionary, or 2) iterate over the dictioray and see
# if each word can be generated using the letters from the scrambled set.
# From the numbers above, we can see that the number of possible combinations
# of letters grows very fast with increasing size of the set of letters (O(n!)),
# whereas the dictionary is limited to 501,002 words maximum (O(501,002) = O(1)).
# Thus, we take the second approach, becasue it takes O(1) time no matter what
# the size of the set of scrambled letters.

# Counting the Frequency of each Letter:
#
# When generating the set of scrambled letters, we choose the letters with a 
# probabliliy equal to the frequency that they appear in the dictionaries.
# For example, about 7% of the letters in the dictionary are A's, so when
# generating the scrambled letters, we choose A with 7% probability. The following
# code calculates the cumulative frequency of each letter in the dictionary
# which is used in the algorithm that picks the scrambled letters. Rather than
# run it everytime (since the frequencies don't change), it has been commented
# out and the result has been hard coded. [As a side note: the letter frequency
# is almost identical across each dictionary set, i.e. 'easy,' 'medium', 'hard'
# 'insane'.]
#
#class LetterCounter:
#    letter_counts = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
#    'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0,
#    'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
#    total_letters = 0
#    
#    def count_word(self, word):
#        for c in word.upper():
#            try:
#                self.letter_counts[c] += 1
#                self.total_letters += 1
#            except KeyError:
#                pass
#
#    def letter_frequency(self):
#        letter_frequencies = {}
#        for k, v in self.letter_counts.items():
#            letter_frequencies[k] = v / self.total_letters
#        return letter_frequencies
#
#lc = LetterCounter()
#with fileinput.input(files=dicts[args.difficulty],openhook=fileinput.hook_encoded("iso-8859-1")) as f:
#    for line in f:
#        lc.count_word(line)
#
#print(lc.letter_counts)
#letter_frequency = lc.letter_frequency()
#cumulative_frequency = 0.0
#for k in sorted(lc.letter_frequency().keys()):
#    cumulative_frequency += letter_frequency[k]
#    print("'{}': {},".format(k, cumulative_frequency))

# Cumulative frequency of each letter in 'easy' dictionaries
letter_frequencies = [
('A', 0.07121085473733121),
('B', 0.0886732846287687),
('C', 0.12884066132482141),
('D', 0.1681822658481337),
('E', 0.28295197137323136),
('F', 0.29740424704477103),
('G', 0.3291699600750519),
('H', 0.3502511408029941),
('I', 0.43492688002060653),
('J', 0.4367501445732628),
('K', 0.44577303134146323),
('L', 0.4940870166896891),
('M', 0.5199283825724194),
('N', 0.5912680274651321),
('O', 0.6494331970514632),
('P', 0.6783453242860356),
('Q', 0.6802519236451151),
('R', 0.7523340059041449),
('S', 0.8587273007351142),
('T', 0.9292841035068803),
('U', 0.9613730545741971),
('V', 0.9718025318629371),
('W', 0.9809643099751765),
('X', 0.9835451636771358),
('Y', 0.9970251999404032),
('Z', 1.0),
]

dd = os.path.dirname(os.path.realpath(__file__)) + "/../scowl-7.1/final/"

dicts = {'easy': [dd+"english-words.10", dd+"english-words.20", dd+"english-words.35",
        dd+"canadian-words.10", dd+"canadian-words.20", dd+"canadian-words.35"]}
dicts['medium'] = [dd+"english-words.40", dd+"english-words.50", 
        dd+"canadian-words.40", dd+"canadian-words.50"] + dicts['easy']
dicts['hard'] = [dd+"english-words.55", dd+"english-words.60", dd+"english-words.70",
        dd+"canadian-words.55", dd+"canadian-words.60", dd+"canadian-words.70"] + dicts['medium']
dicts['insane'] = [dd+"english-words.80", dd+"english-words.95",
        dd+"canadian-words.80", dd+"canadian-words.95"] + dicts['hard']

def generate_scramble(num):
    """Generate a set of scrambled letters."""
    seq = ""
    for i in range(num):
        x = random.uniform(0, 1)
        for k, v in letter_frequencies:
            if x < v:
                seq += k
                break
    return seq

def make_letter_count(s):
    """Create a hash table maping each letter to the number of times that it occurs in the string s"""
    lc = {}
    for l in s:
        try:
            lc[l] += 1
        except KeyError:
            lc[l] = 1
    return lc

def can_make_word(letter_count, word):
    """Determine if word can be formed from the letters in the letter_count map"""
    letter_count = letter_count.copy()
    for l in word:
        try:
            letter_count[l] -= 1
            if letter_count[l] < 0:
                return False
        except KeyError:
            return False
    return True

def generate_game(difficulty, size=6, num=1):
    words = []
    for line in fileinput.input(files=dicts[difficulty],openhook=fileinput.hook_encoded("iso-8859-1")):
        word = line.strip().upper()
        if len(word) > 2:
            words.append(word)
    while True:
        scramble = generate_scramble(size)
        letter_count = make_letter_count(scramble)
        soln = []
        for word in words:
            if can_make_word(letter_count, word):
                soln.append(word)
        if len(soln) > 3:
            return (scramble, soln)

def compare_words(word1, word2):
    if (len(word1) < len(word2)):
        return -1
    elif (len(word1) > len(word2)):
        return 1
    elif word1 < word2:
        return -1
    elif word1 > word2:
        return 1
    else:
        return 0

class OutputFormatter:
    def beginOutput(self):
        pass
    
    def output(self, scramble, words):
        pass
    
    def endOutput(self):
        pass

class PlainFormatter(OutputFormatter):
    def output(self, scramble, words):
        print(scramble, *words)

class JavaScriptFormatter(OutputFormatter):
    def beginOutput(self):
        print("games = [")
    
    def output(self, scramble, words):
        print("{letters: '", scramble, "', words: ['", sep='', end='')
        print(*words, sep="', '", end="']},\n")
    
    def endOutput(self):
        print("];")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "difficulty", 
            type=str,
            choices=["easy", "medium", "hard", "insane"],
            default="easy",
            nargs="?",
            help="level of difficulty")
    parser.add_argument(
            "-s", "--size",
            type=int,
            default=6,
            help="the number of scrambled letters in the game")
    parser.add_argument(
            "-n", "--num",
            type=int,
            default=1,
            help="the number of games to generate")
    parser.add_argument(
            "-m", "--markup",
            type=str,
            choices=["plain", "JavaScript"],
            default="plain",
            help="the markup language to use for output")
    args = parser.parse_args()
    formatter = OutputFormatter()
    if args.markup == "plain":
        formatter = PlainFormatter()
    elif args.markup == "JavaScript":
        formatter = JavaScriptFormatter()
    formatter.beginOutput()
    for i in range(args.num):
        scramble, words = generate_game(args.difficulty, args.size)
        formatter.output(scramble, sorted(words, cmp=compare_words))
    formatter.endOutput()
