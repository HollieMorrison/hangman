

import random
from vocab import random_words

def get_word():
  word = random.choice()
  return word.upper()


def run(word):
  word_complete = "_" * len(word)
  guesses = False
  letters_guessed = []
  words_guessed = []
  lives = 6