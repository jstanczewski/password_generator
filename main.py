import random
from string import ascii_letters, punctuation, digits


def generate_password():
    while True:
        length = int(input('Type the length of Your desired password. '))
        user_choice = input('Do You want Your password to include digits and punctuation marks? [Y/N] ')
        choice = ascii_letters
        if user_choice.upper() == 'Y':
            choice += punctuation + digits
        password = ''
        for i in range(length):
            password += choice[random.randint(0, len(choice) - 1)]
        print(f'Your randomly generated password: {password}')
        if input('Do You want to generate another password? [Y/N] ').upper() != 'Y':
            break


generate_password()
