import reproductor
import tkinter #Se crear la interface
import vlc #Se reproducira las cansiones
import eyed3
import os

def Buscar_En_Directorio(Diccionario): #Podemos ingresar Diccionario Artistas, DiccionarioCansiones,Diccionario Genero 
	#Ubicasion: /home/diegorcc/Escritorio/Reproductor

	directorio = nombreDirectorio.get() #Diccionarion tendra las cansiones encontradas en el directorio y subdirectorios
	
	lista = reproductor.Busqueda_Cansion_En_Directorio(directorio,".mp3") #Retorna lista con las ubicasiones de cansiones formato .mp3
	
	DirectorioActual.set(directorio) #Cambiamos el valor del texto en el nuevo directorio
	Diccionario.Ingresando_Cansiones_a_Diccionario(lista) #Ingresamos los titulos de cansiones al diccionario 

	Borrando_ListaBox_Cantante() #Borramos la lista de cantantes
	
	List = []

	reproductor.Retorna_Posibles_Convinaciones_de_Diccionario(Diccionario.head,'',List)
	Insertando_ListaBox_Cansines(List)

def Buscar_Cansion_Titulo(Diccionario,instanciamosObjeto,Reproductor): #Buscarenos la cansion dentro del diccionario
	
	Borrando_ListaBox_Cantante() #Borramos la lista de cantantes

	nombre_cansion = nombreCansion.get() # nombre contiene el valor del texto introducido en entrada_Cansion
	
	Nodo = Diccionario.head

	if nombre_cansion !='':
		Nodo = reproductor.Retorna_Cansion_o_Nodo_Sin_Cansion(Diccionario.head,nombre_cansion,0)
	
	if Nodo!=None :
		
		nombreCansionActual.set(nombre_cansion) #Cambiamos el valor de la cansion
		
		if Nodo.cansion != None:
				
			nombreCansion.set("") #Borramos el campo de busqueda YA QUE SE ENCONTRO LA CANSION
			
			Reproducir_Cansion(Nodo.cansion,instanciamosObjeto,Reproductor)		
		else:
			
			List = [] #Los valores de esta lista son los que se ingresan
			if nombre_cansion == '':
				reproductor.Retorna_Posibles_Convinaciones_de_Diccionario(Diccionario.head, nombre_cansion ,List)
			else:
				reproductor.Retorna_Posibles_Convinaciones_de_Diccionario(Nodo.hijo.head, nombre_cansion ,List)
			Insertando_ListaBox_Cansines(List)

def Reproducir_Cansion(ubicasion_cansion,instanciamosObjeto,Reproductor):
	Actualizar_Informacion_Cansion(ubicasion_cansion) #Nodo.cansion contiene la ubicasion de la cansion
	
	archivo_Reproducir = instanciamosObjeto.media_new(ubicasion_cansion)

	Reproductor.stop()
	Reproductor.set_media(archivo_Reproducir)
	Reproductor.play()

def Actualizar_Informacion_Cansion(ubicasion_cansion):
	Cansion_Cargada = eyed3.load(ubicasion_cansion)

	try: #Puede no tener titulo o artista
		minutos = int(Cansion_Cargada.info.time_secs/60)
		segundos = (Cansion_Cargada.info.time_secs - minutos*60)

		info_Duracion.set(str(minutos) + ':' + str(segundos)[0:3])
		
		info_Cansion.set(Cansion_Cargada.tag.title)
		info_Artista.set(Cansion_Cargada.tag.artist)
		info_Genero.set(Cansion_Cargada.tag.genre)
		
	except:
		titulo_cansion = ''
		for i in range(len(ubicasion_cansion)-1,1,-1):
			if ubicasion_cansion[i] == '/':
				break
			titulo_cansion = ubicasion_cansion[i] + titulo_cansion
		
		info_Cansion.set(titulo_cansion)
		info_Artista.set('Ninguna')
		info_Genero.set('Ninguna')	

#Reproductor Botones
#======================================>>>>>>>>>>>>>>>>>
def Boton_Play(Reproductor):
	Reproductor.play()
