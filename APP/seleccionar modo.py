import tkinter as tk
from tkinter import ttk
import subprocess
import os


def cerrar_sesion():
    # Agrega aquí las acciones que deseas realizar al cerrar sesión
    # Por ejemplo, guardar datos, limpiar variables, etc.
    root.destroy()


def Crear_receta():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "recetario.py"])


def certificado_medico():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "certificado medico.py"])


def notadeevolucion():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "nota de evolucion.py"])


def Crear_Historial():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "historia clinica.py"])


def hoja_referencia():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "hoja de referencia.py"])


# Crear la ventana principal
root = tk.Tk()

# Configurar el tamaño de la ventana
root.geometry("300x250")

# Botón para cerrar sesión
btn_cerrar_sesion = tk.Button(
    root, text="Cerrar sesión", command=cerrar_sesion)
btn_cerrar_sesion.pack(pady=10)

# Botón para redirigir a recetario.py
btn_redirigir = tk.Button(root, text="Crear receta", command=Crear_receta)
btn_redirigir.pack(pady=5)

# Botón para redirigir a certificado_medico
btn_redirigir = tk.Button(
    root, text="Certificado Médico", command=certificado_medico)
btn_redirigir.pack(pady=5)

# Botón para redirigir a Crear_Historial
btn_redirigir = tk.Button(
    root, text="Crear Historial", command=Crear_Historial)
btn_redirigir.pack(pady=5)

# Botón para redirigir a notadeevolucion
btn_redirigir = tk.Button(
    root, text="Nota de Evolución", command=notadeevolucion)
btn_redirigir.pack(pady=5)

# Botón para redirigir a hoja_referencia
btn_redirigir = tk.Button(
    root, text="Hoja de Referencia", command=hoja_referencia)
btn_redirigir.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
