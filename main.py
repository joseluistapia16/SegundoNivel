def getEdad(edad):
    if edad>=0 and edad<11:
        return "Infante"
    if edad>10 and edad<18:
        return "Adolescente"
    if edad>17 and edad<26:
        return "Joven"
    if edad>25 and edad<65:
        return "Adulto"
    if edad>64:
        return "Adulto mayor"
    if edad<0:
        return "Edad invalida!"

def getAverange(n1,n2,n3):
    return (n1+n2+n3)/3

def ejercicio1():
    print("Establecer edad.")
    edad = int(input("Edad:"))
    msg = getEdad(edad)
    print(msg)

def ejercicio2():
    print("    Promedio de 3 notas")
    nombre = input("Nombre:")
    asignatura = input("Asignatura:")
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))
    promedio = getAverange(nota1,nota2,nota3)
    msg = "El promedio es:{}".format(round(promedio,2))
    print(msg)
def menu():
    print("   Menu de opciones")
    print("1.- Establecer edad")
    print("2.- Promedio")
    print("3.- Salir")
    op = int(input("Ingrese una opcion[1..3]:"))
    if op == 1:
        ejercicio1()
        menu()
    if op == 2:
        ejercicio2()
        menu()
    if op == 3:
        print("Gracias por su visita...")



menu()