import os
import datetime
import shutil
import webbrowser
import tkinter as tk
from tkinter import ttk
from datetime import date
from ttkthemes import ThemedTk
from tkinter import filedialog
from openpyxl.drawing.image import Image
import mysql.connector
from tkcalendar import DateEntry
from tkinter import Toplevel
from babel.dates import format_date, format_datetime, format_time
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pdfrw
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page['/Annots']
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]  # remove brackets around the field name
                    if key in data_dict:
                        annotation.update(
                            pdfrw.IndirectPdfDict(V='{}'.format(data_dict[key]))
                        )
    PdfWriter().write(output_pdf_path, template_pdf)

def copy_and_rename_pdf_template(folder, data):
    # Ruta de la plantilla de PDF
    pdf_template_path = 'PLANTILLAS/PDF/receta.pdf'

    # Obteniendo la fecha actual y el nombre del paciente para el nuevo nombre del archivo
    current_date = get_current_date()
    patient_name = data[1].replace(' ', '_')  # Suponiendo que "Nombre del Paciente:" es la segunda etiqueta

    # Creando la ruta del nuevo archivo PDF
    new_pdf_path = os.path.join(folder, f"Receta_{patient_name}_{current_date}.pdf")

    # Copiando la plantilla a la nueva ruta con el nuevo nombre
    shutil.copy(pdf_template_path, new_pdf_path)

    return new_pdf_path

# Connection to the database
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="AME"
    )

# Get database cursor
def get_database_cursor(connection):
    return connection.cursor()

# Get current date
def get_current_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")

# Create a folder with current date if it doesn't exist
def create_folder_with_current_date():
    current_date = get_current_date()
    folder = os.path.join(os.getcwd(), "Recetarios", current_date)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

# Ask questions and return answers
def ask_questions(entries):
    answers = []
    for entry in entries:
        # Space if there's no answer
        answer = entry.get() if entry.get() else " "
        answers.append(answer)
    print(f'Número de respuestas recogidas: {len(answers)}')  # Añadir esta línea
    return tuple(answers)

# Save data to the database
def save_to_database(cursor, connection, data):
    query = """
        INSERT INTO recetas (
            fecha, nombre, edad, temp, ta, fr, fc, id, talla, peso, 
            circun_abdom, alergias, tratamiento, Instruccion1, Tratamiento2, Instruccion2,
            Tratamiento3, Instruccion3, Tratamiento4, Instruccion4, 
            indicaciones_generales, proxima_cita
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s
        )
    """
    cursor.execute(query, data)
    connection.commit()

# Print success message and open the folder where the recipe was saved
def print_success_message_and_open_folder(folder):
    print("La receta modificada se ha guardado en la carpeta", folder)
    os.startfile(folder)

# Get autocomplete list from the database
def get_autocomplete_list_from_db():
    connection = get_database_connection()
    cursor = get_database_cursor(connection)
    cursor.execute("SELECT nombre FROM tratamientos")
    return [row[0] for row in cursor.fetchall()]

# Generate report
def generate_report(entries):
    folder = create_folder_with_current_date()
    data = ask_questions(entries)
    connection = get_database_connection()
    cursor = get_database_cursor(connection)
    save_to_database(cursor, connection, data)
    save_data_to_text_file(folder, data)
    
    # Copia y renombra la plantilla del PDF y obtén la ruta
    new_pdf_path = copy_and_rename_pdf_template(folder, data)
    
    # Abre el nuevo archivo PDF en el navegador predeterminado
    webbrowser.open_new(new_pdf_path)
    
    print_success_message_and_open_folder(folder)
    return new_pdf_path

def save_data_to_text_file(folder, data):
    # Create text file path
    current_date = get_current_date()
    patient_name = entries[1].get()  # Assuming "Nombre del Paciente:" is the second label
    patient_name = patient_name.replace(' ', '_')  # Replace spaces with underscores for filename
    text_file_path = os.path.join(folder, f"Receta_temporal_de_{patient_name}_atendido_el_dia_{current_date}.txt")

    # Write data to text file
    with open(text_file_path, "w") as text_file:
        text_file.write(f"FECHA Y HORA#0: {current_date}\n")
        for i, (label_text, datum) in enumerate(zip(labels[1:], data[1:]), start=1):
            # Remove colon at the end of label text
            label_text = label_text[:-1]
            text_file.write(f"{label_text.upper()}#{i}: {datum}\n")

