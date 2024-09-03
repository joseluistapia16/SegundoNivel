class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"

def inicio():
    personas = [
        Persona("Ana", 25),
        Persona("Luis", 30),
        Persona("Juan", 20),
        Persona("Ana", 20)
    ]

    # Usando sorted() con una clave de ordenación múltiple
    personas_ordenadas = sorted(personas, key=lambda p: (p.nombre,p.edad))

    # Imprimir personas ordenadas
    for persona in personas_ordenadas:
        print(persona.nombre,persona.edad)



def inputInt(cadena):
    num = -1
    while num < 0:
        try:
            num = int(input(cadena))
        except:
            num = -1
            print("Valor invalido.")
    return num
def inputFloat(cadena):
    num = -1
    while num < 0:
        try:
            num = float(input(cadena))
        except:
            num = -1
            print("Valor invalido.")
    return num
def nota(cadena):
    valor = -1
    while valor < 0 or valor > 10:
        valor = inputFloat(cadena)
    return valor
def ejercicio1():
    c = 0
    ac = 0
    general = 0
    while True:
        notas = []
        ac = 0
        print("Estudiante #{}".format(c+1))
        nombre = input("Ingrese su nombre: ")
        materia = input("Ingrese su materia: ")
        for i in range(3):
            valor = nota("Ingrese su nota " + str(i + 1) + ": ")
            notas.append(valor)
            ac = ac + notas[i]
        ac = ac / 3
        print("El promedio es: {}".format(round(ac, 2)))
        general = general + ac
        c = c +1
        op = input("Desea agregar otro estdiante [S/N]: ")
        if op == "N" or op == "n":
            break
    general = (general/c)
    print("El promedio general es: {}".format(general))





#ejercicio1()
#inicio()
class MyClass:
    def __init__(self, value):
        self.value = value
    def prueba(self):
        return self.value/3

obj = MyClass(6)
print(obj.prueba())

