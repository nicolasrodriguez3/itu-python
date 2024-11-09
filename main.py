from Manager import Manager

from tienda.tienda import Tienda
from tienda.carrito import Carrito


def main():
    tienda = Tienda("hola")
    carrito = Carrito()

    tienda.nuevo_producto("Coca-Cola", 2000, 15)
    tienda.nuevo_producto("Pepsi", 1800, 10)
    tienda.nuevo_producto("Fanta", 1500, 3)
    
    app = Manager(tienda=tienda, carrito=carrito)
    app.mainloop()


if __name__ == "__main__":
    main()
