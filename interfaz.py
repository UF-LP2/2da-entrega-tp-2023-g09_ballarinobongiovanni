import tkinter as tk
from tkinter import *
from src.clases import Hospital
from src.clases import Medico
from src.clases import Paciente
from src.clases import Enfermero
from tkinter import scrolledtext
import csv

hp=Hospital("hop")
en=Enfermero("en")
app =tk.Tk()
def parchivo():
        with open("src/Pacientes.csv",'r') as file:
            reader = csv.DictReader(file) #crea un diccionario con el encabezado, es decir que permite recorrer cada lista y ser reconocida por su encabezado
            for row in reader: #almacenamos en cada variable el valor de cada columna
                Dni = row['dni']
                tiempoespe = int(row['tiempoespera'])
                tiempomax = int(row['tiempoesperamax'])
                enfermed = row ['enfermedad']

                pac = Paciente(Dni, tiempoespe, tiempomax, enfermed)
                hp.listapaciente.append(pac)


def simulacion():
  simulacionventana = tk.Toplevel(app)
  simulacionventana.title("Simulación de DyC")

  text_widget = scrolledtext.ScrolledText(simulacionventana, width=60, height=20)
  text_widget.pack(fill=tk.BOTH, expand=True)
  text_widget.tag_configure("rojo", foreground="red")

  hospital = Hospital("Hospital") #tengo que pasarle info
  """La cantidad de enfermeros dedicados varía. Uno cubre el turno nocturno (23 a 6), dos cubren
  la mañana (6 a 10), cinco la hora pico (10 a 16) y tres el resto del horario (16 a 23). """
  medico_uno = Medico(dni=1, horarioinicio=0, horariofin=72, presentismo=True)
  medico_dos = Medico(dni=2, horarioinicio=72, horariofin=120, presentismo=True)#mañana
  medico_tres = Medico(dni=3, horarioinicio=72, horariofin=120, presentismo=True)
  medico_cuatro = Medico(dni=4, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_cinco = Medico(dni=5, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_seis = Medico(dni=6, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_siete = Medico(dni=7, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_ocho = Medico(dni=8, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_nueve = Medico(dni=9, horarioinicio=192, horariofin=276, presentismo=True)
  medico_diez = Medico(dni=10, horarioinicio=192, horariofin=276, presentismo=True)#tarde noche
  medico_once = Medico(dni=11, horarioinicio=192, horariofin=276, presentismo=True)
  medico_doce = Medico(dni=12, horarioinicio=276, horariofin=288, presentismo=True)
  hospital.agregarmedico(medico_uno)
  hospital.agregarmedico(medico_dos)
  hospital.agregarmedico(medico_tres)
  hospital.agregarmedico(medico_cuatro)
  hospital.agregarmedico(medico_cinco)
  hospital.agregarmedico(medico_seis)
  hospital.agregarmedico(medico_siete)
  hospital.agregarmedico(medico_ocho)
  hospital.agregarmedico(medico_nueve)
  hospital.agregarmedico(medico_diez)
  hospital.agregarmedico(medico_once)
  hospital.agregarmedico(medico_doce)
  
  
  hospital.pacientesarchivo()
  for i in range (288): #cada iteracion son 5 min hora real
    listar = hospital.dearchivo_a_paciente(i)
    if listar == True:
      en.listado(hospital.listapaciente,hospital) #si ingresan nuevos pacientes , es necesario listarlos
      hospital.ordenar() #ordena con mergesort

    hospital.medicoshorario(i) #crea una lista de los medicos habilitados para ese horario
    hospital.dyc(i,text_widget) #funcion dividir y conquistar
    hospital.finalizaciondehorario() #desocupa los medicos
    hospital.aumentartiempodeespera()
    hospital.pacientefallecido(text_widget)

  for j in hospital.listapaciente: #para comprobar si hubo alguno sin atender
    print(j)
  print ("Termino el programa")

def listar():
        hp.pacientesarchivo()
        lista_como_cadena = "" #inicializo la cadena vacía
        i=1
        for paciente in hp.listaarchivo:
            detallepaciente = "{}.El Paciente con dni {} y con enfermedad {}".format(i, paciente.dni, paciente.enfermedad)
            lista_como_cadena += detallepaciente + "\n"  #agrego el detalle del paciente a la cadena con un salto de línea
            i+=1
        listar_window = tk.Toplevel(app)
        listar_window.title("Lista de Pacientes")

        listar_label = tk.Label(listar_window, text="Lista de pacientes:\n{}".format(lista_como_cadena), font=("Arial", 12), justify='left')
        listar_label.pack()

def colores():
   parchivo()
   en.listado(hp.listapaciente,hp)
   info_ventana = tk.Toplevel(app)
   info_ventana.title("Cantidad de Pacientes por Color")
   
   tk.Label(info_ventana, text="Cantidad de Rojos: {}".format(len(hp.listarojo)), font=("Arial", 12), fg="Red").pack(side=tk.LEFT)
   tk.Label(info_ventana, text="Cantidad de Naranjas: {}".format(len(hp.listanaranja)), font=("Arial", 12),fg="orange").pack(side=tk.LEFT)
   tk.Label(info_ventana, text="Cantidad de Amarillos: {}".format(len(hp.listaamarillo)), font=("Arial", 12),fg="Yellow").pack(side=tk.LEFT)
   tk.Label(info_ventana, text="Cantidad de Verdes: {}".format(len(hp.listaverde)), font=("Arial", 12),fg="green").pack(side=tk.LEFT)
   tk.Label(info_ventana, text="Cantidad de Azules: {}".format(len(hp.listaazul)), font=("Arial", 12),fg="Blue").pack(side=tk.LEFT)
   tk.Label(info_ventana, text="Total de Pacientes: {}".format(40), font=("Arial", 12), anchor='center').pack()
  
       
app.geometry('500x400')
app.configure(background="dark sea green")
app.title("Interfaz")
titulo_label = tk.Label(app, text="Sistema de Hospital", font=("Helvetica",20),bg= "dark sea green",fg="White")

titulo_label.pack()
tk.Button(
    app,
    text = "Listar",
    font=("Helvetica",14),
    bg="indian red",
    fg="White",
    command=lambda:listar()
).pack()
tk.Button(
    app,
    text = "Simulación DyC",
    font=("Helvetica",14),
    bg="indian red",
    fg="White",
    command=lambda:simulacion()
).pack()
tk.Button(
   app, 
   text="Mostrar Cantidad de Pacientes por Color", 
   font=("Helvetica", 14),
   bg="indian red",
   fg= "White",
   command=lambda:colores()
   ).pack()

"""label1=Label(ventana, text="Listar:")
label1.place(x=40, y=30)

bt1=Button(ventana, text="Listar", command=hp.listar())
bt1.place(x=60, y=80)"""

app.mainloop()