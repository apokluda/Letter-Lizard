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
parser.add_argument("difficulty", type=str, choices=["easy", "medium", "hard", "insane"], default="easy", nargs="?", help="level of difficulty")
parser.add_argument("-s", "--size", type=int, default=6, help="the number of scrambled letters in the game")
parser.add_argument("-n", "--num", type=int, default=1, help="the number of games to generate")
args = parser.parse_args()

dd = "scowl-7.1/final/"

dicts = {'easy': [dd+"english-words.10", dd+"english-words.20", dd+"english-words.35", dd+"canadian-words.10", dd+"canadian-words.20", dd+"canadian-words.35"]}
dicts['medium'] = [dd+"english-words.40", dd+"english-words.50", dd+"canadian-words.40", dd+"canadian-words.50"] + dicts['easy']
dicts['hard'] = [dd+"english-words.55", dd+"english-words.60", dd+"english-words.70", dd+"canadian-words.55", dd+"canadian-words.60", dd+"canadian-words.70"] + dicts['medium']
dicts['insane'] = [dd+"english-words.80", dd+"english-words.95", dd+"canadian-words.80", dd+"canadian-words.95"] + dicts['hard']

count = 0
with fileinput.input(files=dicts[args.difficulty]) as f:
    for line in f:
        count += 1
print(count)
