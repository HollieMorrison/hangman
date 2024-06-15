

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
  print("Are you ready to play hangman?!")
  print(visual_hangman(lives))
  print(word_complete)
  print("\n")
while not guesses and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("You already guessed that letter", guess)
            elif guess not in word:
                print(guess, "is not in this word.")
                lives -= 1
                letters_guessed.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                letters_guessed.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(random_words)
                if "_" not in word_complete:
                    guesses = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                words_guessed.append(guess)
            else:
                guesses = True
                word_complete = word
        else:
            print("Not a valid guess, please try again.")
        print(visual_hangman(tries))
        print(word_complete)
        print("\n")
    if guesses:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")



















  def visual_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs, game is over, player loses.
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()