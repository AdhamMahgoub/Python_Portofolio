import random

letterslist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numberslist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolslist = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Pypassword Generator!\n')

print('How many letters?')
letters = int(input())
print('How many symbols?')
symbols = int(input())
print('how many numbers? ')
numbers = int(input())

for trials in range(50): #possible combinations

    password = []

    countletters = 0
    countsymbols = 0
    countnumbers = 0

    i = 0
    while i < (letters + symbols + numbers):
        j = random.randint(1,3)
        if j == 1 and countnumbers < numbers:
            password.append(random.choice(numberslist))
            countnumbers += 1
            i += 1
        elif j == 2 and countletters < letters:
            password.append(random.choice(letterslist))
            countletters += 1
            i += 1

        elif j == 3 and countsymbols < symbols:
            password.append(random.choice(symbolslist))
            countsymbols += 1
            i += 1
        # else:
            # print('error')
            # print(f'j = {j}')
            # print("test", countsymbols, countnumbers, countletters)

    password = ''.join(password)
    print(f'Here is your password: {password}')