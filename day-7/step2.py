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

# TODO2- Depois de um chute, colocar a letra que pertence a palavra no lugar dela 
def is_complete(blanket_word):
    for letter in blanket_word:
        if letter == "_":
            return 0
        else:
            continue

    return 1

def is_in_the_word(b_word,chossen_word, guess): 
    # Melhorar essa função para começar a substituir a b_word com as letras corretas
    for letter in chossen_word:
        if guess == letter:
            letter = guess
        else:
            continue
    

def user_guess():
    guess = input("Make a letter guess: ").lower()
    return guess

if __name__ == "__main__":

    chossen_word, b_word = blanket_word(word_list)

    while is_complete(b_word) != 1:
        guess = user_guess()


