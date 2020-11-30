class Cliente:
	def __init__(self, nombre_apellido, dni, metodos_pago):
		self.nombre_apellido = nombre_apellido
		self.dni = dni
		self.billetera = metodos_pago
		self.productos = []

	def pagar(self, producto):
		for metodo in self.billetera:
			if metodo.alcanza(producto.precio):
				metodo.pagar(producto.precio)
				return True
		else:
			return False

	def comprar(self, producto):
		if self.pagar(producto):
			self.productos.append(producto)

class Producto:
	def __init__(self, precio):
		self.precio = precio

class MetodoPago:

	def __init__(self, disponible):
		self.disponible = disponible

class Tarjeta(MetodoPago):
	def __init__(self, disponible):
		super().__init__(disponible)
		self.saldo = 0.0

	def pagar(self, precio):
		if self.alcanza(precio):
			self.disponible -= precio
			self.saldo += precio
			return True
		else:
			return False

	def alcanza(self, precio):
		if self.saldo + precio <= self.disponible:
			return True
		else:
			return False

class Efectivo(MetodoPago):
	def __init__(self, disponible):
		super().__init__(disponible)

	def pagar(self, precio):
		if self.alcanza(precio):
			self.disponible -= precio
			return True
		else:
			return False

	def alcanza(self, precio):
		if precio <= self.disponible:
			return True
		else:
			return False

def main():
	cl = Cliente("Carlos Maceira", 32956544, [Efectivo(500), Tarjeta(1000)])
	prod = Producto(750)
	cl.comprar(prod)
	print(cl.productos)
	for mediopago in cl.billetera:
		print(mediopago.disponible)

if __name__ == '__main__':
	main()