def Boton_Pause(Reproductor):
	Reproductor.pause()
def Boton_Stop(Reproductor):
	Reproductor.stop()
def Boton_Siguiente(Reproductor): #No terminado
	pass
#======================================>>>>>>>>>>>>>>>>>

#Boton de busqueda de cansiones en Directorio
#======================================>>>>>>>>>>>>>>>>
nombreDirectorio = tkinter.StringVar()
DirectorioActual = tkinter.StringVar() #Contendra el ultimo directorio de nombreDirectorio

Texto_Directorio = tkinter.Label(text = "Dir Music: ").place(x=30,y=9)
Texto_DirectorioVariable = tkinter.Label(textvariable = DirectorioActual).place(x=100,y=9)

entrada_Directorio = tkinter.Entry(ReproductorMP3,textvariable = nombreDirectorio,width=55).place(x=30,y=30)
bootonBuscarDirectorio = tkinter.Button(text = "Buscar",command = lambda: Buscar_En_Directorio(DiccionarioCansiones),width=10).place(x=480,y=26)
#======================================>>>>>>>>>>>>>>>>

#Solo sume 70 a cada campo de y para guardar distancia


#Boton de busqueda de cansion en Diccionario
#======================================>>>>>>>>>>>>>>>>
nombreCansion = tkinter.StringVar() #Objeto variable que contiene strings, tipo variable global
nombreCansionActual = tkinter.StringVar()

Texto_Usuario = tkinter.Label(text="Buscar Music: ").place(x=30,y=79) 
Texto_UsuarioVariable = tkinter.Label(textvariable = nombreCansionActual).place(x=120,y=79) #Texto


entrada_Cansion = tkinter.Entry(ReproductorMP3,textvariable = nombreCansion,width=55).place(x=30,y=100) #Campo de entrada de texto donde nombreCansion obtendra los valores

bootonBuscar = tkinter.Button(text = "Buscar",command = lambda: Buscar_Cansion_Titulo(DiccionarioCansiones,instanceReproductorVLC,reproductor_cansion),width=10).place(x=480,y=96)
#======================================>>>>>>>>>>>>>>>>

#Solo sume 70 a cada campo de y para guardar distancia


#Boton de play de cansion
posicionx = 35
posiciony = 150
#======================================>>>>>>>>>>>>>>>>
bootonPause = tkinter.Button(text = "Play",command = lambda:Boton_Play(reproductor_cansion),width=10).place(x=posicionx,y=posiciony)
#======================================>>>>>>>>>>>>>>>>


#Boton de pausa de cansion
#======================================>>>>>>>>>>>>>>>>
bootonPause = tkinter.Button(text = "Pausa",command = lambda:Boton_Pause(reproductor_cansion),width=10).place(x=posicionx + 110,y=posiciony)
#======================================>>>>>>>>>>>>>>>>


#Boton stop de cansion
#======================================>>>>>>>>>>>>>>>>
bootonPause = tkinter.Button(text = "Stop",command = lambda:Boton_Stop(reproductor_cansion),width=10).place(x=posicionx + 110*2,y=posiciony)
#======================================>>>>>>>>>>>>>>>>


#Boton siguiente de cansion
#======================================>>>>>>>>>>>>>>>>
bootonPause = tkinter.Button(text = " Sig >",command = lambda:Boton_Stop(reproductor_cansion),width=10).place(x=posicionx + 110*3,y=posiciony)
#======================================>>>>>>>>>>>>>>>>


#Boton de informaicion de cansion
#======================================>>>>>>>>>>>>>>>>
info_Cansion = tkinter.StringVar()
info_Artista = tkinter.StringVar()
info_Genero = tkinter.StringVar()
info_Duracion = tkinter.StringVar()

posicion_y = 200

textoCansion = tkinter.Label(text= "Titulo: ").place(x=30,y=posicion_y)
Campo_Cansion = tkinter.Label(textvariable = info_Cansion).place(x=110,y=posicion_y)

