import random

word_list = ['Giovanna', 'Portal', 'Costa']

# 1- Chosse a random word in word_list
# 2 - Make the user input a letter in lowercase
# 3 - Verify if the letter is in the word chossen

chossen_word = random.choice(word_list).lower()
user_guess = input("Make a letter guess: ").lower() # Todo - Make sure the input is a letter

for letter in chossen_word:
    if user_guess == letter:
        print("Right")
    else:
        print("Wrong")

