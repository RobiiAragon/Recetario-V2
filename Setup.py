import tkinter as tk
from tkinter import messagebox
import subprocess
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")


def iniciar_sesion():
    # Agrega aquí los usuarios y contraseñas permitidos
    usuarios_registrados = {"Aragon": "jala1975", "Invitado": "invitadoamespa"}

    def verificar_credenciales():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()

        if usuario in usuarios_registrados and contraseña == usuarios_registrados[usuario]:
            messagebox.showinfo("Inicio de sesión exitoso",
                                "¡Bienvenido, {}!".format(usuario))
            root.destroy()  # Cerrar la ventana de inicio de sesión
            aplicacion_final()
        else:
            messagebox.showerror("Error de inicio de sesión",
                                 "Credenciales incorrectas. Por favor, intente nuevamente.")

    # Crear la ventana de inicio de sesión
    root = tk.Tk()
    root.title("AME - Inicio de Sesión")
    root.geometry("300x200")  # Cambia las dimensiones según tus necesidades

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
