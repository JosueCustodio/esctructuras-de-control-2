
# Ejercicio 3: Contar los dígitos de un número con while
def contar_digitos():
    num = int(input("Ingrese un número entero positivo: "))
    digitos = 0
    while num > 0:
        num //= 10
        digitos += 1
    print(f"El número tiene {digitos} dígitos.")

contar_digitos()