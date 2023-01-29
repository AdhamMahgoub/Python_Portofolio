def auction_art_display():
    auction_art = '''
                                              88
                                        ,d    ""
                                        88
    ,adPPYYba, 88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,
    ""     `Y8 88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a
    ,adPPPPP88 88       88 8b           88    88 8b       d8 88       88
    88,    ,88 "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88
    `"8bbdP"Y8  `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88  '''


from replit import clear

bid_dict = {}
stop_or_continue = 'yes'
while stop_or_continue == 'yes':
    name = input("What is your name?: ")
    bid = int(input('What\'s tour bid?: $'))
    stop_or_continue = input('are there any other bids? Type \'yes\' or \'no\': ')
    bid_dict[name] = bid
    clear() #to delete the output terminal

max = 0
for key in bid_dict:
  if bid_dict[key] > max:
    max = bid_dict[key]

for key in bid_dict:
  if bid_dict[key] == max:
    print(f'the owner of the most bid is {name} with ${bid_dict[name]}')