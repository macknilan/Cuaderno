"""
Script de loop de espera.
"""

import time


def loop_de_espera():
    loop_espera = "-\|/"
    idx = 0
    while True:
        print(loop_espera[idx % len(loop_espera)], end="\r")
        idx += 1
        time.sleep(0.1)

        if idx == len(loop_espera):
            idx = 0

        # Verificar el valor del incide de loop_espera
        print(f'   idx: {idx}', end='\r')


if __name__ == "__main__":
    loop_de_espera()
