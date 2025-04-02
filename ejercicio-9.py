# Ejercicio 9: Factorial de un número con while
def factorial_while():
    num = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print(f"El factorial es {factorial}.")

factorial_while()