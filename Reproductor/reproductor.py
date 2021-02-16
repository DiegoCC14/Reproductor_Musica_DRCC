import eyed3 #Se buscara los metadatos de las cansiones, titulo, artista, genero
import os #Capturamos las ubicasiones de todas las cansiones .mp3 para luego reproducir
import time #Para que las cansiones se reproduscan
import vlc #Se reproducira las cansiones

class Node():
	def __init__(self,letra_Almacenar):
		self.letra = letra_Almacenar
		self.cansion = None
		self.hijo = Lista()
		self.nextNode = None

class Lista(): #Usaremos estructura de diccionario
	#SOLO CONTENDRA CANSIONES 
	head = None
	def Suma_Lista(self,Cansion,La_Cadena_Almacenar,Contador):
		
		currentNode = self.head
		currentNodeAnterior = self.head

		while currentNode != None and ord(currentNode.letra) <= ord(La_Cadena_Almacenar[Contador]):
			if currentNode.letra == La_Cadena_Almacenar[Contador]:
				if Contador+1 == len(La_Cadena_Almacenar):
					currentNode.cansion = Cansion
					return()
				return(currentNode.hijo.Suma_Lista(Cansion,La_Cadena_Almacenar,Contador+1))
			
			currentNodeAnterior = currentNode
			currentNode = currentNode.nextNode
		
		nodo = Node(La_Cadena_Almacenar[Contador])
		
		if currentNode == currentNodeAnterior:
			nodo.nextNode = self.head
			self.head = nodo
		else:
			currentNodeAnterior.nextNode = nodo
			nodo.nextNode = currentNode

		if Contador+1 != len(La_Cadena_Almacenar):
			return(nodo.hijo.Suma_Lista(Cansion,La_Cadena_Almacenar,Contador+1))
		nodo.cansion = Cansion
		return()

	def Ver_Diccionario(self):
		currentNode = self.head
		while currentNode != None:
			print(currentNode.letra)
			if currentNode.cansion !=None:
				print(currentNode.cansion,"Fin letra")
			currentNode.hijo.Ver_Diccionario()
			currentNode = currentNode.nextNode

	#Posible a quitar
	#Posible a quitar
	#Posible a quitar
	def Retorna_Cansion(self,titulo_a_buscar,Contador):
		currentNode = self.head
		while currentNode != None and ord(currentNode.letra) <= ord(titulo_a_buscar[Contador]):
		
			if currentNode.letra == titulo_a_buscar[Contador]:
				if Contador+1 == len(titulo_a_buscar): #Tendria que encontrarse la cansion, sino sera None
					return(currentNode.cansion)
				return(currentNode.hijo.Retorna_Cansion(titulo_a_buscar,Contador+1))

			currentNode = currentNode.nextNode

		return(None)#No encontro el archivo

	def Ingresando_Cansiones_a_Diccionario(self,listaUbicasiones):
		for ubicasion_cansion_de_lista in listaUbicasiones:
			try: #Puede ocurrir que no tenga titulo, error 
				cansion = eyed3.load(ubicasion_cansion_de_lista)
				titulo_cansion = cansion.tag.title #Tomamos el titulo de la cansion y lo guardanos en el diccionario
				self.Suma_Lista(ubicasion_cansion_de_lista,titulo_cansion,0) #cuardamos la ubicasion de la cansion en el findepalabra
			except :
				titulo_cansion = ''
				for i in range(len(ubicasion_cansion_de_lista)-1,1,-1):
					if ubicasion_cansion_de_lista[i] == '/':
						break
					titulo_cansion = ubicasion_cansion_de_lista[i] + titulo_cansion
				
				print('cansion no encontrada: ',ubicasion_cansion_de_lista)

				self.Suma_Lista(ubicasion_cansion_de_lista,titulo_cansion,0)

'''
-----------------------------------
-----------------------------------
-----------------------------------

'''

class Node_Listas(): #Este Nodo contendra dentro de cansion, una lista de ubicasiones de cansiones
	def __init__(self,letra_Almacenar):
		self.letra = letra_Almacenar
		self.cansion = [] #Contiene una lista de cansiones en orden alfabetico
		self.hijo = Diccionario_Listas()
		self.nextNode = None

class Diccionario_Listas():
	#Lo usaremos para la lista de Artistas y Generos, estas contienen por cada Artista, varias cansiones la igual que generos
	head = None
	
	def Suma_Lista(self,Cansion,La_Cadena_Almacenar,Contador):
		
		currentNode = self.head
		currentNodeAnterior = self.head
		
		while currentNode != None and ord(currentNode.letra) <= ord(La_Cadena_Almacenar[Contador]):
			

			if currentNode.letra == La_Cadena_Almacenar[Contador]:
				if Contador+1 == len(La_Cadena_Almacenar):
					currentNode.cansion.append(Cansion) #Se trata de una lista normal [] donde almacenamos la ubicasion de las cansiones
					return()
				return(currentNode.hijo.Suma_Lista(Cansion,La_Cadena_Almacenar,Contador+1))
			
			currentNodeAnterior = currentNode
			currentNode = currentNode.nextNode
		
		nodo = Node_Listas(La_Cadena_Almacenar[Contador])
		
		if currentNode == currentNodeAnterior:
			nodo.nextNode = self.head
			self.head = nodo
		else:
			currentNodeAnterior.nextNode = nodo
			nodo.nextNode = currentNode

		if Contador+1 != len(La_Cadena_Almacenar):
			return(nodo.hijo.Suma_Lista(Cansion,La_Cadena_Almacenar,Contador+1))
		nodo.cansion.append(Cansion)
		return()

	def Ingresando_Artistas_a_Diccionario(self,listaUbicasiones):
		for ubicasion_cansion_de_lista in listaUbicasiones:
			try:
				cansion = eyed3.load(ubicasion_cansion_de_lista)  
				artista_cansion = cansion.tag.artist #Tomamos el artista de la cansion y lo guardanos en el diccionario
				self.Suma_Lista(ubicasion_cansion_de_lista,artista_cansion,0)	
			except: 
				print('Artista Desconocido')
				self.Suma_Lista(ubicasion_cansion_de_lista,'Desconocido',0) #cuardamos la ubicasion de la cansion en el findepalabra

	def Ver_Diccionario(self):
		currentNode = self.head

		while currentNode != None:
			print(currentNode.letra)
			if currentNode.cansion != []:
				print('Lista: ',currentNode.cansion)
			currentNode.hijo.Ver_Diccionario()
			currentNode = currentNode.nextNode


