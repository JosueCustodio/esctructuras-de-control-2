# Ejercicio 10: Solicitar contraseña hasta que sea correcta
def solicitar_contrasena():
    contrasena_correcta = "294533"  
    contrasena = ""
    while contrasena != contrasena_correcta:
        contrasena = input("Ingrese la contraseña: ")
    print("Contraseña correcta. Acceso permitido.")

solicitar_contrasena()