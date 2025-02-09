
import random

word_list = ['Giovanna', 'Portal', 'Costa']

def choice_word():

    chossen_word = random.choice(word_list).lower()

    temp = ""

    for letter in chossen_word:
        temp += " _ "

    return chossen_word, temp


def win(display_word, chossen_word):
    if display_word == chossen_word:
        return 1
    else:
        return 0

def game(display_word, chossen_word):
    guess = input("Make a letter guess: ").lower()

    for letter in chossen_word:
        if letter == guess:
            print(letter)
            display_word += letter
        else:
            display_word += " _ "


def main():
    chossen_word, display_word = choice_word()
    print(chossen_word)

    while win(display_word, chossen_word) == 0:
        game(display_word, chossen_word)
        print(display_word)

    print("You won")

if __name__ == "__main__":
    main()
