import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#this can be added as a module to improve the readibility and organization of the code 
word_list = '''abruptly,
absurd,
abyss,
affix,
askew,
avenue,
awkward,
axiom,
azure,
bagpipes,
bandwagon,
banjo,
bayou'''.split()

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/              ''')
chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display.append('-')



lives_used = 0
while '-' in display and lives_used < 6:
    #guessing a different letter
    guess = input('please enter a guess ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives_used += 1
        print('Take Care!!!! the letter entered is not in the chosen word')
    print(HANGMANPICS[lives_used])
    print(display)
    print(f'you have {6 - lives_used} lives left')


if '-' in display:
    print('You Lost')
if '-' not in display:
    print('You Won')