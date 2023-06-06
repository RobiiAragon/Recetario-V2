import tkinter as tk
from tkinter import ttk
import sqlite3

def agregar_usuario():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    
    conn = sqlite3.connect('basedatos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()
    
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    
def mostrar_usuarios():
    conn = sqlite3.connect('basedatos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    
    usuarios = [f"{row[0]} - {row[1]}, {row[2]}" for row in rows]
    usuarios_combobox['values'] = usuarios

root = tk.Tk()

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack()

edad_label = tk.Label(root, text="Edad:")
edad_label.pack()
edad_entry = tk.Entry(root)
edad_entry.pack()

agregar_button = tk.Button(root, text="Agregar usuario", command=agregar_usuario)
agregar_button.pack()

mostrar_button = tk.Button(root, text="Mostrar usuarios", command=mostrar_usuarios)
mostrar_button.pack()

usuarios_combobox = ttk.Combobox(root)
usuarios_combobox.pack()

root.mainloop()
