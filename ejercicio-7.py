# Ejercicio 7: Imprimir números impares hasta el ingresado con while
def numeros_impares():
    num = int(input("Ingrese un número entero positivo: "))
    i = 1
    while i <= num:
        print(i)
        i += 2

numeros_impares()