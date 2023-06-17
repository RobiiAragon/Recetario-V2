import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
from openpyxl.drawing.image import Image


def obtener_fecha_actual():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def crear_carpeta_con_fecha_actual():
    fecha_actual = obtener_fecha_actual()
    carpeta = os.path.join(os.getcwd(), "Recetarios", fecha_actual)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta


def hacer_preguntas():
    nombre = nombre_entry.get()
    if not nombre:
        nombre = " "  # Espacio en blanco
    edad = edad_entry.get()
    if not edad:
        edad = " "  # Espacio en blanco
    temp = temp_entry.get()
    if not temp:
        temp = " "  # Espacio en blanco
    ta = ta_entry.get()
    if not ta:
        ta = " "  # Espacio en blanco
    peso = peso_entry.get()
    if not peso:
        peso = " "  # Espacio en blanco
    fc = fc_entry.get()
    if not fc:
        fc = " "  # Espacio en blanco
    talla = talla_entry.get()
    if not talla:
        talla = " "  # Espacio en blanco
    fr = fr_entry.get()
    if not fr:
        fr = " "  # Espacio en blanco
    circun_abdom = circun_abdom_entry.get()
    if not circun_abdom:
        circun_abdom = " "  # Espacio en blanco
    id = id_entry.get()
    if not id:
        id = " "  # Espacio en blanco
    alergias = alergias_entry.get()
    if not alergias:
        alergias = " "  # Espacio en blanco
    tratamiento = tratamiento_entry.get()
    if not tratamiento:
        tratamiento = " "  # Espacio en blanco
    indicaciones_generales = indicaciones_generales_entry.get()
    if not indicaciones_generales:
        indicaciones_generales = " "  # Espacio en blanco
    proxima_cita = proxima_cita_entry.get()
    if not proxima_cita:
        proxima_cita = " "  # Espacio en blanco
    return nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita


def llenar_datos_en_plantilla(nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita):
    plantilla = openpyxl.load_workbook("receta.xlsx")
    hoja = plantilla.active

    hoja["J4"] = nombre
    hoja["J36"] = nombre
    hoja["H5"] = edad
    hoja["H37"] = edad
    # Fecha y hora automática en columna D4
    hoja["BB4"] = obtener_fecha_actual()
    # Fecha y hora automática en columna D34
    hoja["BB36"] = obtener_fecha_actual()
    hoja["R5"] = temp
    hoja["R37"] = temp
    hoja["H6"] = ta
    hoja["H38"] = ta
    hoja["R6"] = peso
    hoja["R38"] = peso
    hoja["H7"] = fc
    hoja["H39"] = fc
    hoja["R7"] = talla
    hoja["R39"] = talla
    hoja["H8"] = fr
    hoja["H40"] = fr
    hoja["L10"] = circun_abdom
    hoja["L42"] = circun_abdom
    hoja["H11"] = id
    hoja["H43"] = id
    hoja["I13"] = alergias
    hoja["I45"] = alergias
    hoja["AC6"] = tratamiento
    hoja["AC38"] = tratamiento
    hoja["O16"] = indicaciones_generales
    hoja["O48"] = indicaciones_generales
    hoja["AF22"] = proxima_cita
    hoja["AF54"] = proxima_cita

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


def generar_reporte():
    carpeta = crear_carpeta_con_fecha_actual()
    nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita = hacer_preguntas()
    plantilla = llenar_datos_en_plantilla(nombre, edad, temp, ta, peso, fc, talla, fr,
                                          circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita)
    ruta_receta_modificada = guardar_plantilla_modificada(
        plantilla, carpeta, nombre)
    imprimir_mensaje_exito(carpeta)


window = tk.Tk()
window.title("Generador de nota de evolucion")
window.geometry("350x100")
window.iconbitmap('ico.ico')

generar_button = tk.Button(
    window, text="Generar Reporte", command=generar_reporte)
mensaje_label = tk.Label(window, wraplength=350)

generar_button.pack()
mensaje_label.pack()

window.mainloop()
