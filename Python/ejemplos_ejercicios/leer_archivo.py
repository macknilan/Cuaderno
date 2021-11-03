# -*- unicode: utf-8 -*-


def run():
    counter = 0
    with open('aleph.txt') as f:
        # print(f.readlines) # IMPRIME TODO EL TEXTO DEL ARCHIVO
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()
