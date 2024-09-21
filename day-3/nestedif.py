print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
    elif age >= 12 and age <= 18:
        price = 7
    else:
        if 45 <= age <= 55: 
            price = 0
        else:
            price = 12

    photo = input("Do you want a photo? y or n: ")

    if photo == "y":
        price+=3
    
    print(f"The total price is {price}")
else:
    print("You can't go.")
