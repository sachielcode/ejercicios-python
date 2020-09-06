import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number do you want to find? '))

    list = [random.randint(0, 100) for i in range(list_size)]

    encontrado = busqueda_lineal(list, objective)
    print(list)
    print(f'The element {objective} {"esta" if encontrado else "no esta"} en la lista')