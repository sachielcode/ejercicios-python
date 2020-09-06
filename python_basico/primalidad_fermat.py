import random


def fermat(numero):
    aleatorio = random.randint(1, numero - 1)
    if numero <= 1:
        return False
    if aleatorio**(numero - 1) != 1:
        return False
    else:
        return True
        

def run():
    numero = int(input('Escribe un número: '))
    if fermat(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == "__main__":
    run()