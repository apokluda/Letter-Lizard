#!/usr/bin/python3

import argparse
import fileinput

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
args = parser.parse_args()

dd = "scowl-7.1/final/"

dicts = {'easy': [dd+"english-words.10", dd+"english-words.20", dd+"english-words.35",
        dd+"canadian-words.10", dd+"canadian-words.20", dd+"canadian-words.35"]}
dicts['medium'] = [dd+"english-words.40", dd+"english-words.50", 
        dd+"canadian-words.40", dd+"canadian-words.50"] + dicts['easy']
dicts['hard'] = [dd+"english-words.55", dd+"english-words.60", dd+"english-words.70",
        dd+"canadian-words.55", dd+"canadian-words.60", dd+"canadian-words.70"] + dicts['medium']
dicts['insane'] = [dd+"english-words.80", dd+"english-words.95",
        dd+"canadian-words.80", dd+"canadian-words.95"] + dicts['hard']

class LetterCounter:
    letter_counts = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
    'J':0, 'K':0, 'L':0, 'M':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0,
    'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    total_letters = 0
    
    def count_word(self, word):
        for c in word.upper():
            try:
                self.letter_counts[c] += 1
                self.total_letters += 1
            except KeyError:
                pass

    def letter_frequency(self):
        letter_frequencies = {}
        for k, v in self.letter_counts.items():
            letter_frequencies[k] = v / self.total_letters
        return letter_frequencies

lc = LetterCounter()
with fileinput.input(files=dicts[args.difficulty],openhook=fileinput.hook_encoded("iso-8859-1")) as f:
    for line in f:
        lc.count_word(line)
        
print(lc.letter_counts)
letter_frequency = lc.letter_frequency()
for k in sorted(lc.letter_frequency().keys()):
    print("'{}': {},".format(k, letter_frequency[k]))
