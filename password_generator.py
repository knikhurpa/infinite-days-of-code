#Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

# Ask user for number of letters, symbols and numbers in the password and then validate the input using try except block 
while True:
    try:
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        break
    except:
        print("Please enter a valid number!")
while True:
    try:
        nr_symbols = int(input(f"How many symbols would you like?\n")) 
        break
    except:
        print("Please enter a valid number!")

while True:
    try:
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        break
    except:
        print("Please enter a valid number!")


password_list = []

# Loop over letters list to randomly select letters for specified number of times
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Loop over symbols list 
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Loop over numbers list
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list and join it into a string
random.shuffle(password_list)

print(''.join(password_list))
