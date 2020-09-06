import random


def busqueda_binaria(lista, comienzo, final, objetivo):
    if comienzo >= final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)



if __name__ == "__main__":
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number do you want to find? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    encontrado = busqueda_binaria(list, 0, len(list), objective)

    print(list)
    print(f'El elemento {objective} {"esta" if encontrado else "no esta"} en la lista')