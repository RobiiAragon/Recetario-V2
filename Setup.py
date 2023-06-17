import tkinter as tk
from tkinter import messagebox
import subprocess
import customtkinter
import mysql.connector

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")


def iniciar_sesion():
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
    root = tk.Tk()
    root.title("AME - Inicio de Sesión")
    root.geometry("300x200")  # Cambia las dimensiones según tus necesidades
    root.iconbitmap('ico.ico')

    label_usuario = tk.Label(root, text="Nombre de usuario:")
    label_usuario.pack()
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.pack()
    entry_contraseña = tk.Entry(root, show="*")
    entry_contraseña.pack()

    # Utilizar CTkButton en lugar de Button
    button_iniciar_sesion = customtkinter.CTkButton(
        root, text="Iniciar Sesión", command=verificar_credenciales)
    button_iniciar_sesion.pack()

    root.mainloop()


def aplicacion_final():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/seleccionar modo.py"])


# Llamada a la función de inicio de sesión
iniciar_sesion()
