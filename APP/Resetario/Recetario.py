import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
from openpyxl.drawing.image import Image
import mysql.connector
from tkcalendar import DateEntry

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="AME"
)
cursor = conexion.cursor()


def obtener_fecha_actual():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def crear_carpeta_con_fecha_actual():
    fecha_actual = obtener_fecha_actual()
    carpeta = os.path.join(os.getcwd(), "Recetarios", fecha_actual)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta


def hacer_preguntas(entries):
    respuestas = []
    for entry in entries:
        respuesta = entry.get()
        if not respuesta:
            respuesta = " "  # Espacio en blanco
        respuestas.append(respuesta)
    return tuple(respuestas)


def guardar_en_base_de_datos(datos):
    # Insertar los datos en la base de datos
    query = "INSERT INTO recetas (nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, datos)
    cursor.execute("ALTER TABLE recetas AUTO_INCREMENT = 1")

    conexion.commit()


def llenar_datos_en_plantilla(plantilla, datos):
    hoja = plantilla.active

    hoja["J4"] = datos[0]
    hoja["J32"] = datos[0]
    hoja["H6"] = datos[1]
    hoja["H34"] = datos[1]
    # Fecha y hora automática en columna D4
    hoja["BB4"] = obtener_fecha_actual()
    # Fecha y hora automática en columna D34
    hoja["BB32"] = obtener_fecha_actual()
    hoja["Q6"] = datos[2]
    hoja["Q34"] = datos[2]
    hoja["G8"] = datos[3]
    hoja["G36"] = datos[3]
    hoja["Q8"] = datos[4]
    hoja["Q36"] = datos[4]
    hoja["G10"] = datos[5]
    hoja["G38"] = datos[5]
    hoja["Q10"] = datos[6]
    hoja["Q38"] = datos[6]
    hoja["G12"] = datos[7]
    hoja["G40"] = datos[7]
    hoja["L14"] = datos[8]
    hoja["K42"] = datos[8]
    hoja["G16"] = datos[9]
    hoja["G44"] = datos[9]
    hoja["H18"] = datos[10]
    hoja["H46"] = datos[10]
    hoja["X8"] = datos[11]
    hoja["X36"] = datos[11]
    hoja["O21"] = datos[12]
    hoja["O48"] = datos[12]
    hoja["AF27"] = datos[13]
    hoja["AF55"] = datos[13]

    # Cargar la imagen
    imagen = Image("receta.png")

    # Ajustar la imagen al tamaño de la celda deseada
    imagen.width = 750
    imagen.height = 990

    # Insertar la imagen en la celda deseada
    hoja.add_image(imagen, "A1")

    return plantilla


def guardar_plantilla_modificada(plantilla, carpeta, nombre_pdf):
    ruta_receta_modificada = os.path.join(carpeta, f"{nombre_pdf}.xlsx")
    plantilla.save(ruta_receta_modificada)
    return ruta_receta_modificada


def imprimir_mensaje_exito(carpeta):
    print("La receta modificada se ha guardado en la carpeta", carpeta)
    os.startfile(carpeta)


def generar_reporte(entries):
    carpeta = crear_carpeta_con_fecha_actual()
    datos = hacer_preguntas(entries)
    guardar_en_base_de_datos(datos)
    plantilla = openpyxl.load_workbook("PLANTILLAS XLSX/receta.xlsx")
    plantilla_modificada = llenar_datos_en_plantilla(plantilla, datos)
    ruta_receta_modificada = guardar_plantilla_modificada(
        plantilla_modificada, carpeta, datos[0])
    imprimir_mensaje_exito(carpeta)


window = Tk()
window.title("Generador de Resetas medicas")
window.geometry("350x650")
window.iconbitmap('ico.ico')

labels = [
    "Nombre:", "Edad:", "Temp:", "T.A.:", "Peso:", "F.C.:", "Talla:", "F.R.:",
    "Circun. Abdom.:", "I.D.:", "Alergias:", "Tratamiento:", "Indicaciones Generales:",
    "Próxima Cita:"
]

entries = []

for label_text in labels:
    label = tk.Label(window, text=label_text)
    label.pack()
    if label_text == "Próxima Cita:":
        entry = DateEntry(window, date_pattern='dd-mm-yyyy')
    else:
        entry = tk.Entry(window)
    entry.pack()
    entries.append(entry)

generar_button = tk.Button(
    window, text="Generar Reporte", command=lambda: generar_reporte(entries)
)
generar_button.pack()

mensaje_label = tk.Label(window, wraplength=350)
mensaje_label.pack()

window.mainloop()
