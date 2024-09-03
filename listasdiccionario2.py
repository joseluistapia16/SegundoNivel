def ejercicio1():
    res=True
    lista=[]
    while res==True:
        nombre=input("Nombre: ")
        apellido=input("Apellido: ")
        edad=int(input("Edad: "))
        personas={
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad
        }
        lista.append(personas)
        op=input("Desea ingresar otra persona? [S/N]: ")
        if op=="n" or op=="N":
            res=False
    for personas in lista:
        print(personas["nombre"],personas["apellido"],personas["edad"]) #para que salga limpio usamos el nombre de la

if __name__ == '__main__':
    ejercicio1()
