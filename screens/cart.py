import tkinter as tk
from constants import style
from tienda import Tienda, Carrito

class Cart(tk.Frame):
    def __init__(self, parent, controller, tienda, carrito):
        super().__init__(parent)
        self.configure(bg=style.BACKGROUND)
        self.controller = controller
        self.tienda: Tienda = tienda
        self.carrito: Carrito = carrito

        self.init_widgets()
        self.update_view()

    def init_widgets(self):
        buttons_frame = tk.Frame(self, bg=style.BACKGROUND)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        tk.Button(
            buttons_frame,
            text="Volver",
            justify=tk.CENTER,
            **style.STYLE,
            command=lambda: self.controller.show_frame("HOME")
        ).pack(fill=tk.X, pady=5)

        tk.Label(self, text="Tu carrito", justify=tk.CENTER, **style.STYLE).pack(
            side=tk.TOP, fill=tk.X, expand=True, padx=22, pady=11
        )
        
        self.product_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.product_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
            
    def update_view(self):
        for widget in self.product_frame.winfo_children():
            widget.destroy()
        
        for producto, cantidad in self.carrito.productos:
            tk.Label(
                self.product_frame,
                text=f"{producto.nombre} - Cantidad: {cantidad} - Precio: ${producto.precio * cantidad:.2f}",
                justify=tk.CENTER,
                **style.STYLE
            ).pack(side=tk.TOP, fill=tk.X, expand=True, padx=22, pady=5)
            
    def actualizar_carrito(self):
        self.update_view()
        
            
        
