import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', "_", "+"]
print("Welcome to password generator in python")
length = int(input("Enter the length of the password: "))

# Calculating the number of characters for each type
nletters = random.randint(1, length - 2)
nsymbols = random.randint(1, length - nletters - 1)
nnumbers = length - nletters - nsymbols

# To Generate password
password_list = []
for i in range(nletters):
    password_list.append(random.choice(letters))
for i in range(nsymbols):
    password_list.append(random.choice(symbols))
for i in range(nnumbers):
    password_list.append(random.choice(numbers))

# Shuffles the password
random.shuffle(password_list)

# Converting the list to a string
password = ''.join(password_list)
print("Generated password:", password)
