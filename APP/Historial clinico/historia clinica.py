import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import ttk, Text
from tkinter import filedialog
from openpyxl.drawing.image import Image
import customtkinter as ctk

def obtener_fecha_actual():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def crear_carpeta_con_fecha_actual():
    fecha_actual = obtener_fecha_actual()
    carpeta = os.path.join(os.getcwd(), "Historia Clinica", fecha_actual)
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
    sexo = sexo_entry.get()
    if not sexo:
        sexo = " "  # Espacio en blanco
    l_origen = l_origen_entry.get()
    if not l_origen:
        l_origen = " "  # Espacio en blanco
    l_residencia = l_residencia_entry.get()
    if not l_residencia:
        l_residencia = " "  # Espacio en blanco
    edo_civil = edo_civil_entry.get()
    if not edo_civil:
        edo_civil = " "  # Espacio en blanco
    ant_hf = ant_hf_entry.get()
    if not ant_hf:
        ant_hf = " "  # Espacio en blanco
    diab = diab_entry.get()
    if not diab:
        diab = " "  # Espacio en blanco
    epilep = epilep_entry.get()
    if not epilep:
        epilep = " "  # Espacio en blanco
    hipertension = hipertension_entry.get()
    if not hipertension:
        hipertension = " "  # Espacio en blanco
    cardiovasc = cardiovasc_entry.get()
    if not cardiovasc:
        cardiovasc = " "  # Espacio en blanco
    lueticos = lueticos_entry.get()
    if not lueticos:
        lueticos = " "  # Espacio en blanco
    fimicos = fimicos_entry.get()
    if not fimicos:
        fimicos = " "  # Espacio en blanco
    neopla = neopla_entry.get()
    if not neopla:
        neopla = " "  # Espacio en blanco
    sida = sida_entry.get()
    if not sida:
        sida = " "  # Espacio en blanco
    aliment = aliment_entry.get()
    if not aliment:
        aliment = " "  # Espacio en blanco
    higiene_b = higiene_b_var.get()
    higiene_r = higiene_r_var.get()
    higiene_m = higiene_m_var.get()
    inmunizaciones = inmunizaciones_entry.get()
    if not inmunizaciones:
        inmunizaciones = " "  # Espacio en blanco
    taxicomania_menos = taxicomania_menos_var.get()
    taxicomania_mas = taxicomania_mas_var.get()
    tabaquismo_menos = tabaquismo_menos_var.get()
    tabaquismo_mas = tabaquismo_mas_var.get()
    alcoholismo_menos = alcoholismo_menos_var.get()
    alcoholismo_mas = alcoholismo_mas_var.get()
    tiempo_evolucion = tiempo_evolucion_entry.get()
    if not tiempo_evolucion:
        tiempo_evolucion = " "  # Espacio en blanco
    quirurgicos = quirurgicos_entry.get()
    if not quirurgicos:
        quirurgicos = " "  # Espacio en blanco
    transfuciones = transfuciones_entry.get()
    if not transfuciones:
        transfuciones = " "  # Espacio en blanco
    traumaticos = traumaticos_entry.get()
    if not traumaticos:
        traumaticos = " "  # Espacio en blanco
    alergicos = alergicos_entry.get()
    if not alergicos:
        alergicos = " "  # Espacio en blanco
    otros = otros_entry.get()
    if not otros:
        otros = " "  # Espacio en blanco
    menarca = menarca_entry.get()
    if not menarca:
        menarca = " "  # Espacio en blanco
    ritmo = ritmo_entry.get()
    if not ritmo:
        ritmo = " "  # Espacio en blanco
    ivsa = ivsa_entry.get()
    if not ivsa:
        ivsa = " "  # Espacio en blanco
    no_parejas = no_parejas_entry.get()
    if not no_parejas:
        no_parejas = " "  # Espacio en blanco
    g = g_entry.get()
    if not g:
        g = " "  # Espacio en blanco
    p = p_entry.get()
    if not p:
        p = " "  # Espacio en blanco
    ab = ab_entry.get()
    if not ab:
        ab = " "  # Espacio en blanco
    c = c_entry.get()
    if not c:
        c = " "  # Espacio en blanco
    fur = fur_entry.get()
    if not fur:
        fur = " "  # Espacio en blanco
    leucorrea_menos = leucorrea_menos_var.get()
    leucorrea_mas = leucorrea_mas_var.get()
    caracteristicas = caracteristicas_entry.get()
    if not caracteristicas:
        caracteristicas = " "  # Espacio en blanco
    padecimiento_actual = padecimiento_actual_entry.get()
    if not padecimiento_actual:
        padecimiento_actual = " "  # Espacio en blanco
    peso = peso_entry.get()
    if not peso:
        peso = " "  # Espacio en blanco
    talla = talla_entry.get()
    if not talla:
        talla = " "  # Espacio en blanco
    ta = ta_entry.get()
    if not ta:
        ta = " "  # Espacio en blanco
    t = t_entry.get()
    if not t:
        t = " "  # Espacio en blanco
    fc = fc_entry.get()
    if not fc:
        fc = " "  # Espacio en blanco
    fr = fr_entry.get()
    if not fr:
        fr = " "  # Espacio en blanco
    cabeza = cabeza_var.get()
    cuello = cuello_var.get()
    torax = torax_var.get()
    abdomen = abdomen_var.get()
    miembros_sup = miembros_sup_var.get()
    miembros_inf = miembros_inf_var.get()
    estudios_clinicos = estudios_clinicos_entry.get()
    if not estudios_clinicos:
        estudios_clinicos = " "  # Espacio en blanco
    tratamiento = tratamiento_entry.get()
    if not tratamiento:
        tratamiento = " "  # Espacio en blanco
    observaciones = observaciones_entry.get()
    if not observaciones:
        observaciones = " "  # Espacio en blanco

    plantilla = llenar_datos_en_plantilla(nombre, edad, sexo, lugar_origen, lugar_residencia, estado_civil,
                                          antecedentes_hf, diabetes, epilepsia, hipertension, cardiovascular,
                                          lueticos, fimicos, neopla, sida, alimentacion, higiene_b, higiene_r, higiene_m,
                                          inmunizaciones, tabaquismo_menos, tabaquismo_mas, alcoholismo_menos,
                                          alcoholismo_mas, tiempo_evolucion, quirurgicos, transfuciones, traumaticos,
                                          alergicos, otros, menarca, ritmo, ivsa, no_parejas, g, p, ab, c, fur,
                                          leucorrea_menos, leucorrea_mas, caracteristicas, padecimiento_actual, peso,
                                          talla, ta, t, fc, fr, cabeza, cuello, torax, abdomen, miembros_sup, miembros_inf,
                                          estudios_clinicos, tratamiento, observaciones)

    ruta_historia_clinica_modificada = guardar_plantilla_modificada(
        plantilla, carpeta, nombre)
    imprimir_mensaje_exito(carpeta)


