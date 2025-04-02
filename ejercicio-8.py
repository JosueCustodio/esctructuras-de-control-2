# Ejercicio 8: Serie de Fibonacci hasta el enésimo término con for
def fibonacci():
    n = int(input("Ingrese un número entero positivo: "))
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci()