import tkinter as tk
from tkinter import filedialog, messagebox
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from datetime import datetime
import os


def hacer_preguntas():
    # Obtener los valores de los campos
    neopla = neopla_entry.get()
    sida = sida_entry.get()
    alimentacion = alimentacion_entry.get()
    higiene_b = higiene_b_var.get()
    higiene_r = higiene_r_var.get()
    higiene_m = higiene_m_var.get()
    inmunizaciones = inmunizaciones_entry.get()
    tabaquismo_menos = tabaquismo_menos_var.get()
    tabaquismo_mas = tabaquismo_mas_var.get()
    alcoholismo_menos = alcoholismo_menos_var.get()
    alcoholismo_mas = alcoholismo_mas_var.get()
    tiempo_evolucion = tiempo_evolucion_entry.get()
    quirurgicos = quirurgicos_entry.get()
    medicamentos = medicamentos_entry.get()

    # Guardar los valores en una plantilla modificada
    guardar_plantilla_modificada(ruta_archivo, neopla, sida, alimentacion, higiene_b, higiene_r, higiene_m,
                                 inmunizaciones, tabaquismo_menos, tabaquismo_mas, alcoholismo_menos,
                                 alcoholismo_mas, tiempo_evolucion, quirurgicos, medicamentos)


def guardar_plantilla_modificada(ruta_archivo, neopla, sida, alimentacion, higiene_b, higiene_r, higiene_m,
                                 inmunizaciones, tabaquismo_menos, tabaquismo_mas, alcoholismo_menos,
                                 alcoholismo_mas, tiempo_evolucion, quirurgicos, medicamentos):
    # Cargar la plantilla
    workbook = Workbook()
    sheet = workbook.active

    # Rellenar la plantilla con los valores
    sheet['B3'] = neopla
    sheet['B4'] = sida
    sheet['B5'] = alimentacion
    sheet['B7'] = higiene_b
    sheet['B8'] = higiene_r
    sheet['B9'] = higiene_m
    sheet['B11'] = inmunizaciones
    sheet['B13'] = tabaquismo_menos
    sheet['B14'] = tabaquismo_mas
    sheet['B16'] = alcoholismo_menos
    sheet['B17'] = alcoholismo_mas
    sheet['B19'] = tiempo_evolucion
    sheet['B21'] = quirurgicos
    sheet['B23'] = medicamentos

    # Guardar la plantilla modificada
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"Historia Clínica {fecha_actual}.xlsx"
    directorio = f"./{fecha_actual}"
    os.makedirs(directorio, exist_ok=True)
    ruta_guardado = os.path.join(directorio, nombre_archivo)
    workbook.save(ruta_guardado)
    messagebox.showinfo("Éxito", "La plantilla se ha guardado correctamente.")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Historia Clínica")
ventana.geometry("800x600")  # Cambiar el tamaño de la ventana según tus necesidades

# Etiquetas y campos de entrada
neopla_label = tk.Label(ventana, text="Neoplasias:")
neopla_label.grid(row=0, column=0, sticky="w")
neopla_entry = tk.Entry(ventana)
neopla_entry.grid(row=0, column=1)

sida_label = tk.Label(ventana, text="SIDA:")
sida_label.grid(row=1, column=0, sticky="w")
sida_entry = tk.Entry(ventana)
sida_entry.grid(row=1, column=1)

alimentacion_label = tk.Label(ventana, text="Alimentación:")
alimentacion_label.grid(row=2, column=0, sticky="w")
alimentacion_entry = tk.Entry(ventana)
alimentacion_entry.grid(row=2, column=1)

higiene_b_label = tk.Label(ventana, text="Higiene Bucal:")
higiene_b_label.grid(row=3, column=0, sticky="w")
higiene_b_var = tk.BooleanVar()
higiene_b_check = tk.Checkbutton(ventana, variable=higiene_b_var)
higiene_b_check.grid(row=3, column=1, sticky="w")

higiene_r_label = tk.Label(ventana, text="Higiene Corporal:")
higiene_r_label.grid(row=4, column=0, sticky="w")
higiene_r_var = tk.BooleanVar()
higiene_r_check = tk.Checkbutton(ventana, variable=higiene_r_var)
higiene_r_check.grid(row=4, column=1, sticky="w")

higiene_m_label = tk.Label(ventana, text="Higiene Mental:")
higiene_m_label.grid(row=5, column=0, sticky="w")
higiene_m_var = tk.BooleanVar()
higiene_m_check = tk.Checkbutton(ventana, variable=higiene_m_var)
higiene_m_check.grid(row=5, column=1, sticky="w")

inmunizaciones_label = tk.Label(ventana, text="Inmunizaciones:")
inmunizaciones_label.grid(row=6, column=0, sticky="w")
inmunizaciones_entry = tk.Entry(ventana)
inmunizaciones_entry.grid(row=6, column=1)

tabaquismo_menos_label = tk.Label(ventana, text="Tabaquismo (-):")
tabaquismo_menos_label.grid(row=7, column=0, sticky="w")
tabaquismo_menos_var = tk.BooleanVar()
tabaquismo_menos_check = tk.Checkbutton(ventana, variable=tabaquismo_menos_var)
tabaquismo_menos_check.grid(row=7, column=1, sticky="w")

tabaquismo_mas_label = tk.Label(ventana, text="Tabaquismo (+):")
tabaquismo_mas_label.grid(row=8, column=0, sticky="w")
tabaquismo_mas_var = tk.BooleanVar()
tabaquismo_mas_check = tk.Checkbutton(ventana, variable=tabaquismo_mas_var)
tabaquismo_mas_check.grid(row=8, column=1, sticky="w")

alcoholismo_menos_label = tk.Label(ventana, text="Alcoholismo (-):")
alcoholismo_menos_label.grid(row=9, column=0, sticky="w")
alcoholismo_menos_var = tk.BooleanVar()
alcoholismo_menos_check = tk.Checkbutton(ventana, variable=alcoholismo_menos_var)
alcoholismo_menos_check.grid(row=9, column=1, sticky="w")

alcoholismo_mas_label = tk.Label(ventana, text="Alcoholismo (+):")
alcoholismo_mas_label.grid(row=10, column=0, sticky="w")
alcoholismo_mas_var = tk.BooleanVar()
alcoholismo_mas_check = tk.Checkbutton(ventana, variable=alcoholismo_mas_var)
alcoholismo_mas_check.grid(row=10, column=1, sticky="w")

tiempo_evolucion_label = tk.Label(ventana, text="Tiempo de Evolución:")
tiempo_evolucion_label.grid(row=11, column=0, sticky="w")
tiempo_evolucion_entry = tk.Entry(ventana)
tiempo_evolucion_entry.grid(row=11, column=1)

quirurgicos_label = tk.Label(ventana, text="Antecedentes Quirúrgicos:")
quirurgicos_label.grid(row=12, column=0, sticky="w")
quirurgicos_entry = tk.Entry(ventana)
quirurgicos_entry.grid(row=12, column=1)

medicamentos_label = tk.Label(ventana, text="Medicamentos:")
medicamentos_label.grid(row=13, column=0, sticky="w")
medicamentos_entry = tk.Entry(ventana)
medicamentos_entry.grid(row=13, column=1)

# Botón de guardar
guardar_button = tk.Button(ventana, text="Guardar", command=hacer_preguntas)
guardar_button.grid(row=14, column=0, columnspan=2)

# Ejecutar la ventana
ventana.mainloop()
