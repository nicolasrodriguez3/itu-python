from typing import Literal, List
from tienda.carrito import Carrito
from tienda.producto import Producto
from helpers.gestor_archivos import GestorArchivos


class Tienda:
    def __init__(self, nombre: str, productos: List[Producto] = []) -> None:
        self.__nombre: str = nombre
        self.__productos: List[Producto] = productos

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def productos(self) -> List[Producto]:
        return self.__productos

    def existe_producto(self, producto) -> bool:
        return producto in self.__productos

    def buscar_producto(self, nombre_producto: str) -> Producto:
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                return producto

        raise Exception(f"No existe el producto {nombre_producto}")

    def mostrar_productos(self):
        for producto in self.__productos:
            print(producto)

    def eliminar_producto(self, nombre_producto: str):
        producto: Producto = self.buscar_producto(nombre_producto)
        self.__productos.remove(producto)
        print("El producto fue removido exitosamente")

    def reabastecer_producto(self, producto: Producto, cantidad: int):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        producto.ajustar_stock(cantidad)
        print("Se ajustó el nuevo stock")

    def vender(self, carrito: Carrito):
        if carrito.esta_vacio:
            print("No hay productos en el carrito")
            return None

        print(f"El total de la compra es {carrito.total}")

    def exportar_productos(self, formato: Literal["csv", "json"] = "csv"):
        filename = f"listado_productos.{formato}"
        if formato == "csv":
            GestorArchivos.exportar_csv(self.__productos, filename)
        elif formato == "json":
            GestorArchivos.exportar_json(self.__productos, filename)

    def actualizar_precios(self, porcentaje: float):
        for producto in self.__productos:
            producto.actualizar_precio(porcentaje)

    def actualizar_precio_producto(self, producto: Producto, nuevo_precio: float):
        if producto in self.__productos:
            try:
                producto.precio = nuevo_precio
                print(f"El nuevo precio de {producto.nombre} es {nuevo_precio}")
            except ValueError:
                print(f"El nuevo precio no puede ser negativo")

    def nuevo_producto(self, nombre: str, precio: float, stock: int):
        nuevo_producto = Producto(nombre, precio, stock)
        if not self.existe_producto(nuevo_producto):
            self.__productos.append(nuevo_producto)
            print("El producto fue agregado correctamente")
        else:
            print("El producto ya está en la tienda")