from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes

class ListaClientes:
	def __init__(self):
		self.rc = RepositorioClientes()
		self.lista = self.rc.get_all()

	def nuevo_cliente_corporativo(self, nombre_empresa, 
								   nombre_contacto,
								   telefono_contacto, telefono, mail):
		c = ClienteCorporativo(nombre_empresa, nombre_contacto,
								telefono_contacto, telefono, mail)
		c.id_cliente = self.rc.store(c)
		if c.id_cliente == 0:
			return None
		else:
			self.lista.append(c)
			return c

	def nuevo_cliente_particular(self, nombre, apellido, 
								   telefono, mail):
		c = ClienteParticular(nombre,apellido, telefono, mail)						
		c.id_cliente = self.rc.store(c)
		if c.id_cliente == 0:
			return None
		else:
			self.lista.append(c)
			return c	


