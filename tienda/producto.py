class Producto:
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.__nombre: str = nombre
        self.__precio: float = precio
        self.__stock: int = stock

    def __str__(self) -> str:
        return (
            f"Nombre: {self.__nombre} \nPrecio: {self.__precio} \nStock: {self.__stock}"
        )

    # Getters
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> float:
        return self.__precio

    @property
    def stock(self) -> int:
        return self.__stock

    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("Debe ingresar un nombre")
        self.__nombre = nuevo_nombre

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.__precio = nuevo_precio

    @stock.setter
    def stock(self, cantidad: int):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__stock = cantidad

    # Métodos
    def vender(self, cantidad: int):
        if self.__stock < cantidad:
            raise ValueError("No hay suficiente stock")
        self.__stock -= cantidad

    def ajustar_stock(self, cantidad: int):
        self.__stock += cantidad

    def actualizar_precio(self, porcentaje: float):
        self.__precio += self.__precio * porcentaje
