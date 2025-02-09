
import random

word_list = ['Giovanna', 'Portal', 'Costa']

chossen_word = random.choice(word_list).lower()

temp = ""

for letter in chossen_word:
    temp += " _ "


display_word = ""
is_complete = 0

while is_complete == 0:
    guess = input("Make a letter guess: ").lower()

    is_complete = 1
    for letter in chossen_word:
        if letter == guess:
            display_word += letter
        else:
            display_word += " _ "
            is_complete = 0

    print(display_word)


