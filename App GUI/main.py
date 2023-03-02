# IMPORTS
import tkinter as tk
import customtkinter as ctk
import widgets


# CLASES

class MainWindow:

    def __init__(self, ventana):
        self.wind = ventana
        # Título
        self.wind.title("Generador de Señales")
        # Dimensiones
        self.dimentions = (500, 600)
        self.wind.geometry(f"{self.dimentions[0]}x{self.dimentions[1]}")
        self.wind.maxsize(self.dimentions[0], self.dimentions[1])
        self.wind.minsize(self.dimentions[0], self.dimentions[1])
        # MenuBar
        self.menubar = widgets.BarraMenu(ventana)
        # Channel 1
        self.ch1 = widgets.Canal(ventana, 1)
        self.ch1.frame.grid(padx=(80, 50), pady=(25, 0))
        self.submit = widgets.Submit(ventana, self.ch1)
        self.submit.boton.grid(padx=(80, 50), pady=(100, 50))


if __name__ == '__main__':
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    window.bind("<Button-1>", lambda event: event.widget.focus_set())
    app = MainWindow(window)
    window.mainloop()
