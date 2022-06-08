from random import *
from time import *


def number_guessing(x, y):  # game block
    phrases_too_much = ['Oh, too many! Try again', 'Too much!', "Wow, that's too much!",
                        'A lot of!', 'Take it lower', 'Need less!']
    phrases_too_little = ['Oh, too little! Try again', 'Too little!', "Uh, that's too little!",
                          'Little!', 'Take it higher', 'Need more!']
    phrases_almost = ['Almost guessed!', 'Already near', 'You are close', 'You are already there', 'Come on, almost',
                      'Hot!']
    phrases_guessed = ['Congratulations! You guessed my number :)',
                       'Well done! You guessed :)', 'Wow, you guessed it! :)']
    phrases_too_soon = ['Wow, so fast!', 'Yes, you are a magician! You guessed my number', 'Be honest, have you been watching?',
                        'You have great intuition!', "Even I couldn't guess that quickly!"]
    if x > y:
        x, y = y, x
        num_0 = randint(x, y)
        sleep(2)
        print('I guessed a number from', x, 'to', y, 'Try to guess!')
    else:
        num_0 = randint(x, y)
        sleep(2)
        print('I guessed a number from', x, 'to', y, 'Try to guess!')
    count = 0
    score = 50
    max_score = 0
    while True:
        num_1 = input()
        while num_1.isdigit() == False:
            num_1 = input('Please, enter the number ')
        num_1 = int(num_1)
        count += 1
        if num_1 == num_0:
            if count == 1:
                print('-' * 70)
                print('Incredible, got it right the first time!')
                print('-' * 70)
                print('Total attempts:', count)
                print(f'Score result: {score}')
                print('-' * 70)
                if input('Do you want to play again? Enter "yes" or "no" ').lower() in ['yes', 'y', 'lf', 'да', 'д']:
                    begin()
                else:
                    print('Come back when you want to play again :)')
                    break
            elif 1 <= count <= 5:
                print('-' * 70)
                print(choice(phrases_too_soon))
                print('-' * 70)
                print('Total attempts:', count)
                print(f'Score result: {score}')
                print('-' * 70)
                if input('Do you want to play again? Enter "yes" or "no" ').lower() in ['yes', 'y', 'lf', 'да', 'д']:
                    begin()
                else:
                    print('Come back when you want to play again :)')
                    break
            else:
                print('-' * 70)
                print(choice(phrases_guessed))
                print('-' * 70)
                print('Total attempts:', count)
                print(f'Score result: {score}')
                print('-' * 70)
                if input('Do you want to play again? Enter "yes" or "no" ').lower() in ['yes', 'y', 'lf', 'да', 'д']:
                    begin()
                else:
                    print('Come back when you want to play again :)')
                    break
        elif num_1 > num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_much),
                      choice(phrases_almost), sep='\n')
            else:
                print(choice(phrases_too_much))
        elif num_1 < num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_little),
                      choice(phrases_almost),  sep='\n')
            else:
                print(choice(phrases_too_little))
        score -= 5


def game_rules():  # game rules
    print('')
    print("Excellent! Let me tell you the rules of the game.")
    print("I will guess the whole number, and you will guess it.")
    print("You must enter a range of whole numbers in which I will guess the number")
    print("The range limits must not match! So we can't play.")
    input("Now write something to make sure you understand the rules of the game :)")


def begin():  # game launch
    x = input('Enter the first limit of the range: ')
    while x.isdigit() is False:
        print("It's not a whole number")
        x = input("Enter the new number. ")

    print('First border is ', x)
    y = input('Enter the second limit of the range: ')
    while x == y:
        print("You entered the same numbers. So you can't play :(")
        y = input("Enter a new second number. ")
    print('Second border is ', y)

    while y.isdigit() is False:
        print("It's not a whole number")
        y = input("Enter the new number. ")

    else:
        x, y = int(x), int(y)
        number_guessing(x, y)


    # welcome
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('I welcome you to the Trifidu program "Number Guessing"!')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print(' - - - - - - - - - - - - - - -- - - - - - - - -  - - - -')
if input("Would you like to play a game? Enter 'yes' or 'no'  ").lower() in ['yes', 'y', 'lf', 'да', 'д']:
    game_rules()
    begin()
else:
    if input("'It won't take much time and effort. If you decide, enter 'yes' :)  ").lower() in ['yes', 'y', 'lf', 'да', 'д']:
        game_rules()
        begin()
    else:
        sleep(1)
        print('Come back when you want to play :)')
