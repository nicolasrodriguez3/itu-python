from tienda.producto import Producto

class Carrito:
    def __init__(self) -> None:
        self.__productos = []
        
    @property
    def productos(self):
        return self.__productos

    def agregar(self, producto: Producto, cantidad: int = 1):
        # Buscar si el producto ya está en el carrito
        for i, (prod, qty) in enumerate(self.__productos):
            if prod == producto:
                self.__productos[i] = (prod, qty + cantidad)
                print(f"Se agregó {cantidad} {producto.nombre} al carrito")
                return

        # Si el producto no está en el carrito
        self.__productos.append((producto, cantidad))
        print(f"Se agregó {cantidad} {producto.nombre} al carrito")

    def mostrar(self):
        if not self.__productos:
            print("\nEl carrito está vacío.")
        else:
            print("\nCarrito de compras:")
            for producto, cantidad in self.__productos:
                print(
                    f"{producto.nombre} - Cantidad: {cantidad} - Precio total: {producto.precio * cantidad}"
                )

    def eliminar(self, producto: Producto, cantidad: int | None = None):
        for i, (prod, qty) in enumerate(self.__productos):
            if prod == producto:
                # Si no se especifica cantidad o la cantidad es mayor o igual, eliminamos el producto
                if not cantidad or cantidad >= qty:
                    self.__productos.pop(i)
                    print(f"Se eliminó {producto.nombre} del carrito")
                else:
                    self.__productos[i] = (prod, qty - cantidad)
                    print(f"Se eliminó {cantidad} {producto.nombre} del carrito")
                return
        print(f"{producto.nombre} no se encuentra en el carrito")

    def vaciar(self):
        self.__productos.clear()

    @property
    def esta_vacio(self) -> bool:
        return not self.__productos

    @property
    def total(self) -> float:
        return sum(
            producto.precio * cantidad for producto, cantidad in self.__productos
        )
