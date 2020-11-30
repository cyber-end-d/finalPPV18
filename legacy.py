class Cliente:
    def __init__(self, nombre_apellido, dni, tarjeta, efectivo, productos):
        self.nombre_apellido = nombre_apellido
        self.dni = dni
        self.tarjeta = Tarjeta()
        self.efectivo = Efectivo()
        self.productos = []
        self.preferencia = "tarjeta"

    def pagar(self, producto):
        if self.preferencia == "tarjeta":
            if self.tarjeta.limite_maximo - self.tarjeta.gastado > producto.precio:
                self.tarjeta.pagar(producto.precio)
            else:
                if self.efectivo.disponible > producto.precio:
                    self.efectivo.gastar(producto.precio)
        else:
            if self.efectivo.disponible > producto.precio:
                self.efectivo.gastar(producto.precio)
            else:
                if self.tarjeta.limite_maximo - self.tarjeta.gastado > producto.precio:
                    self.tarjeta.pagar(producto.precio)

    def comprar(self, producto):
        self.pagar(producto)
        self.productos.append(producto)


class Producto:
    def __init__(self, precio):
        self.precio = precio

class Efectivo:
    def __init__(self, disponible):
        self.disponible = disponible

    def gastar(self, plata):
        self.disponible -= plata


class Tarjeta(Efectivo):
    def __init__(self, limite_maximo, gastado):
        self.limite_maximo = limite_maximo
        self.gastado = gastado

    def pagar(self, plata):
        self.gastado += plata