'''
def Reproducir_Cansion(instance,Ubicasion_cansion):

	#duracion_Cansion = eyed3.load(Ubicasion_cansion).info.time_secs #Necesito la duracion de la cansion para poder verla
	
	reproductor_cansion = instance.media_player_new()
	archivo_Reproducir = instance.media_new(Ubicasion_cansion)

	#reproductor_cansion.stop()
	
	reproductor_cansion.set_media(archivo_Reproducir)
	reproductor_cansion.play()
	time.sleep(50)
	return(reproductor_cansion)
'''

def Busqueda_Cansion_En_Directorio(Mi_Ubicasion,extencion_Archivo): #Retorna ubicasion de archivos con extencion .extencion_Archivo
	
	Lista_Ficheros = os.listdir(Mi_Ubicasion) #Buscamos todos los ficheros de la direccion actual

	#Debo de poner la direccion de la carpeta completa, plis, sino no los ve como carpetas,plis * 2
	Lista_Carpetas = list(filter(lambda ficheros: os.path.isdir(Mi_Ubicasion +'/'+ficheros) , Lista_Ficheros )) #genera lista solo con carpetas, 
	
	Lista_Cansiones = list(filter(lambda fichero: fichero.endswith( extencion_Archivo ), Lista_Ficheros )) # Solo toma los archivos con extencion extencion_Archivo
	Lista_Cansiones = list(map(lambda fichero: Mi_Ubicasion + '/' + fichero , Lista_Cansiones)) #Le anadimos la ubicasion de la cansion

	if Lista_Carpetas != []:
		for Carpeta in Lista_Carpetas:
			Lista_Cansiones = Lista_Cansiones + Busqueda_Cansion_En_Directorio(Mi_Ubicasion + '/' + Carpeta,extencion_Archivo)
			
	return(Lista_Cansiones) 

#Podra ser usado desde el diccionario Artisca como Cansines
#Como el objeto Lista se pasa por referencia solo le anadimos las cadenas
def Retorna_Posibles_Convinaciones_de_Diccionario(NodoActual,CadenaParaConcatenarLetras,Lista): #El Nodo Actual es por donde se empiesa a buscar las posibles soluciones
	#Ingresamos un nodo y este dara las posibles soluciones del diccionario
	#Retorna Lista con las soluciones
	if NodoActual != None:

		currentNode = NodoActual #Por costumbre 

		while currentNode != None:
			if NodoActual.cansion != None:
				Lista.append(CadenaParaConcatenarLetras+currentNode.letra) #Concatenamos y retornamos

			Retorna_Posibles_Convinaciones_de_Diccionario(currentNode.hijo.head,CadenaParaConcatenarLetras+currentNode.letra,Lista) #Ingresamos a ver si hay algo mas
			
			currentNode = currentNode.nextNode
	return()
#Buscamos dentro del diccionario una secuencia de paalabras, y retornamos el nodo o nada
def Retorna_Cansion_o_Nodo_Sin_Cansion(NodoActual,titulo_a_buscar,Contador):
		
		currentNode = NodoActual
		while currentNode != None and ord(currentNode.letra) <= ord(titulo_a_buscar[Contador]):
		
			if currentNode.letra == titulo_a_buscar[Contador]:

				if Contador+1 == len(titulo_a_buscar): #Tendria que encontrarse la cansion, sino sera None

					return(currentNode) #Retornamos el nodo sin importar si se encuentra la cansion dentro
				
				return(Retorna_Cansion_o_Nodo_Sin_Cansion(currentNode.hijo.head,titulo_a_buscar,Contador+1))

			currentNode = currentNode.nextNode

		return(None)#No encontro el archivo

#--------------------------------------------------->>>>>>>>>>>>>>>>>>
#--------------------------------------------------->>>>>>>>>>>>>>>>>>
#--------------------------------------------------->>>>>>>>>>>>>>>>>>
#--------------------------------------------------->>>>>>>>>>>>>>>>>>
#--------------------------------------------------->>>>>>>>>>>>>>>>>>
#Reproducir_Cansion(vlc.Instance(),'/media/diegorcc/DiegoCRR1/Musica/The Weeknd - Blinding Lights.mp3')
instance = vlc.Instance()
reproductor_cansion = instance.media_player_new()
archivo_Reproducir = instance.media_new('/media/diegorcc/DiegoCRR1/Musica/The Weeknd - Blinding Lights.mp3')

#reproductor_cansion.stop()

reproductor_cansion.set_media(archivo_Reproducir)
reproductor_cansion.play()
time.sleep(15)