# Crear la ventana de aplicación con CTk en lugar de Tk
window = ctk.CTk()
window.title("Generador de Historiales clinicos")
window.geometry("350x850")
window.iconbitmap('APP/ico.ico')

# Crear un contenedor Frame para alojar los widgets
content = tk.Frame(window)
content.grid(row=0, column=0, sticky="nsew")

# Configurar el grid
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Crear scrollbar
ctk_textbox_scrollbar = ctk.CTkScrollbar(window, width=15)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

# Conectar el evento de scroll del contenedor al scrollbar
content.configure(yscrollcommand=ctk_textbox_scrollbar.set)

# Hacer que el scrollbar se mueva con el contenedor
ctk_textbox_scrollbar.config(command=content.yview)

nombre_label = tk.Label(content, text="Nombre:")
nombre_entry = tk.Entry(content)
edad_label = tk.Label(content, text="Edad:")
edad_entry = tk.Entry(content)
sexo_label = tk.Label(content, text="Sexo:")
sexo_entry = tk.Entry(content)
lugar_origen_label = tk.Label(content, text="Lugar de Origen:")
lugar_origen_entry = tk.Entry(content)
lugar_residencia_label = tk.Label(content, text="Lugar de Residencia:")
lugar_residencia_entry = tk.Entry(content)
estado_civil_label = tk.Label(content, text="Estado Civil:")
estado_civil_entry = tk.Entry(content)
antecedentes_hf_label = tk.Label(content, text="Ant. H.F.:")
antecedentes_hf_entry = tk.Entry(content)
diabetes_label = tk.Label(content, text="Diabetes:")
diabetes_entry = tk.Entry(content)
epilepsia_label = tk.Label(content, text="Epilepsia:")
epilepsia_entry = tk.Entry(content)
hipertension_label = tk.Label(content, text="Hipertensión:")
hipertension_entry = tk.Entry(content)
cardiovascular_label = tk.Label(content, text="Cardiovascular:")
cardiovascular_entry = tk.Entry(content)
lueticos_label = tk.Label(content, text="Luéticos:")
lueticos_entry = tk.Entry(content)
fimicos_label = tk.Label(content, text="Fímicos:")
fimicos_entry = tk.Entry(content)
neopla_label = tk.Label(content, text="Neopla.:")
neopla_entry = tk.Entry(content)
sida_label = tk.Label(content, text="Sida:")
sida_entry = tk.Entry(content)
alimentacion_label = tk.Label(content, text="Alimentación:")
alimentacion_entry = tk.Entry(content)
higiene_label = tk.Label(content, text="Higiene:")
higiene_b_var = tk.IntVar()
higiene_b_checkbox = tk.Checkbutton(content, variable=higiene_b_var)
higiene_r_label = tk.Label(content, text="Higiene B:")
higiene_r_var = tk.IntVar()
higiene_r_checkbox = tk.Checkbutton(content, variable=higiene_r_var)
higiene_m_label = tk.Label(content, text="Higiene R")
higiene_m_var = tk.IntVar()
higiene_m_checkbox = tk.Checkbutton(content, variable=higiene_m_var)
higiene_m_label = tk.Label(content, text="Higiene M")
higiene_m_var = tk.IntVar()
inmunizaciones_label = tk.Label(content, text="Inmunizaciones:")
inmunizaciones_entry = tk.Entry(content)
tabaquismo_menos_label = tk.Label(content, text="Tabaquismo (-):")
tabaquismo_menos_var = tk.IntVar()
tabaquismo_menos_checkbox = tk.Checkbutton(
    content, variable=tabaquismo_menos_var)
