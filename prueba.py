import tkinter as tk
from tkinter import PhotoImage
ruta ="C:/Users/user/Pictures/ico.png"
# Crear la ventana principal
root = tk.Tk()
root.title("Formulario con Iconos en Botones")

# Cargar las imágenes
imagen1 = PhotoImage(file=ruta)  # Asegúrate de tener esta imagen en tu directorio
imagen2 = PhotoImage(file=ruta)  # Asegúrate de tener esta imagen en tu directorio
imagen3 = PhotoImage(file=ruta)  # Asegúrate de tener esta imagen en tu directorio

# Crear los botones con imágenes como iconos
boton1 = tk.Button(root, image=imagen1, text="Botón 1", compound="left")
boton1.pack(pady=10)

boton2 = tk.Button(root, image=imagen2, text="Botón 2", compound="left")
boton2.pack(pady=10)

boton3 = tk.Button(root, image=imagen3, text="Botón 3", compound="left")
boton3.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
