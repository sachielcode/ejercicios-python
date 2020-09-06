import random


def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista



if __name__ == "__main__":
    tamano_lista = int(input('What is the size of the list? '))
    #objective = int(input('What number do you want to find? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    #print(lista)
    lista_ordenada = burbuja(lista)
    print(lista_ordenada)
    #print(f'El elemento {objective} {"esta" if encontrado else "no esta"} en la lista')