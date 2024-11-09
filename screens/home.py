import tkinter as tk
from constants import style, config

class Home(tk.Frame):
    def __init__(self, parent, controller, tienda, carrito):
        super().__init__(parent)
        self.configure(bg=style.BACKGROUND)
        self.controller = controller
        self.tienda = tienda

        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self, text="Bienvenido a la tienda", justify=tk.CENTER, **style.STYLE
        ).pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=22, pady=11)

        for key, value in config.SECTIONS.items():
            if key == "HOME":
                continue

            tk.Button(
                self,
                text=value,
                justify=tk.CENTER,
                **style.STYLE,
                command=lambda key=key: self.controller.show_frame(key)
            ).pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=22, pady=11)
