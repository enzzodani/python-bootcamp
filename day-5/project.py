import random

# Array of letters (lowercase and uppercase)
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Array of numbers (0 to 9)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Array of common symbols
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", 
           "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/"]

print("Welcome to the password generator")

num_letter = int(input("How many letters do you want?"))
num_number = int(input("How many numbers do you want?"))
num_symbol = int(input("How many symbols do you want?"))

total_loops = num_symbol + num_number + num_letter
password = ""

while len(password) < total_loops:
    random_number = random.randint(1,3)    
    if random_number == 1 and num_letter != 0:
        password += random.choice(letters)
        num_letter -= 1
    elif random_number == 2 and num_number != 0:
        password += random.choice(numbers)
        num_number -= 1
    elif random_number == 3 and num_symbol != 0:
        password += random.choice(symbols)
        num_symbol -= 1

print(f"Your password is: {password}")

