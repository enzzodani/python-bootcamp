print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? R$ "))

tip = float(input("How much tip would you like to give? 10, 12, or 15? "))/100

number_of_people = float(input("How many people to split the bill? "))

result = (bill + (bill*tip)) / number_of_people

print(f"Each person should pay: R$ {round(result, 2)}")
