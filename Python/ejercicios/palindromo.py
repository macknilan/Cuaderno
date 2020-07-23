# -*- coding: utf-8 -*-
"""palindromo.py"""


def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False
    # return reversed_word


if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('{} Si es un palindromo.'.format(word))
    else:
        print('{} Si no es palindromo.'.format(word))


    # print('Palabra {} ').format(result)

    # reves = []
    # for letter in 'Python':
    #     reves.insert(0, letter)

    #     print ('Current Letter {}: {}').format(letter, reves)
