import random
import images

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0,len(word_list)-1)]
lives = 6

display = []

for i in range(len(chosen_word)):
    display += '_'
print(' '.join(display))

while '_' in display:
    print(lives)
    print(images.stages[lives])
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(' '.join(display))
    if lives == 0:
        break

