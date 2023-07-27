import mysql.connector
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pyperclip

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="AME"
    )

def get_treatment_names():
    cnx = get_database_connection()
    cursor = cnx.cursor()

    query = "SELECT nombre FROM tratamientos;"

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    cnx.close()

    return [row[0] for row in result]

def update_list(*args):
    search_term = search_var.get()
    listbox.delete(0, tk.END)
    for item in treatment_names:
        if search_term.lower() in item.lower():
            listbox.insert(tk.END, item)

def copy_to_clipboard(event):
    # Obtiene el elemento seleccionado
    selection = listbox.curselection()
    if selection:
        selected_item = listbox.get(selection)
        # Copia el texto al portapapeles
        pyperclip.copy(selected_item)

# Aplicación con el tema 'calm'
root = ThemedTk(theme="calm")
root.title("Recetario AME")  # Cambiar a tu título preferido
root.geometry("400x300")

# Variable para la búsqueda
search_var = tk.StringVar()
search_var.trace("w", update_list)

# Crea un frame para mantener juntos la etiqueta y la caja de entrada
frame = ttk.Frame(root)
frame.pack()

# Etiqueta del buscador
search_label = ttk.Label(frame, text="Buscador:")
search_label.pack(side=tk.LEFT)

# Entrada de búsqueda
search_entry = ttk.Entry(frame, textvariable=search_var)
search_entry.pack(side=tk.LEFT)

# Listbox para mostrar los nombres de los tratamientos
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)
# Bindea el evento de doble click al Listbox
listbox.bind("<Double-Button-1>", copy_to_clipboard)

# Obtén los nombres de los tratamientos
treatment_names = get_treatment_names()

# Llena la listbox con los nombres de los tratamientos
for name in treatment_names:
    listbox.insert(tk.END, name)

root.mainloop()
