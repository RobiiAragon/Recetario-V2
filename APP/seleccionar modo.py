import subprocess
import webbrowser
import customtkinter as ctk
import os
import shutil
import datetime


def cerrar_sesion():
    # Agrega aquí las acciones que deseas realizar al cerrar sesión
    # Por ejemplo, guardar datos, limpiar variables, etc.
    root.destroy()

def abrir_ruta_receta():
    ruta = r"C:\Resetario AME\ARCHIVO\RECETAS"
    subprocess.run(["explorer", ruta])

def abrir_ruta_certificado_medico():
    ruta = r"C:\Resetario AME\ARCHIVO\CERTIFICADOS MEDICOS"
    subprocess.run(["explorer", ruta])

def abrir_ruta_Historial():
    ruta = r"C:\Resetario AME\ARCHIVO\HISTORIALES MEDICOS"
    subprocess.run(["explorer", ruta])

def abrir_ruta_notadeevolucion():
    ruta = r"C:\Resetario AME\ARCHIVO\NOTAS DE EVOLUCION"
    subprocess.run(["explorer", ruta])

def abrir_ruta_hoja_referencia():
    ruta = r"C:\Resetario AME\ARCHIVO\HOJAS DE REFERENCIA"
    subprocess.run(["explorer", ruta])

def Crear_receta():
    # Llamada al script recetario.py usando subprocess
    subprocess.call(["python", "APP/Resetario/Recetario.py"])


def certificado_medico():
    # Verificar si la carpeta "ARCHIVO" existe
    if os.path.exists("ARCHIVO"):
        # Crear la carpeta "certificados medicos" dentro de "ARCHIVO" si no existe
        carpeta_certificados = os.path.join("ARCHIVO", "CERTIFICADOS MEDICOS")
        if not os.path.exists(carpeta_certificados):
            os.makedirs(carpeta_certificados)
    else:
        print("La carpeta 'ARCHIVO' no existe.")

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Crear la carpeta con la fecha actual si no existe
    carpeta_fecha_actual = os.path.join(carpeta_certificados, fecha_actual)
    if not os.path.exists(carpeta_fecha_actual):
        os.makedirs(carpeta_fecha_actual)

    # Obtener la hora y el minuto actual
    hora_actual = datetime.datetime.now().strftime("%H-%M")

    # Nombre del archivo PDF a pegar
    nombre_archivo = f"{hora_actual}.pdf"

    # Ruta completa de la plantilla PDF y del archivo a pegar
    ruta_plantilla = "PLANTILLAS/PDF/CertificadoMedico.pdf"
    ruta_destino = os.path.join(carpeta_fecha_actual, nombre_archivo)

    # Copiar y pegar el archivo PDF en la carpeta correspondiente
    shutil.copyfile(ruta_plantilla, ruta_destino)

    # Ejecutar el archivo PDF con Adobe Acrobat Reader en Windows
    subprocess.run(["start", "C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe", ruta_destino], shell=True)



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
root.iconbitmap('APP/ico.ico')
root.title("AME - Selecciona modo")
root.geometry("300x250")

# Configurar el gestor de geometría para que se ajuste al centro de la ventana
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Botón para cerrar sesión
btn_cerrar_sesion = ctk.CTkButton(
    root, text="Cerrar sesión 🔒", command=cerrar_sesion)
btn_cerrar_sesion.grid(row=0, column=0, pady=10, padx=5, sticky="nsew")

# Botón para redirigir a recetario.py
btn_redirigir = ctk.CTkButton(
    root, text="Crear receta 📝", command=Crear_receta)
btn_redirigir.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")
btn_abrir_ruta = ctk.CTkButton(
    root, text="📂", command=abrir_ruta_receta, width=2)
btn_abrir_ruta.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")  # Añadir padx con 5 píxeles de margen a la derecha

# Botón para redirigir a certificado_medico
btn_redirigir = ctk.CTkButton(
    root, text="Certificado Médico 📑", command=certificado_medico)
btn_redirigir.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")
btn_abrir_ruta = ctk.CTkButton(
    root, text="📂", command=abrir_ruta_certificado_medico, width=2)
btn_abrir_ruta.grid(row=2, column=1, pady=5, padx=5, sticky="nsew")  # Añadir padx con 5 píxeles de margen a la derecha

# Botón para redirigir a Crear_Historial
btn_redirigir = ctk.CTkButton(
    root, text="Crear Historial 🗂️", command=Crear_Historial)
btn_redirigir.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
btn_abrir_ruta = ctk.CTkButton(
    root, text="📂", command=abrir_ruta_Historial, width=2)
btn_abrir_ruta.grid(row=3, column=1, pady=5, padx=5, sticky="nsew")  # Añadir padx con 5 píxeles de margen a la derecha

# Botón para redirigir a notadeevolucion
btn_redirigir = ctk.CTkButton(
    root, text="Nota de Evolución 📊", command=notadeevolucion)
btn_redirigir.grid(row=4, column=0, pady=5, padx=5, sticky="nsew")
btn_abrir_ruta = ctk.CTkButton(
    root, text="📂", command=abrir_ruta_notadeevolucion, width=2)
btn_abrir_ruta.grid(row=4, column=1, pady=5, padx=5, sticky="nsew")  # Añadir padx con 5 píxeles de margen a la derecha

# Botón para redirigir a hoja_referencia
btn_redirigir = ctk.CTkButton(
    root, text="Hoja de Referencia 🗒️", command=hoja_referencia)
btn_redirigir.grid(row=5, column=0, pady=5, padx=5, sticky="nsew")
btn_abrir_ruta = ctk.CTkButton(
    root, text="📂", command=abrir_ruta_hoja_referencia, width=2)
btn_abrir_ruta.grid(row=5, column=1, pady=5, padx=5, sticky="nsew")  # Añadir padx con 5 píxeles de margen a la derecha

# Iniciar el bucle principal de la ventana
root.mainloop()
