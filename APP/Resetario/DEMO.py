import os
import datetime
import openpyxl
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog
from customtkinter import CTkScrollbar
from openpyxl.drawing.image import Image
import mysql.connector
from tkcalendar import DateEntry
from tkinter import Toplevel  # Importar Toplevel


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
    query = "INSERT INTO recetas (fecha, nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, Instruccion1, Tratamiento2, Instruccion2, Tratamiento3, Instruccion3, Tratamiento4, Instruccion4, indicaciones_generales, proxima_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data_with_date = (get_current_date(),) + \
        data  # Agregar la fecha a los datos
    cursor.execute(query, data_with_date)
    cursor.execute("ALTER TABLE recetas AUTO_INCREMENT = 1")
    conexion.commit()


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
    sheet["L42"] = data[8]
    sheet["G16"] = data[9]
    sheet["G44"] = data[9]
    sheet["I18"] = data[10]
    sheet["O48"] = data[10]
    sheet["Y8"] = data[11]
    sheet["Y36"] = data[11]
    sheet["Y10"] = data[12]
    sheet["Y38"] = data[12]
    sheet["Y14"] = data[13]
    sheet["Y42"] = data[13]
    sheet["Y15"] = data[14]
    sheet["Y44"] = data[14]
    sheet["Y19"] = data[15]
    sheet["Y47"] = data[15]
    sheet["Y21"] = data[16]
    sheet["Y48"] = data[16]
    sheet["Y24"] = data[17]
    sheet["Y51"] = data[17]
    sheet["Y25"] = data[18]
    sheet["Y52"] = data[18]
    sheet["E22"] = data[19]
    sheet["E49"] = data[19]
    sheet["AF27"] = data[20]
    sheet["AF55"] = data[20]
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


def update_checkboxes(search_var, options, variables, checkboxes, checkbox_area):
    search_text = search_var.get().lower()
    for checkbox, option, variable in zip(checkboxes, options, variables):
        checkbox_area.delete(checkbox)
    checkboxes.clear()
    variables.clear()
    y = 0
    for option in options:
        if search_text in option.lower():
            check_var = tk.BooleanVar()
            variables.append(check_var)
            checkbox = ctk.CTkCheckBox(checkbox_area, text=option, variable=check_var, onvalue=True, offvalue=False, text_color='black')
            checkboxes.append(checkbox_area.create_window(0, y*30, window=checkbox, anchor='nw'))
            y += 1
    checkbox_area.config(scrollregion=checkbox_area.bbox('all'))


def show_multi_select_dialog(master, options, var):
    dialog = tk.Toplevel(master)
    dialog.title("Seleccione Tratamientos")
    dialog.geometry("400x350")  # Establecer las dimensiones de la ventana

    search_frame = tk.Frame(dialog)
    search_frame.pack(padx=3, pady=3)

    search_label = tk.Label(search_frame, text="Buscador:")
    search_label.pack(side="left")

    search_var = tk.StringVar()
    search_bar = tk.Entry(search_frame, textvariable=search_var)
    search_bar.pack(side="left")

    frame = tk.Frame(dialog)  # Crear un marco para el scrollbar y los checkbox
    frame.pack()

    # scrollbar = tk.Scrollbar(frame)  # Crear el scrollbar -- remover esta línea

    # Crear el CTkScrollbarf
    scrollbar = CTkScrollbar(frame, command=None)
    scrollbar.pack(side="right", fill="y")

    checkbox_area = tk.Canvas(frame, yscrollcommand=scrollbar.set)  # Crear el área de checkbox y conectarla al scrollbar
    checkbox_area.pack(side="left")

    scrollbar.config(command=checkbox_area.yview)  # Configurar el scrollbar para actualizar la vista del área de checkbox

    variables = []
    checkboxes = []
    for option in options:
        check_var = tk.BooleanVar()
        variables.append(check_var)
        checkbox = ctk.CTkCheckBox(checkbox_area, text=option, variable=check_var, onvalue=True, offvalue=False, text_color='black')
        checkboxes.append(checkbox_area.create_window(0, len(variables)*30, window=checkbox, anchor='nw'))

    checkbox_area.config(scrollregion=checkbox_area.bbox('all'))  # Configurar la región de desplazamiento del área de checkbox para que incluya todos los checkbox

    search_var.trace("w", lambda *args: update_checkboxes(search_var, options, variables, checkboxes, checkbox_area))

    submit_button = ctk.CTkButton(dialog, text="Submit", command=lambda: var.set(", ".join([option for option, selected in zip(options, variables) if selected.get()])))
    submit_button.pack()


# Obtener los tratamientos de la base de datos
def get_treatments(cursor):
    cursor.execute("SELECT nombre FROM tratamientos")
    return [row[0] for row in cursor.fetchall()]


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
window = ctk.CTk()
window.title("Generador de Recetas Médicas")
window.geometry("430x690")
window.configure(background='#242324')

labels = [
    "Nombre:", "Edad:", "Temp:", "T.A.", "Peso:", "F.C.", "Talla:", "F.R.",
    "Circun. Abdom.", "I.D:", "Alergias:", "Tratamiento 1:", "Tratamiento 2:", "Tratamiento 3:", "Tratamiento 4:", "Indicaciones Generales:",
    "Próxima Cita:"
]

entries = []

# Centrar la ventana en la pantalla
window.update_idletasks()  # Actualizar la ventana antes de obtener las dimensiones
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{x}+{y}")

# Crear las etiquetas y las entradas de datos
conexion = get_database_connection()
cursor = get_database_cursor(conexion)
treatments = get_treatments(cursor)

for index, label_text in enumerate(labels):
    label = ctk.CTkLabel(window, text=label_text, width=20)
    label.grid(row=index, column=0, padx=10, pady=5)

    if label_text in ["Tratamiento 1:", "Tratamiento 2:", "Tratamiento 3:", "Tratamiento 4:"]:
        var = tk.StringVar()

        # Crea un frame para el combobox y la entrada de descripción
        treatment_frame = tk.Frame(window)
        treatment_frame.grid(row=index, column=1, padx=10, pady=5)

        # Combobox para seleccionar tratamientos
        combobox = ctk.CTkComboBox(treatment_frame, values=treatments, variable=var)
        combobox.pack(side="left")

        # Entrada para la descripción del tratamiento
        description_entry = ctk.CTkEntry(treatment_frame, width=100)
        description_entry.pack(side="left")
        entries.append(var)
        entries.append(description_entry)  # Añade la entrada de descripción a las entradas

    else:
        entry = DateEntry(window, date_pattern='dd-mm-yyyy', height=20, width=40) if label_text == "Próxima Cita:" else ctk.CTkEntry(window, width=200)
        entry.grid(row=index, column=1, padx=10, pady=5)
        entries.append(entry)


# Crear el botón para generar el reporte
generate_button = ctk.CTkButton(window, text="Generar Reporte", command=lambda: generate_report(entries))
generate_button.grid(row=len(labels), columnspan=2, padx=10, pady=10)

window.mainloop()
