# implement phonetic matching for a given word and set of words

import sys
import re

# read in the word and the list of words
word = "Moorthy"
#words = sys.argv[2:]
with open('words.txt') as f:
    words = f.read().splitlines()


# create a dictionary of phonetic codes
phonetic_codes = {
    'b': '1',
    'f': '1',
    'p': '1',
    'v': '1',
    'c': '2',
    'g': '2',
    'j': '2',
    'k': '2',
    'q': '2',
    's': '2',
    'x': '2',
    'z': '2',
    'd': '3',
    't': '3',
    'l': '4',
    'm': '5',
    'n': '5',
    'r': '6'
}

# create a function to convert a word to a phonetic code
def word_to_phonetic_code(word):
    # convert word to lower case
    word = word.lower()
    # remove non-alphabetic characters
    word = re.sub('[^a-z]', '', word)
    # convert word to phonetic code
    code = ''
    for letter in word:
        if letter in phonetic_codes:
            code += phonetic_codes[letter]
    # remove duplicates
    code = re.sub(r'(\d)\1+', r'\1', code)
    return code

# convert the word to a phonetic code
word_code = word_to_phonetic_code(word)

# find the words that match the phonetic code
matches = []
for w in words:
    w_code = word_to_phonetic_code(w)
    if w_code == word_code:
        matches.append(w)

# print the matches
print(' '.join(matches))