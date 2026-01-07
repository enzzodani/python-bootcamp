import ./assets/art.py

auction = {}
big = 0

# Intro
print(art.logo)

# principal loop
while true:
    name = input("What is your name?:")
    auction[name] = input("What's your bid?: $")

    print("Are there any other bidders? Type 'yes' or 'no'.") 
    bin = input().lower()

    if bin = 'yes':
        continue
    elif bin = 'no':
        break
    else:
        print("Invalid answer. Please type 'yes' or 'no'.")
        # I need go to the bin validator again, i will repair this later

for key in auction:
    if auction[key] >= big:
        big = auction[key]
        winner = key
    else:
        continue

print(f"The winner is {winner} with a bid of ${big}.")
