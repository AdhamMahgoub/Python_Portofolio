def calculator_logo():
  logo = """
   _____________________
  |  _________________  |
  | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
  | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
  |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
  | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
  | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
  | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
  | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
  | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
  | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
  | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
  | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
  |_____________________|
  """
  return logo
print(calculator_logo())

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2





operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}


def calculator():
  running = True
  n1 = float(input('What is the first number?: '))

  while running:
    operation_symbol = input('Pick an operation + - * /: ')
    calculation_function = operations[operation_symbol]
    n2 = float(input('What is the next number?: '))
    answer = calculation_function(n1, n2)


    print(f'{n1} {operation_symbol} {n2} = {answer}')


    test = input(f'type "y" to continue calculating with {answer}, "n" to start a new calculation or "s" to end the program: ')
    if test == 'y':
      running = True
      n1 = answer
    elif test == 'n':
      running = False
      calculator()
    elif test == 's':
      running = False
    else:
      print('incorrect input')

calculator()