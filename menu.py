import sys
import datetime
from repositorioClientes import RepositorioClientes
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from listaClientes import ListaClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
from listaTrabajos import ListaTrabajos
class Menu:
	"Muestra un menu para que se responda a las opciones"
	def __init__(self):
		self.lista_clientes = ListaClientes()
		self.repositoriocl = RepositorioClientes()
		self.lista = self.repositoriocl.get_all()
		self.repositoriotr = RepositorioTrabajos()
		self.LT = ListaTrabajos()
		self.opciones= {
			"1": self.mostrar_clientes,
			"2": self.nuevo_cliente,
			"3": self.modificar_cliente,
			"4": self.eliminar_cliente,
			"5": self.carga_trabajo,
			"6": self.modificar_trabajo,
			"7": self.mostrar_trabajos,
			"8": self.HistorialTrabajosCl,
			"0": self.salir
		}

	def mostrar_menu(self):
		print("""
Menu del sistema:
1. Mostrar todos los clientes
2. Ingreso de nuevo cliente
3. Modificacion de cliente
4. Eliminacion de cliente
5. Carga de nuevo trabajo
6. Modificar datos de un trabajo
7. Mostrar todos los trabajos
8. Informe
0. Salir
""")

	def ejecutar(self): 
		"Muestra el menu y responde a las opciones."
		while True:
			self.mostrar_menu()
			opcion = input("Ingresar una opcion: ")
			accion = self.opciones.get(opcion)
			if accion:
				accion()
			else:				
				print("{0} no es una opcion valida".format(opcion))

	#CLIENTE // Mostrar todos los clientes.
	def mostrar_clientes(self, lista = None):
		if lista == None:
			lista = self.repositoriocl.get_all()
		for cliente in lista:
			print(cliente)
			print("==========================")

	#CLIENTE // Ingreso de cliente.
	def nuevo_cliente(self):
		tipo = "A"
		while tipo not in ("C", "c", "P", "p"):
			tipo = input("Ingrese el tipo de cliente: C: Corporativo/ P:Particular")
		nombre = input("Ingrese el nombre:")
		if tipo in ("C", "c"):
			contacto = input("Ingrese el nombre del contacto: ")
			tc = input("Ingrese el telefono del contacto: ")
		else:
			apellido = input("Ingrese el apellido: ")
		tel = input("Ingrese el telefono: ")
		mail = input("Ingresa la direccion de email: ")
		if tipo in ("C", "c"):
			c = self.lista_clientes.nuevo_cliente_corporativo(nombre,
				contacto, tc, tel, mail)
		else:
			c = self.lista_clientes.nuevo_cliente_particular(nombre,
				apellido, tel, mail)
		if c is None:
			print("Error al cargar el cliente")
		else:
			print("Cliente cargado correctamente")

	#CLIENTE // Modificacion de cliente.	
	def modificar_cliente(self):
		tipo = "A"
		id_cliente = int(input("Ingrese el ID del cliente registrado: "))
		while tipo not in ("C", "c", "P", "p"):
			tipo = input("Ingrese el tipo de cliente: C: Corporativo/ P: Particular ")
		nombre = input("Ingrese el nombre: ")
		if tipo in ("C", "c"):
			contacto = input("Ingrese el nombre del contacto: ")
			tc = input("Ingrese el telefono del contacto: ")
		else:
			apellido = input("Ingrese el apellido: ")
		tel = input("Ingrese el telefono: ")
		mail = input("Ingresa la direccion de email: ")
		if tipo in ("C", "c"):
			cliente = ClienteCorporativo(nombre, contacto, tc, tel, mail, id_cliente)
			c = self.repositoriocl.update(cliente)
		else:
			cliente = ClienteParticular(nombre, apellido, tel, mail, id_cliente)
			c = self.repositoriocl.update(cliente)

		if c is None:
			print("Error al modificar el cliente")
		else:
			print("Cliente modificado correctamente")

	#CLIENTE // Suprimir un cliente.
	def eliminar_cliente(self):
		id_cliente = int(input("Ingrese el id del cliente"))
		c = self.repositoriocl.get_one(id_cliente)
		if c == None:
			print("El id del cliente no esta cargado en nuestra base de datos")	
		else:
			self.repositoriocl.delete(c)
			print("El cliente fue eliminado correctamente!")

	#TRABAJO // Carga de un nuevo trabajo.
	def carga_trabajo(self):
		id_cliente = int(input("Ingrese el id del cliente: "))
		rc = RepositorioClientes()
		cl = rc.get_one(id_cliente)
		fecha_ingreso = datetime.date.today()
		dia = int(input("Ingrese el dia: "))
		mes = int(input("Ingrese el mes: "))
		anio = int(input("Ingrese el anio: "))
		fecha_entrega_propuesta = datetime.date(anio, mes, dia)
		descripcion_trabajo = input("Ingrese una descripcion del trabajo a realizar: ")
		c = self.LT.nuevo_trabajo(cl, fecha_ingreso, fecha_entrega_propuesta, descripcion_trabajo)
		if c == None:
			print("Error, no puede cargarse el nuevo trabajo ")
		else:
			print("Trabajo cargado correctamente en la base de datos! ")

	#TRABAJO // Modificar datos de los trabajos cargados. // FechaING-PROP-REAL-DESC-ESTADO DEL TRABAJO.
	def modificar_trabajo(self):
		print("Al ingresar un ID de trabajo se tendran que modificar todos los datos, en caso de que quede un campo vacio se modificara de esa forma")
		id_trabajo = int(input("Ingrese el ID del trabajo: "))
		C = self.repositoriotr.get_one(id_trabajo)
		if C == None:
			print("No se encontro el trabajo")
		else:
			t = input("Si desea modificar la fecha de ingreso presione f, de lo contrario presione 0 para continuar: ")
			if t in ("f","F"):
				dia = int(input("Ingrese nuevamente el dia: "))
				mes = int(input("Ingrese nuevamente el mes: "))
				anio = int(input("Ingrese nuevamente el anio: "))
				print("Fecha modificada exitosamente! ")
				fechaingreso = datetime.date(anio, mes, dia)
			else:
				fechaingreso = C.fecha_ingreso
			t = input("Si desea modificar la fecha de entrega propuesta de un trabajo presione la tecla e, de lo contrario presione 0 para continuar: ")
			if t in ("e", "E"):
				dia = int(input("Ingrese nuevamente el dia: "))
				mes = int(input("Ingrese nuevamente el mes: "))
				anio = int(input("Ingrese nuevamente el anio: "))
				print("Fecha modificada exitosamente! ")
				fentregapropuesta = datetime.date(anio, mes, dia)
			else:
				fentregapropuesta = C.fecha_entrega_propuesta
				print("Ningun dato se ha modificado")
			t = input("Si desea modificar la fecha real de un trabajo presione la tecla r, de lo contrario presione 0 para continuar: ")
			if t in ("r", "R"):
				dia = int(input("Ingrese nuevamente el dia: "))
				mes = int(input("Ingrese nuevamente el mes: "))
				anio = int(input("Ingrese nuevamente el anio: "))
				print("Fecha modificada exitosamente! ")
				fentregareal = datetime.date(anio, mes, dia)
			else:
				fentregareal = C.fecha_entrega_real
				print("No se ha modificado la fecha! ")
			t = input("Si desea modificar la descripcion de un trabajo presione la tecla t, de lo contrario presione 0 para continuar: ")
			if t in ("t", "T"):
				t = input("Ingrese la nueva descripcion del trabajo: ")
				print("Se ha modificado el nombre del trabajo! ")
				descripcion = t
			else:
				C.descripcion = descripcion
				print("La descripcion del trabajo no ha podido modificarse")
			trabajo = self.LT.modificar_trabajo(fechaingreso, fentregapropuesta, fentregareal, descripcion, id_trabajo)
			self.repositoriocl.update(trabajo)
			self.LT.TrabajoL = self.repositoriotr.get_all()
			
	#TRABAJO // Mostrar todos los trabajos.
	def mostrar_trabajos(self, listat = None):
		if listat == None:
			listat =self.repositoriotr.get_all()
		for cliente in listat:
			print(cliente)
			print("============================")

	#INFORME // Despliega una lista con los trabajos cargados en cada cliente.
	def HistorialTrabajosCl(self):
		"Pide un ID y muestra una lista con los trabajos cargados en cada cliente"
		for i in self.repositoriocl.get_all_particulares():
			print("=====================================")
			print("ID cliente: ",i.id_cliente, "- Nombre: ", i.nombre)
			print("=====================================")
		for i in self.repositoriocl.get_all_corporativos():
			print("=====================================")
			print("ID cliente: ",i.id_cliente, "- Nombre: ", i.nombre_empresa)
		id = int(input("Ingrese el ID del cliente: "))
		C = self.repositoriotr.get_one(id)
		if C == None:
			print()
		else:
			print("=====================================")
			print(C)
			print("=====================================")
			for I in self.LT.TrabajoL:
				if I.cliente.id_cliente == id:
					print("========================================")
					print("ID trabajo: ", I.id_trabajo)
					print("Fecha de ingreso: ", I.fecha_ingreso)
					print("Fecha entrega propuesta: ", I.fecha_entrega_propuesta)
					print("Fecha entrega real: ", I.fecha_entrega_real)
					print("Descripcion: ", I.descripcion)
					print("Retirado: ", I.retirado)
					print("========================================")
				else:
					print("========================================")
					print("No se encontraron trabajos")
					print("========================================")		
		
	def salir(self):
		print("Gracias por utilizar el sistema.")
		sys.exit(0)

if __name__ == "__main__":
	m = Menu()
	m.ejecutar()
