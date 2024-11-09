import tkinter as tk
from tkinter import messagebox, filedialog
from constants import style
from tienda import Tienda
from helpers.gestor_archivos import GestorArchivos


class Management(tk.Frame):
    def __init__(self, parent, controller, tienda, carrito):
        super().__init__(parent)
        self.controller = controller
        self.tienda: Tienda = tienda
        self.configure(bg=style.BACKGROUND)
        self.init_widgets()
        
        self.nombre_entry = tk.StringVar()
        self.precio_entry = tk.StringVar()
        self.stock_entry = tk.StringVar()

        self.show_form("new_product")


    def init_widgets(self):
        tk.Label(self, text="Gestión de Productos", font=("Arial", 16)).pack(pady=10)

        # Frame para los botones
        buttons_frame = tk.Frame(self, bg=style.BACKGROUND)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Frame para el formulario
        self.form_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botones
        tk.Button(
            buttons_frame,
            text="Volver",
            justify=tk.CENTER,
            **style.STYLE,
            command=lambda: self.controller.show_frame("HOME")
        ).pack(fill=tk.X, pady=5)
        
        tk.Button(
            buttons_frame,
            text="Nuevo producto",
            **style.STYLE,
            command=lambda: self.show_form("new_product")
        ).pack(fill=tk.X, pady=5)

        tk.Button(
            buttons_frame,
            text="Cambiar precio",
            **style.STYLE,
            command=lambda: self.show_form("change_price")
        ).pack(fill=tk.X, pady=5)

        tk.Button(
            buttons_frame,
            text="Cambiar stock",
            **style.STYLE,
            command=lambda: self.show_form("change_stock")
        ).pack(fill=tk.X, pady=5)

        tk.Button(
            buttons_frame,
            text="Exportar listado de productos",
            **style.STYLE,
            command=self.exportar_productos
        ).pack(fill=tk.X, pady=5)
        
        

    def show_form(self, action):
        # Limpia el frame de formulario antes de mostrar el nuevo formulario
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        if action == "new_product":
            self.new_product_form()
        elif action == "change_price":
            self.change_price_form()
        elif action == "change_stock":
            self.change_stock_form()

    def new_product_form(self):
        # Formulario para agregar un nuevo producto
        tk.Label(self.form_frame, text="Nuevo Producto", **style.STYLE).pack(pady=10)
        tk.Label(self.form_frame, text="Nombre", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.nombre_entry).pack(pady=5)
        tk.Label(self.form_frame, text="Precio", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.precio_entry).pack(pady=5)
        tk.Label(self.form_frame, text="Stock", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.stock_entry).pack(pady=5)
        
        tk.Button(self.form_frame, text="Guardar", **style.STYLE, command=self.agregar_producto).pack(pady=10)

    def change_price_form(self):
        # Formulario para cambiar el precio de un producto
        tk.Label(self.form_frame, text="Cambiar Precio", **style.STYLE).pack(pady=10)
        
        tk.Label(self.form_frame, text="Nombre", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.nombre_entry).pack(pady=5)
        
        tk.Label(self.form_frame, text="Precio", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.precio_entry).pack(pady=5)
        
        tk.Button(self.form_frame, text="Actualizar", **style.STYLE, command=self.change_stock).pack(pady=10)

    def change_stock_form(self):
        # Formulario para cambiar el stock de un producto
        tk.Label(self.form_frame, text="Cambiar Stock", **style.STYLE).pack(pady=10)
        
        tk.Label(self.form_frame, text="Nombre", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.nombre_entry).pack(pady=5)
        
        tk.Label(self.form_frame, text="Stock", **style.STYLE).pack(pady=5)
        tk.Entry(self.form_frame, **style.STYLE, textvariable=self.stock_entry).pack(pady=5)
        
        tk.Button(self.form_frame, text="Actualizar", **style.STYLE, command=self.change_stock).pack(pady=10)


    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            stock = int(self.stock_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El precio y el stock deben ser numéricos.")
            return

        try:
            self.tienda.nuevo_producto(nombre, precio, stock)
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
        
        self.nombre_entry.set("")
        self.precio_entry.set("")
        self.stock_entry.set("")


    def change_stock(self):
        nombre = self.nombre_entry.get()
        try:
            stock = int(self.stock_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El stock debe ser numérico.")
            return
        
        try:
            producto = self.tienda.buscar_producto(nombre)
        except Exception:
            messagebox.showerror("Error", "El producto no existe.")
            return
        
        self.tienda.reabastecer_producto(producto, stock)


    def change_price(self):
        nombre  = self.nombre_entry.get()
        try:
            precio = int(self.precio_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser numérico.")
            return
        
        try:
            producto = self.tienda.buscar_producto(nombre)
        except Exception:
            messagebox.showerror("Error", "El producto no existe.")
            return
        
        self.tienda.actualizar_precio_producto(producto, precio)
        
    def exportar_productos(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filename:
            GestorArchivos.exportar_csv(self.tienda.productos, filename)
            messagebox.showinfo("Éxito", "Se exportaron los productos correctamente.")