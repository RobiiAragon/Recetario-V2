import subprocess
import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
import os

# Crear la carpeta "ARCHIVO" si no existe
if not os.path.exists("ARCHIVO"):
    os.makedirs("ARCHIVO")

# Modes: system (default), light, dark
ctk.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("blue")


def iniciar_sesion():
    # Función para verificar las credenciales del usuario
    def verificar_credenciales():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()

        # Establecer conexión con la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="AME"
        )
        cursor = connection.cursor()

        # Ejecutar consulta para verificar las credenciales
        query = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
        values = (usuario, contraseña)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Inicio de sesión exitoso",
                                "¡Bienvenido, {}!".format(usuario))
            root.destroy()  # Cerrar la ventana de inicio de sesión
            aplicacion_final()
        else:
            messagebox.showerror("Error de inicio de sesión",
                                 "Credenciales incorrectas. Por favor, intente nuevamente.")

        # Cerrar la conexión con la base de datos
        cursor.close()
        connection.close()

    # Crear la ventana de inicio de sesión
    root = ctk.CTk()
    root.title("AME - Inicio de Sesión")
    root.geometry("300x200")  # Cambia las dimensiones según tus necesidades
    root.iconbitmap('ico.ico')

    label_usuario = ctk.CTkLabel(root, text="Nombre de usuario:")
    label_usuario.grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = ctk.CTkEntry(root)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    label_contraseña = ctk.CTkLabel(root, text="Contraseña:")
    label_contraseña.grid(row=1, column=0, padx=10, pady=10)
    entry_contraseña = ctk.CTkEntry(root, show="*")
    entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

    # Utilizar CTkButton en lugar de Button
    button_iniciar_sesion = ctk.CTkButton(
        root, text="Iniciar Sesión", command=verificar_credenciales)
    button_iniciar_sesion.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


def aplicacion_final():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/seleccionar modo.py"])


# Llamada a la función de inicio de sesión
iniciar_sesion()
