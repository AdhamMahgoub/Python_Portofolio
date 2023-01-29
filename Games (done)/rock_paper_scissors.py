import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game_images = [rock, paper, scissors]
print("The Game Started")

while True:
    print('What do you choose?' + '''
            0 for Rock
            1 for Paper
            2 for Scissors''')
    my_choice = int(input())
    if my_choice < 3 and my_choice >= 0:
        print(game_images[my_choice])

        comp_choice = random.randint(0, 2)
        print("the computer chose: \n", game_images[comp_choice])

        if my_choice == comp_choice:
            print("draw")

        if my_choice == 0 and comp_choice == 2:
            print('You Won')
        if my_choice == 2 and comp_choice == 0:
            print('You Lost')

        if my_choice == 1 and comp_choice == 0:
            print('You Won')
        if my_choice == 0 and comp_choice == 1:
            print('You Lost')

        if my_choice == 2 and comp_choice == 1:
            print('You Won')
        if my_choice == 1 and comp_choice == 2:
            print('You Lost')

    else:
        print("invalid number")
    print("\n")