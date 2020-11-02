from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime



class ListaTrabajos:
	def __init__(self):
		self.RT = RepositorioTrabajos()
		self.TrabajoL = self.RT.get_all()

	def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
		#Recibe los datos de un trabajo, crea un nuevo trabajo y lo agrega a la lista Trabajos.
		T = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion,False)
		T.id_trabajo = self.RT.store(T)
		if T.id_trabajo == 0:
			print(T)
			return None
		else:
			self.TrabajoL.append(T)
			return T

	def BuscarPorID(self, id_trabajo):
		#Recibe un ID y retorna un trabajo.
		for T in self.TrabajoL:
			if T.id_trabajo == int(id_trabajo):
				return (T)
		print("El ID ingresado no coincide o pertenece con ningun trabajo asignado")
		return None

	def modificar_trabajo(self, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, id_trabajo):
		#Recibe un trabajo y modifica los datos.
		T = self.BuscarPorID(id_trabajo)
		if T:
			T.fecha_ingreso = fecha_ingreso
			T.fecha_entrega_propuesta = fecha_entrega_propuesta
			T.fecha_entrega_real = fecha_entrega_real
			T.descripcion = descripcion
			return self.RT.update(T)
		return None
		
		
