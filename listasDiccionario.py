def ejercicio1():
    lista = []
    res = True
    while res == True:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        direccion = input("Ingrese la direccion: ")
        personas = {
            "nombre": nombre,
            "edad" : edad,
            "direccion": direccion
        }
        lista.append(personas)
        op = input("Desea ingresar otra persona? [S/N]: ")
        if op == "n" or op == "N":
            res = False
    print("Listas de personas")
    for personas in lista:
        print(personas['nombre'],personas['edad'],personas['direccion'])

if __name__ == '__main__':
    ejercicio1()