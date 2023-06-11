import tkinter
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


def button_function():
    date = entry.get()  # Obtener la fecha ingresada por el usuario
    print("Fecha ingresada:", date)


# Crear una etiqueta y un campo de entrada para solicitar la fecha
label = customtkinter.CTkLabel(app, text="Fecha:")
label.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(app)
entry.place(relx=0.6, rely=0.4, anchor=tkinter.CENTER)


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="Mostrar información", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
