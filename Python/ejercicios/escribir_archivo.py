# -+- unicode: utf-8 -*-


def run():
    with open('numeros.txt', 'w') as f:  # SE CREA EL ARCHIVO SI NO EXISTE O LO SOBRE ESCRIBE
        for i in range(10):
            f.write('i -> {} \n'.format(i))
            # f.write('{}'.format(i))


if __name__ == '__main__':
    run()