tabaquismo_mas_label = tk.Label(content, text="Tabaquismo (+):")
tabaquismo_mas_var = tk.IntVar()
tabaquismo_mas_checkbox = tk.Checkbutton(content, variable=tabaquismo_mas_var)
alcoholismo_menos_label = tk.Label(content, text="Alcoholismo (-):")
alcoholismo_menos_var = tk.IntVar()
alcoholismo_menos_checkbox = tk.Checkbutton(
    content, variable=alcoholismo_menos_var)
alcoholismo_mas_label = tk.Label(content, text="Alcoholismo (+):")
alcoholismo_mas_var = tk.IntVar()
alcoholismo_mas_checkbox = tk.Checkbutton(content, variable=alcoholismo_mas_var)
tiempo_evolucion_label = tk.Label(content, text="Tiempo de Evolución:")
tiempo_evolucion_entry = tk.Entry(content)
quirurgicos_label = tk.Label(content, text="Quirúrgicos:")
quirurgicos_entry = tk.Entry(content)
transfuciones_label = tk.Label(content, text="Transfusiones:")
transfuciones_entry = tk.Entry(content)
traumaticos_label = tk.Label(content, text="Traumáticos:")
traumaticos_entry = tk.Entry(content)
alergicos_label = tk.Label(content, text="Alergias:")
alergicos_entry = tk.Entry(content)
otros_label = tk.Label(content, text="Otros:")
otros_entry = tk.Entry(content)
menarca_label = tk.Label(content, text="Menarca:")
menarca_entry = tk.Entry(content)
ritmo_label = tk.Label(content, text="Ritmo:")
ritmo_entry = tk.Entry(content)
ivsa_label = tk.Label(content, text="IVSA:")
ivsa_entry = tk.Entry(content)
no_parejas_label = tk.Label(content, text="No. de Parejas:")
no_parejas_entry = tk.Entry(content)
g_label = tk.Label(content, text="G:")
g_entry = tk.Entry(content)
p_label = tk.Label(content, text="P:")
p_entry = tk.Entry(content)
ab_label = tk.Label(content, text="AB:")
ab_entry = tk.Entry(content)
c_label = tk.Label(content, text="C:")
c_entry = tk.Entry(content)
fur_label = tk.Label(content, text="FUR:")
fur_entry = tk.Entry(content)
leucorrea_menos_label = tk.Label(content, text="Leucorrea (-):")
leucorrea_menos_var = tk.IntVar()
leucorrea_menos_checkbox = tk.Checkbutton(content, variable=leucorrea_menos_var)
leucorrea_mas_label = tk.Label(content, text="Leucorrea (+):")
leucorrea_mas_var = tk.IntVar()
leucorrea_mas_checkbox = tk.Checkbutton(content, variable=leucorrea_mas_var)
caracteristicas_label = tk.Label(content, text="Características:")
caracteristicas_entry = tk.Entry(content)
padecimiento_actual_label = tk.Label(content, text="Padecimiento Actual:")
padecimiento_actual_entry = tk.Entry(content)
peso_label = tk.Label(content, text="Peso:")
peso_entry = tk.Entry(content)
talla_label = tk.Label(content, text="Talla:")
talla_entry = tk.Entry(content)
ta_label = tk.Label(content, text="TA:")
ta_entry = tk.Entry(content)
t_label = tk.Label(content, text="T:")
t_entry = tk.Entry(content)
fc_label = tk.Label(content, text="FC:")
fc_entry = tk.Entry(content)
fr_label = tk.Label(content, text="FR:")
fr_entry = tk.Entry(content)
cabeza_label = tk.Label(content, text="Cabeza:")
cabeza_var = tk.IntVar()
cabeza_checkbox = tk.Checkbutton(content, variable=cabeza_var)
cuello_label = tk.Label(content, text="Cuello:")
cuello_var = tk.IntVar()
cuello_checkbox = tk.Checkbutton(content, variable=cuello_var)
torax_label = tk.Label(content, text="Tórax:")
torax_var = tk.IntVar()
torax_checkbox = tk.Checkbutton(content, variable=torax_var)
abdomen_label = tk.Label(content, text="Abdomen:")
abdomen_var = tk.IntVar()
abdomen_checkbox = tk.Checkbutton(content, variable=abdomen_var)
miembros_sup_label = tk.Label(content, text="Miembros Superiores:")
miembros_sup_var = tk.IntVar()
miembros_sup_checkbox = tk.Checkbutton(content, variable=miembros_sup_var)
miembros_inf_label = tk.Label(content, text="Miembros Inferiores:")
miembros_inf_var = tk.IntVar()
miembros_inf_checkbox = tk.Checkbutton(content, variable=miembros_inf_var)
estudios_clinicos_label = tk.Label(content, text="Estudios Clínicos:")
estudios_clinicos_entry = tk.Entry(content)
tratamiento_label = tk.Label(content, text="Tratamiento:")
tratamiento_entry = tk.Entry(content)
observaciones_label = tk.Label(content, text="Observaciones:")
observaciones_entry = tk.Entry(content)