class AutocompleteEntry(ttk.Entry):
    def __init__(self, autocomplete_list, *args, **kwargs):
        super(AutocompleteEntry, self).__init__(*args, **kwargs)
        self.autocomplete_list = autocomplete_list
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = tk.StringVar()
        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Return>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.lb_up = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.lb_up:
                self.lb.destroy()
                self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = tk.Toplevel(self)
                    self.lb.geometry("500x200")
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.listbox = tk.Listbox(self.lb)
                    self.listbox.pack(side="left", fill="both", expand=True)
                    self.scrollbar = ttk.Scrollbar(self.lb, orient="vertical", command=self.listbox.yview)
                    self.scrollbar.pack(side="right", fill="y")
                    self.listbox.config(yscrollcommand=self.scrollbar.set)
                    self.lb_up = True
                self.listbox.delete(0, tk.END)
                for w in words:
                    self.listbox.insert(tk.END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):
        if self.lb_up:
            self.var.set(self.listbox.get(tk.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)

    def up(self, event):
        if self.lb_up:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def down(self, event):
        if self.lb_up:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
            if index != tk.END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [w for w in self.autocomplete_list if w.lower().startswith(self.var.get().lower())]
    
# Crear y configurar la ventana
window = ThemedTk(theme="calm")  # Seleccionar un tema que te guste
window.title("Recetario AME")  # Cambiar a tu título preferido
window.geometry("530x500")

# Agregando padding y estilo a los widgets
style = ttk.Style()
style.configure("TEntry", padding=5)
style.configure("TLabel", padding=5)
style.configure("TButton", padding=5)

# Modificar los colores de fondo, de primer plano y el tipo de letra
style.configure(".", background="white", foreground="black", font=("ARIAL", 10))

# Cambiar también los colores de los botones
style.map("TButton",
    background=[("active", "darkgrey"), ("pressed", "grey")],
    foreground=[("active", "black")],
)

labels = ["Fecha y Hora:", "Nombre del Paciente:", "Edad:", "Temp:", "T.A:", "F.R:", "F.C:", "ID:", "Peso:", "Talla:", "Circun. Abdom:", "Alergias:", "Tratamiento 1:", "Instruccion 1:", "Tratamiento 2:", "Instruccion 2:", "Tratamiento 3:", "Instruccion 3:", "Tratamiento 4:", "Instruccion 4:", "Indicaciones Generales:", "Próxima Cita:"]
entries = []

frame = ttk.Frame(window)
frame.pack(fill='both', expand=True)
canvas = tk.Canvas(frame)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear labels y data entries
autocomplete_list = get_autocomplete_list_from_db()
for index, label_text in enumerate(labels):
    label = ttk.Label(scrollable_frame, text=label_text)
    label.grid(row=index, column=0, padx=10, pady=5)
    # Cambiar el tamaño de los campos de entrada
    if label_text == "Próxima Cita:":
        entry = DateEntry(scrollable_frame, width=50, locale='es_ES')
    elif label_text == "Fecha y Hora:":
        entry = ttk.Entry(scrollable_frame, width=50)
        entry.insert(0, get_current_date())  # Insert current date
    elif "Tratamiento" in label_text:
        entry = AutocompleteEntry(autocomplete_list, scrollable_frame, width=50)
    else:
        entry = ttk.Entry(scrollable_frame, width=50)
    entry.grid(row=index, column=1, padx=10, pady=5)
    entries.append(entry)

# Crear botón para generar reporte
generate_report_button = ttk.Button(scrollable_frame, text="Generar Reporte", command=lambda: generate_report(entries))
generate_report_button.grid(row=len(labels), column=0, padx=10, pady=10, columnspan=2)


canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
window.mainloop()
