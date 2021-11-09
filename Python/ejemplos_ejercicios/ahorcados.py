# -*- coding: utf-8 -*-
"""ahorcados.py"""


import random

# CUANDO UNA VARIALBE ESTA EN MAYUSCULA ES UNA CONSTANTE
IMAGES = [
    """

    +---+
    |   |
        |
        |
        |
        |
        =========""",
    """

    +---+
    |   |
    O   |
        |
        |
        |
        =========""",
    """

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========""",
    """

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========""",
    """

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========""",
    """

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========""",
    """

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========""",
    """

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========""",
    """
""",
]

# CUANDO UNA VARIALBE ESTA EN MAYUSCULA ES UNA CONSTANTE
WORDS = ["rodolfo", "puerta", "ordenador", "abogado", "codigo", "carro"]


def random_word():  # SELECCIONAR UNA PALABRA DE LA LISTA "WORD"
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries] + "\n")
    print(hidden_word)
    print("\n" + "--- * --- * --- * --- * --- * ---" + "\n")


def run():
    word = random_word()
    hidden_word = ["-"] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input("Escoje una letra: "))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print("\n")
                print("Perdiste! La pralabra correcta era: {}".format(word))
                break

        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []

        try:
            hidden_word.index("-")
            pass
        except ValueError:
            print("\n !GANASTE¡ La palabra es {} ".format(word))
            break


if __name__ == "__main__":
    print("B I E N V E N I D O S  A  A H O R C A D O S")
    run()
