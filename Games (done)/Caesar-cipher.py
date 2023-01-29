def print_logo():
    print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
''')

def encode_or_decode(text,message,shift):
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    new_message = []

    if text == 'encode' or text == 'decode':
        for letter in message:
            if letter in letters: #to keep the symbols as is
                index = letters.index(letter)
                if text == 'encode':
                    new_message.append(letters[index + shift])
                elif text == 'decode':
                    new_message.append(letters[index - shift])
            else:
                new_message.append(letter)
        print(f'the {text}d message is: >>>> ', ''.join(new_message))
    else:
        print('incorrect input')

print_logo()
Running = 'yes'
while Running == 'yes':
    option = input('type "encode" or "decode": ')
    message = input('enter the message: ')
    shift = int(input('enter the shift: ')) % 26 #will make sure it stays inside the range
    encode_or_decode(option,message,shift)
    Running = input("Type yes if you want to go again: ")
    print(Running)