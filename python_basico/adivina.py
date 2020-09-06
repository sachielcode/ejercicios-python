import random


def adivina(numero, respuesta):
    if numero == respuesta:
        print('Felicidades, Adivinaste el núnero!!! 🎉🎉🎉 ')
        return True
    elif numero > respuesta:
        print('El número es mayor a ' + str(respuesta))
        return False
    elif numero < respuesta:
        print('El número es menor a ' + str(respuesta))
        return False
        

def run():
    numero = random.randint(1, 100)
    es_correcto = False
    while es_correcto == False:
        respuesta = int(input('Adivina el número: '))
        es_correcto = adivina(numero, respuesta)



if __name__ == "__main__":
    run()