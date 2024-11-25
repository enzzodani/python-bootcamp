# TODO - Printar a palavra e os seus espaços
import random

word_list = ['Giovanna', 'Portal', 'Costa']

def blanket_word(list):
    chossen_word = random.choice(list).lower()
    print(chossen_word)

    temp = [ ]

    for letter in chossen_word:
        temp.append("_")

    b_word = " ".join(temp)
    return chossen_word,b_word

print(blanket_word(word_list))

# TODO2- Depois de um chute, colocar a letra que pertence a palavra no lugar dela 
def is_complete(blanket_word):
    for letter in blanket_word:
        if letter == "_":
            return 0
        else:
            continue

    return 1

def is_in_the_word(chossen_word, b_word):

def user_guess():
    guess = input("Make a letter guess: ").lower()



