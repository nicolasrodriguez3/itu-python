import csv, json
from tienda.producto import Producto


class GestorArchivos:
    @staticmethod
    def exportar_csv(productos: list[Producto], filename: str):
        try:
            with open(filename, "w", newline="") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["Nombre", "Precio", "Stock"])
                for producto in productos:
                    writer.writerow([producto.nombre, producto.precio, producto.stock])

            print(f"Se exporto correctamente al formato CSV")

        except Exception as e:
            print(f"Error al exportar productos: {e}")

    @staticmethod
    def exportar_json(productos: list[Producto], filename: str):
        try:
            with open(filename, "w") as archivo:
                productos_dict = [
                    {
                        "nombre": producto.nombre,
                        "precio": producto.precio,
                        "stock": producto.stock,
                    }
                    for producto in productos
                ]
                json.dump(productos_dict, archivo, indent=4)

            print(f"Se exporto correctamente al formato JSON")

        except Exception as e:
            print(f"Error al exportar productos: {e}")
