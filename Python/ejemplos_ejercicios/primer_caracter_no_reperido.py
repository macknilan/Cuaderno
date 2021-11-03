"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y

PRIMERA INSTANCIA DE UNA LETRA QUE NO SE REPITA
"""


def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (
                seen_letters[letter][0], seen_letters[letter][1] + 1)
        """
        "abacabad" # LO QUE SE ESCREIBE HASTA ESTE PUNTO
        {
            'a':(0,4),
            'b':(1,2),
            'c':(3,1),
        }
        """

    final_letters = []  # LAS LETRAS QUE SOLO VIMOS SOLO UNA VES Y EN QUE INDICE SE ENCUENTRA
    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append((key, value[0]))
            """
            "abacabad"
            [('a',0),('b',7)] # UNA LISTA DE TUPLAS
            """

    # lambda -> UNA FUNCION EN UNA LINEA
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
        """
        x = [('a',0),('b',7)]
        x[0][0] -> a
        x[1][0] -> b
        x[1][1] -> 7
        """
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
