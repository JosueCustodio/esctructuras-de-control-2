# Ejercicio 1: Mostrar números del 1 hasta el ingresado con while
def mostrar_numeros():
    num = int(input("Ingrese un número entero positivo: "))
    i = 1
    while i <= num:
        print(i)
        i += 1
mostrar_numeros()