textoArtista = tkinter.Label(text= "Artista: ").place(x=30,y=posicion_y+30)
Campo_Artista = tkinter.Label(textvariable = info_Artista).place(x=110,y=posicion_y+30)

textoGenero = tkinter.Label(text= "Genero: ").place(x=30,y=posicion_y+2*30)
Campo_Genero = tkinter.Label(textvariable = info_Genero).place(x=110,y=posicion_y+2*30)

textoDuracion = tkinter.Label(text= "Duracion: ").place(x=30,y=posicion_y+3*30)
Campo_Duracion = tkinter.Label(textvariable = info_Duracion).place(x=110,y=posicion_y+3*30)

#Campo de ListaBox
#======================================>>>>>>>>>>>>>>>>
def Cansion_Seleccionada_ListBox(Diccionario,instanciamosObjeto,Reproductor):
	if len(Lista_de_Cansiones_Listabox.curselection()) != 0:
		nombre_cansion_de_ListBox = Lista_de_Cansiones_Listabox.get(Lista_de_Cansiones_Listabox.curselection())
		nombreCansion.set(nombre_cansion_de_ListBox) #Me retorna el nombre de la lista seleccionada en LIsBox
		
		Nodo_Cansion = reproductor.Retorna_Cansion_o_Nodo_Sin_Cansion(Diccionario.head,nombre_cansion_de_ListBox,0)
		
		Reproducir_Cansion(Nodo_Cansion.cansion,instanciamosObjeto,Reproductor)
		#EL curso dentro de la lista contiene algo
		#Debemos de hacer sonar la cansion seleccionada
#======================================>>>>>>>>>>>>>>>>
#======================================>>>>>>>>>>>>>>>>
def Artista_Seleccionado_Listabox():
	if len(Lista_de_Cansiones_Listabox.curselection()) != 0:
		pass
		#EL curso dentro de la lista contiene algo
		#Debemos de hacer sonar la cansion seleccionada
#======================================>>>>>>>>>>>>>>>>
#======================================>>>>>>>>>>>>>>>>
def Borrando_ListaBox_Cantante(): #Borramos todos los elementos de la lista
	Lista_de_Cansiones_Listabox.delete(0,tkinter.END)
#======================================>>>>>>>>>>>>>>>>
#======================================>>>>>>>>>>>>>>>>
def Insertando_ListaBox_Cansines(Lista):
	for i in range(len(Lista)):	
		Lista_de_Cansiones_Listabox.insert(i,Lista[i])
#======================================>>>>>>>>>>>>>>>>
#======================================>>>>>>>>>>>>>>>>
posicionyList_Box = 330

Lista_de_Cansiones_Listabox = tkinter.Listbox(ReproductorMP3,width = 27,height = 14)
Lista_de_Cansiones_Listabox.place(x=30,y=posicionyList_Box)

Lista_de_Artistas_Listabox = tkinter.Listbox(ReproductorMP3,width = 27,height = 14)
Lista_de_Artistas_Listabox.place(x=260,y=posicionyList_Box)
#======================================>>>>>>>>>>>>>>>>
#ListaBox Boton
#======================================>>>>>>>>>>>>>>>>
BotonSeleccionCansionListbox = tkinter.Button(text='Reproducir >',command = lambda : Cansion_Seleccionada_ListBox(DiccionarioCansiones,instanceReproductorVLC,reproductor_cansion)).place(x=82,y=587)
BotonSeleccionArtistaListbox = tkinter.Button(text='Selecciona >').place(x=310,y=587)
#======================================>>>>>>>>>>>>>>>>




ReproductorMP3 = tkinter.Tk()
ReproductorMP3.geometry('600x625')
ReproductorMP3.title("Reproductor_MP3")

DiccionarioCansiones = reproductor.Lista()

instanceReproductorVLC = vlc.Instance() #Instanciamos al objeto
reproductor_cansion = instanceReproductorVLC.media_player_new() #Instanciamos el reproductor vlc

ReproductorMP3.mainloop()
#Ubicasion: /media/diegorcc/DiegoCRR1/Musica