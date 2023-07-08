import os
import datetime
import openpyxl
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, Toplevel
from openpyxl.drawing.image import Image
import mysql.connector
from tkcalendar import DateEntry

# Definición de constantes
DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")  # La contraseña se obtiene desde una variable de entorno
DATABASE_NAME = "AME"
DATE_PATTERN = 'dd-mm-yyyy'
DATE_FORMAT = "%d-%m-%Y"

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def get_cursor(self, connection):
        return connection.cursor()

    def save_to_database(self, data, cursor, connection):
        query = "INSERT INTO recetas (fecha, nombre, edad, temp, ta, peso, fc, talla, fr, circun_abdom, id, alergias, tratamiento, indicaciones_generales, proxima_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data_with_date = (datetime.datetime.now().strftime(DATE_FORMAT),) + data
        cursor.execute(query, data_with_date)
        cursor.execute("ALTER TABLE recetas AUTO_INCREMENT = 1")
        connection.commit()

    def get_treatments(self, cursor):
        cursor.execute("SELECT nombre FROM tratamientos")
        return [row[0] for row in cursor.fetchall()]

class Application:
    def __init__(self, window, database, labels):
        self.window = window
        self.database = database
        self.labels = labels
        self.entries = []

    def validate_inputs(self, entries):
        # Aquí puedes agregar tu lógica para validar las entradas
        return True

    def ask_questions(self):
        answers = []
        for entry in self.entries:
            answer = entry.get() if entry.get() else " "
            answers.append(answer)
        return tuple(answers)

    def generate_report(self):
        data = self.ask_questions()
        if not self.validate_inputs(data):
            messagebox.showerror("Error", "Por favor, introduzca datos válidos.")
            return
        connection = self.database.get_connection()
        cursor = self.database.get_cursor(connection)
        self.database.save_to_database(data, cursor, connection)
        connection.close()
        # Aquí puedes continuar con el resto de tu lógica para generar el reporte...

    def run(self):
        connection = self.database.get_connection()
        cursor = self.database.get_cursor(connection)
        treatments = self.database.get_treatments(cursor)
        connection.close()

        for index, label_text in enumerate(self.labels):
            label = ctk.CTkLabel(self.window, text=label_text, width=20)
            label.grid(row=index, column=0, padx=10, pady=5)
            if label_text == "Tratamiento:":
                var = tk.StringVar()
                button = tk.Button(self.window, text="Seleccionar Tratamientos", command=lambda: self.show_multi_select_dialog(treatments, var))
                button.grid(row=index, column=1, padx=10, pady=5)
                self.entries.append(var)
            else:
                entry = DateEntry(self.window, date_pattern=DATE_PATTERN, height=20, width=40) if label_text == "Próxima Cita:" else ctk.CTkEntry(self.window, width=200)
                entry.grid(row=index, column=1, padx=10, pady=5)
                self.entries.append(entry)

        generate_button = ctk.CTkButton(self.window, text="Generar Reporte", command=self.generate_report)
        generate_button.grid(row=len(self.labels), columnspan=2, padx=10, pady=10)

        self.window.mainloop()

if __name__ == "__main__":
    labels = [
        "Nombre:", "Edad:", "Temp:", "T.A.", "Peso:", "F.C.", "Talla:", "F.R.",
        "Circun. Abdom.", "I.D:", "Alergias:", "Tratamiento:", "Indicaciones Generales:",
        "Próxima Cita:"
    ]

    window = ctk.CTk()
    window.title("Generador de Recetas Médicas")
    window.geometry("410x590")
    window.configure(background='#242324')

    database = Database(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME)

    app = Application(window, database, labels)
    app.run()