def generar_reporte():
    # Aquí va la lógica para generar el reporte
    pass


generar_reporte_button = tk.Button(
    window, text="Generar Reporte", command=generar_reporte)


nombre_label.pack()
nombre_entry.pack()
edad_label.pack()
edad_entry.pack()
sexo_label.pack()
sexo_entry.pack()
lugar_origen_label.pack()
lugar_origen_entry.pack()
lugar_residencia_label.pack()
lugar_residencia_entry.pack()
estado_civil_label.pack()
estado_civil_entry.pack()
antecedentes_hf_label.pack()
antecedentes_hf_entry.pack()
diabetes_label.pack()
diabetes_entry.pack()
epilepsia_label.pack()
epilepsia_entry.pack()
hipertension_label.pack()
hipertension_entry.pack()
cardiovascular_label.pack()
cardiovascular_entry.pack()
lueticos_label.pack()
lueticos_entry.pack()
fimicos_label.pack()
fimicos_entry.pack()
neopla_label.pack()
neopla_entry.pack()
sida_label.pack()
sida_entry.pack()
alimentacion_label.pack()
alimentacion_entry.pack()
higiene_label.pack()
higiene_b_checkbox.pack()
higiene_r_label.pack()
higiene_r_checkbox.pack()
higiene_m_label.pack()
higiene_m_checkbox.pack()
inmunizaciones_label.pack()
inmunizaciones_entry.pack()
tabaquismo_menos_label.pack()
tabaquismo_menos_checkbox.pack()
tabaquismo_mas_label.pack()
tabaquismo_mas_checkbox.pack()
alcoholismo_menos_label.pack()
alcoholismo_menos_checkbox.pack()
alcoholismo_mas_label.pack()
alcoholismo_mas_checkbox.pack()
tiempo_evolucion_label.pack()
tiempo_evolucion_entry.pack()
quirurgicos_label.pack()
quirurgicos_entry.pack()
transfuciones_label.pack()
transfuciones_entry.pack()
traumaticos_label.pack()
traumaticos_entry.pack()
alergicos_label.pack()
alergicos_entry.pack()
otros_label.pack()
otros_entry.pack()
menarca_label.pack()
menarca_entry.pack()
ritmo_label.pack()
ritmo_entry.pack()
ivsa_label.pack()
ivsa_entry.pack()
no_parejas_label.pack()
no_parejas_entry.pack()
g_label.pack()
g_entry.pack()
p_label.pack()
p_entry.pack()
ab_label.pack()
ab_entry.pack()
c_label.pack()
c_entry.pack()
fur_label.pack()
fur_entry.pack()
leucorrea_menos_label.pack()
leucorrea_menos_checkbox.pack()
leucorrea_mas_label.pack()
leucorrea_mas_checkbox.pack()
caracteristicas_label.pack()
caracteristicas_entry.pack()
padecimiento_actual_label.pack()
padecimiento_actual_entry.pack()
peso_label.pack()
peso_entry.pack()
talla_label.pack()
talla_entry.pack()
ta_label.pack()
ta_entry.pack()
t_label.pack()
t_entry.pack()
fc_label.pack()
fc_entry.pack()
fr_label.pack()
fr_entry.pack()
cabeza_label.pack()
cabeza_checkbox.pack()
cuello_label.pack()
cuello_checkbox.pack()
torax_label.pack()
torax_checkbox.pack()
abdomen_label.pack()
abdomen_checkbox.pack()
miembros_sup_label.pack()
miembros_sup_checkbox.pack()
miembros_inf_label.pack()
miembros_inf_checkbox.pack()
estudios_clinicos_label.pack()
estudios_clinicos_entry.pack()
tratamiento_label.pack()
tratamiento_entry.pack()
observaciones_label.pack()
observaciones_entry.pack()

generar_reporte_button.pack()

window.mainloop()
