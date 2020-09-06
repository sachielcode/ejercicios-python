import random


def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista [:medio]
        derecha = lista[medio:]

        # Llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
    return lista



if __name__ == "__main__":
    tamano_lista = int(input('What is the size of the list? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)