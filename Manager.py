import tkinter as tk
from constants import config, style
from screens import Home, Management, Products, Cart


class Manager(tk.Tk):
    def __init__(self, tienda, carrito, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TP 1 - Curso Python + FastAPI")
        self.geometry("600x400")
        self.tienda = tienda
        self.carrito = carrito
        
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.configure(bg=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        
        for key, FrameClass in zip(config.SECTIONS.keys(), (Home, Management, Products, Cart)):
            frame = FrameClass(container, self, tienda=self.tienda, carrito=carrito)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)


        self.show_frame("HOME")
            
            
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
    def update_cart(self):
        self.frames["CART"].actualizar_carrito()
