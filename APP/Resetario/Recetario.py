import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import ttk  # Mejora los widgets
from tkinter import filedialog
from openpyxl.drawing.image import Image
import mysql.connector
from tkcalendar import DateEntry


# Conexión a la base de datos
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="AME"
    )


# Crear el cursor de la base de datos
def get_database_cursor(conexion):
    return conexion.cursor()


# Obtener la fecha actual
def get_current_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


# Crear una carpeta con la fecha actual si no existe
def create_folder_with_current_date():
    current_date = get_current_date()
    folder = os.path.join(os.getcwd(), "Recetarios", current_date)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


# Hacer preguntas y devolver las respuestas
def ask_questions(entries):
    answers = []
    for entry in entries:
        # Espacio en blanco si no hay respuesta
        answer = entry.get() if entry.get() else " "
        answers.append(answer)
    return tuple(answers)


# Guardar datos en la base de datos
def save_to_database(cursor, conexion, data):
    # Insertar los datos en la base de datos
    query = "INSERT INTO recetas (fecha, nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data_with_date = (get_current_date(),) + \
        data  # Agregar la fecha a los datos
    cursor.execute(query, data_with_date)
    cursor.execute("ALTER TABLE recetas AUTO_INCREMENT = 1")
    conexion.commit()


# Cargar y modificar la plantilla con los datos recogidos
# Cargar y modificar la plantilla con los datos recogidos
def fill_data_into_template(template, data):
    sheet = template.active
    sheet["J4"] = data[0]
    sheet["J32"] = data[0]
    sheet["H6"] = data[1]
    sheet["H34"] = data[1]
    sheet["BB4"] = get_current_date()
    sheet["BB32"] = get_current_date()
    sheet["Q6"] = data[2]
    sheet["Q34"] = data[2]
    sheet["G8"] = data[3]
    sheet["G36"] = data[3]
    sheet["Q8"] = data[4]
    sheet["Q36"] = data[4]
    sheet["G10"] = data[5]
    sheet["G38"] = data[5]
    sheet["Q10"] = data[6]
    sheet["Q38"] = data[6]
    sheet["G12"] = data[7]
    sheet["G40"] = data[7]
    sheet["L14"] = data[8]
    sheet["K42"] = data[8]
    sheet["G16"] = data[9]
    sheet["G44"] = data[9]
    sheet["H18"] = data[10]
    sheet["H46"] = data[10]
    sheet["Y8"] = data[11]
    sheet["Y36"] = data[11]
    sheet["O21"] = data[12]
    sheet["O48"] = data[12]
    sheet["AF27"] = data[13]
    sheet["AF55"] = data[13]
    return template


# Guardar la plantilla modificada
def save_modified_template(template, folder, pdf_name):
    modified_recipe_path = os.path.join(folder, f"{pdf_name}.xlsx")
    template.save(modified_recipe_path)
    return modified_recipe_path


# Imprimir el mensaje de éxito y abrir la carpeta donde se guardó la receta
def print_success_message_and_open_folder(folder):
    print("La receta modificada se ha guardado en la carpeta", folder)
    os.startfile(folder)


# Generar el reporte
def generate_report(entries):
    folder = create_folder_with_current_date()
    data = ask_questions(entries)
    conexion = get_database_connection()
    cursor = get_database_cursor(conexion)
    save_to_database(cursor, conexion, data)
    template = openpyxl.load_workbook("PLANTILLAS XLSX/receta.xlsx")
    modified_template = fill_data_into_template(template, data)
    modified_recipe_path = save_modified_template(
        modified_template, folder, data[0])
    print_success_message_and_open_folder(folder)


# Crear y configurar la ventana
window = tk.Tk()
window.title("Generador de Recetas Medicas")
# Aumenté el tamaño de la ventana para acomodar los nuevos widgets
window.geometry("1200x400")
window.configure(background='lightgrey')  # Cambio de color de fondo
window.iconbitmap('ico.ico')

labels = [
    "Nombre:", "Edad:", "Temp:", "T.A.:", "Peso:", "F.C.:", "Talla:", "F.R.:",
    "Circun. Abdom.:", "I.D:", "Alergias:", "Tratamiento:", "Indicaciones Generales:",
    "Próxima Cita:"
]

entries = []

# Crear un estilo para los widgets
style = ttk.Style()
style.configure('TLabel', background='lightgrey', font=('Arial', 11))
style.configure('TEntry', fieldbackground='white', foreground='black')
style.configure('TButton', font=('Arial', 12, 'bold'), borderwidth='1')
style.configure('TLabelframe', background='lightgrey',
                foreground='darkblue', font=('Arial', 14, 'bold'))

# Crear frames para agrupar los campos
patient_data_frame = ttk.LabelFrame(window, text=" Datos del paciente ")
patient_data_frame.pack(pady=10, padx=10, fill='x')

medical_data_frame = ttk.LabelFrame(window, text=" Datos médicos ")
medical_data_frame.pack(pady=10, padx=10, fill='x')

allergies_frame = ttk.LabelFrame(window, text=" Alergias y Tratamiento ")
allergies_frame.pack(pady=10, padx=10, fill='x')

instructions_frame = ttk.LabelFrame(window, text=" Indicaciones y Cita ")
instructions_frame.pack(pady=10, padx=10, fill='x')

frames = [patient_data_frame, medical_data_frame,
          allergies_frame, instructions_frame]

# Crear las etiquetas y las entradas de datos
for index, label_text in enumerate(labels):
    # Utilizamos el operador de división entera para seleccionar el frame
    label = ttk.Label(frames[index//4], text=label_text)
    label.pack(side='left', padx=(10, 0))
    entry = DateEntry(frames[index//4], date_pattern='dd-mm-yyyy',
                      width=30) if label_text == "Próxima Cita:" else ttk.Entry(frames[index//4], width=30)
    entry.pack(side='left', padx=(0, 10))
    entries.append(entry)

# Crear el botón para generar el reporte
generate_button = ttk.Button(
    window, text="Generar Reporte", command=lambda: generate_report(entries))
generate_button.pack(pady=10)

# Crear la etiqueta para los mensajes
message_label = tk.Label(window, wraplength=350,
                         bg='lightgrey', fg='red', font=('Arial', 11))
message_label.pack(pady=10)

window.mainloop()
