import random
import re

words = ["abc", "def", "ghaba"]
lives_left = 5

word = random.choice(words)
guessed = ['_'] * len(word)

while '_' in guessed:
    ch = input(f"Lives left: {lives_left}. Guess the letter: {''.join(guessed)}\n")
    found = False
    for match in re.finditer(ch, word):
        found = True
        guessed[match.start()] = word[match.start()]

    if not found:
        lives_left -= 1
        print(f'{ch} not found')

print('You guessed the word!')
