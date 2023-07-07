import subprocess
import customtkinter as ctk


def cerrar_sesion():
    # Agrega aquí las acciones que deseas realizar al cerrar sesión
    # Por ejemplo, guardar datos, limpiar variables, etc.
    root.destroy()


def Crear_receta():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Resetario/Recetario.py"])


def certificado_medico():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Certificado Medico/certificado medico.py"])


def notadeevolucion():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Nota de evolucion/nota de evolucion.py"])


def Crear_Historial():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Historial clinico/historia clinica.py"])


def hoja_referencia():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Hoja Referencia/hoja de referencia.py"])


# Crear la ventana principal
root = ctk.CTk()
root.iconbitmap('ico.ico')
root.title("AME - Selecciona modo")
# Configurar el tamaño de la ventana
root.geometry("300x250")

# Botón para cerrar sesión
btn_cerrar_sesion = ctk.CTkButton(
    root, text="Cerrar sesión 🔒", command=cerrar_sesion)
btn_cerrar_sesion.pack(pady=10)

# Botón para redirigir a recetario.py
btn_redirigir = ctk.CTkButton(
    root, text="Crear receta 📝", command=Crear_receta)
btn_redirigir.pack(pady=5)

# Botón para redirigir a certificado_medico
btn_redirigir = ctk.CTkButton(
    root, text="Certificado Médico 📑", command=certificado_medico)
btn_redirigir.pack(pady=5)

# Botón para redirigir a Crear_Historial
btn_redirigir = ctk.CTkButton(
    root, text="Crear Historial 🗂️", command=Crear_Historial)
btn_redirigir.pack(pady=5)

# Botón para redirigir a notadeevolucion
btn_redirigir = ctk.CTkButton(
    root, text="Nota de Evolución 📊", command=notadeevolucion)
btn_redirigir.pack(pady=5)

# Botón para redirigir a hoja_referencia
btn_redirigir = ctk.CTkButton(
    root, text="Hoja de Referencia 🗒️", command=hoja_referencia)
btn_redirigir.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
