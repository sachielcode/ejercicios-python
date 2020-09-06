def run():
    opcion = 0
    while opcion != 4:
        menu = """
Bienvenido al conversor de monedas 🤑

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos
4 - Salir

Elige una opción: """
        opcion = input(menu)

        def conversion(pesos, valor_dolar):
            dolares = pesos / valor_dolar
            dolares = round(dolares, 2)
            dolares = str(dolares)
            print("Tienes $" + dolares + " dólares")

        if opcion == '1':
            pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
            valor_dolar = 22.28
            conversion(pesos, valor_dolar)
        elif opcion == '2':
            pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
            valor_dolar = 3733.33
            conversion(pesos, valor_dolar)
        elif opcion == '3':        
            pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
            valor_dolar = 72.38
            conversion(pesos, valor_dolar)
        elif opcion == '4':
            break
        else:
            print("Elige una opción válida: ")
            continue

if __name__ == "__main__":
    run()