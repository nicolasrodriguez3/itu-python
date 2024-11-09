import tkinter as tk
from tkinter import messagebox
from constants import style
from tienda import Tienda, Producto


class Products(tk.Frame):
    def __init__(self, parent, controller, tienda, carrito):
        super().__init__(parent)
        self.controller = controller
        self.tienda: Tienda = tienda
        self.carrito = carrito
        self.configure(bg=style.BACKGROUND)
        self.init_widgets()

        self.nombre_entry = tk.StringVar()
        self.precio_entry = tk.StringVar()
        self.stock_entry = tk.StringVar()

    def init_widgets(self):
        # Frame para los botones de acciones
        buttons_frame = tk.Frame(self, bg=style.BACKGROUND)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        tk.Button(
            buttons_frame,
            text="Volver",
            justify=tk.CENTER,
            **style.STYLE,
            command=lambda: self.controller.show_frame("HOME")
        ).pack(fill=tk.X, pady=5)

        self.product_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.product_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for producto in self.tienda.productos:
            product_label = tk.Label(self.product_frame, text=producto.nombre, **style.STYLE)
            product_label.pack(padx=5, pady=5)

            add_to_cart_button = tk.Button(
                self.product_frame,
                text="Agregar al carrito",
                **style.STYLE,
                command=lambda p=producto: self.agregar_al_carrito(p, 1)
            )
            add_to_cart_button.pack(padx=5, pady=5)

    def agregar_al_carrito(self, producto, cantidad):
        try:
            self.carrito.agregar(producto, cantidad)
            messagebox.showinfo("Éxito", f"El producto '{producto.nombre}' fue agregado al carrito.")
            self.controller.update_cart()
        except Exception as ex:
            messagebox.showerror("Error", "Ocurrio un error al agregar el producto.")
            print(ex)
            