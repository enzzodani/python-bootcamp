# TODO - Printar a palavra e os seus espaços
import random

word_list = ['Giovanna', 'Portal', 'Costa']

def blanket_word(list):
    chossen_word = random.choice(list).lower()
    print(chossen_word)

    temp = [ ]
    number_of_letter = 0

    for letter in chossen_word:
        temp.append("_")
        number_of_letter += 1

    b_word = " ".join(temp)
    return chossen_word,b_word, number_of_letter

# TODO2- Depois de um chute, colocar a letra que pertence a palavra no lugar dela 
def is_complete(blanket_word):
    for letter in blanket_word:
        if letter == "_":
            return 0
        else:
            continue

    return 1

def is_in_the_word(chossen_word, guess): 

    return chossen_word.find(guess)

def sub (b_word, letter, position):
    print("sub function inside")
    print("Letter:" + str(letter) + " ,Position:" + str(position))
    print("blanked: " + b_word + " / blanked position: " + b_word[position])

    if b_word[position] == "_":
        print("inside if sub function")
        b_word = b_word[:position] + letter + b_word[position+1:]
        print(b_word)
        # b_word[position] = letter
        return b_word
    else:
        return None

def user_guess():
    guess = input("Make a letter guess: ").lower()
    return guess

if __name__ == "__main__":

    chossen_word, b_word, number_of_letter = blanket_word(word_list)

    while is_complete(b_word) != 1:
        guess = user_guess()
        position = is_in_the_word(chossen_word, guess)
        if position != -1:
            sub(b_word, guess, position)
            
        print(b_word)


