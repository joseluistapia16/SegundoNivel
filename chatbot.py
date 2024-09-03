def finalizar(mensaje):
    palabras_fin = ["Fin", "FIN", "Chaou", "CHAOU", "BYE", "bye"]
    return mensaje in palabras_fin

def chatbot():
    while True:
        usuario = input("Yo: ")
        if finalizar(usuario):
            print("Chat Bot: ¡Adiós! Que tengas un buen día.")
            break

        print("Chat Bot: Hola, ¿cómo estás?")
        print("Chat Bot: ¿Cuál es tu nombre?")

        usuario = input("Yo: ")
        if finalizar(usuario):
            print("Chat Bot: ¡Adiós! Que tengas un buen día.")
            break

        print(f"Bienvenido {usuario} a nuestra charla virtual")
        print("Chat Bot: ¿Deseas charlar de Fútbol o Programación?")

        usuario = input("Yo: ")
        if finalizar(usuario):
            print("Chat Bot: ¡Adiós! Que tengas un buen día.")
            break

        if usuario.lower() in ["programación", "programacion"]:
            print("Chat Bot: ¿Programas en Python?")
            usuario = input("Yo: ")
            if finalizar(usuario):
                print("Chat Bot: ¡Adiós! Que tengas un buen día.")
                break
        elif usuario.lower() == "futbol":
            print("Chat Bot: ¿De qué equipo eres hincha?")
            usuario = input("Yo:")


if __name__ == '__main__':
    c
