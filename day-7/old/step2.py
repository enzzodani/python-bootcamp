# TODO - Printar a palavra e os seus espaços
import random

word_list = ['Giovanna', 'Portal', 'Costa']

def blanket_word(chossen_word):

    temp = ""
    number_of_letter = 0

    for letter in chossen_word:
        temp += "_ "

    return temp

def display(chossen_word, guess):
    display_word = ""

    for letter in chossen_word:
        if letter == guess:
            display_word += letter
        else:
            display_word += " _ "

    return display_word


def user_guess():
    guess = input("Make a letter guess: ").lower()
    return guess

if __name__ == "__main__":

    chossen_word = random.choice(word_list).lower()
    
    b_word = blanket_word(chossen_word)

    print(display(chossen_word, user_guess()))
