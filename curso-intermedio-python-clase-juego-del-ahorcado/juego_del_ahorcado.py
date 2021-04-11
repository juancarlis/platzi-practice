'''
To-Do:

    1. Traer elementos de lista Data
    2. Seleccionar un elemento de forma aleatoria
    3. Tomar al elemento palabra y mostrar solo las letras que coincidan con las letras de una lista (las que el usuario adivine)

'''

import os
import random
from functools import reduce


def random_word_from_txt():

    list_of_data = []

    with open('archivos/data.txt', 'r', encoding='utf-8') as f:
        for line in f:

            list_of_data.append(line[:-1])

        return random.choice(list_of_data).upper()


def letter_in_guess_list(letter, guess_list):
    if letter in guess_list:
        return letter
    else:
        return '_'


def word_with_hiddens(word, guess_list):
    list_with_hiddens = list(
        map(lambda letter: letter_in_guess_list(letter, guess_list), word))

    return ' '.join(list_with_hiddens)


def check_if_win(word, guess_list):
    list_with_hiddens = list(map(lambda letter: letter in guess_list, word))

    if reduce(lambda x: x != False, list_with_hiddens):
        return 'You WIN!'

    else:
        return 'Keep trying...'


def run():
    running = True
    os.system('clear')
    my_guesses = []

    word_to_guess = random_word_from_txt()

    while running:

        print('¡Adivine la palabra! \n')
        print(word_with_hiddens(word_to_guess, my_guesses)+'\n')

        user_input = input('Ingrese una letra: ').upper()
        my_guesses.append(user_input)

        print(check_if_win(word_to_guess, my_guesses) + '\n')

        os.system('clear')


if __name__ == '__main__':
    run()
