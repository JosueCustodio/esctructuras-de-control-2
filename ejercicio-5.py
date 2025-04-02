# Ejercicio 5: Contar en orden descendente hasta 0 con while
def cuenta_regresiva():
    num = int(input("Ingrese un número entero: "))
    while num >= 0:
        print(num)
        num -= 1

cuenta_regresiva()