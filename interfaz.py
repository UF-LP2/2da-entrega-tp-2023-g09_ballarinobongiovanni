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
def estadisticapac():
  estadisticas_window = tk.Toplevel(app)
  estadisticas_window.title("Estadísticas de Pacientes")

    # Crear etiquetas para mostrar las estadísticas
  label_rojo = tk.Label(estadisticas_window, text="Rojo:",fg="red")
  label_rojo_count = tk.Label(estadisticas_window, textvariable=count_rojo)

  label_naranja = tk.Label(estadisticas_window, text="Naranja:",fg="orange")
  label_naranja_count = tk.Label(estadisticas_window, textvariable=count_naranja)

  label_amarillo = tk.Label(estadisticas_window, text="Amarillo:",fg="yellow")
  label_amarillo_count = tk.Label(estadisticas_window, textvariable=count_amarillo)

  label_verde = tk.Label(estadisticas_window, text="Verde:",fg="green")
  label_verde_count = tk.Label(estadisticas_window, textvariable=count_verde)

  label_azul = tk.Label(estadisticas_window, text="Azul:",fg="blue")
  label_azul_count = tk.Label(estadisticas_window, textvariable=count_azul)

    # Diseñar la disposición de la ventana de estadísticas
  label_rojo.grid(row=0, column=0)
  label_rojo_count.grid(row=0, column=1)

  label_naranja.grid(row=1,column=0)
  label_naranja_count.grid(row=1, column=1)

  label_amarillo.grid(row=2, column=0)
  label_amarillo_count.grid(row=2, column=1)

  label_verde.grid(row=3, column=0)
  label_verde_count.grid(row=3, column=1)

  label_azul.grid(row=4, column=0)
  label_azul_count.grid(row=4, column=1)
  hospital = Hospital("Hospital") #tengo que pasarle info
  
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
      listado(hospital.listapaciente,hospital)

count_rojo = tk.IntVar()
count_naranja = tk.IntVar()
count_amarillo = tk.IntVar()
count_verde = tk.IntVar()
count_azul = tk.IntVar()


# Función que realiza la estadística de pacientes y actualiza la interfaz
def listado(listapaciente, hospital):
    global count_rojo, count_naranja, count_amarillo, count_verde, count_azul  # Debes declarar las variables como globales para modificarlas dentro de la función
    count_rojo.set(0)
    count_naranja.set(0)
    count_amarillo.set(0)
    count_verde.set(0)
    count_azul.set(0)

    for paciente in listapaciente:
        if paciente.enfermedad in (Paciente.enfermedades.politraumatismo.value, Paciente.enfermedades.coma.value):
            hospital.listarojo.append(paciente)
            count_rojo.set(count_rojo.get() + 1)
        elif paciente.enfermedad in (Paciente.enfermedades.convulsion.value, Paciente.enfermedades.hemorragia_dig.value, Paciente.enfermedades.isquemia.value):
            hospital.listanaranja.append(paciente)
            paciente.set_tiempoesperamaximo(10)
            count_naranja.set(count_naranja.get() + 1)
        elif paciente.enfermedad in (Paciente.enfermedades.cefalea.value, Paciente.enfermedades.paresia.value,
                                     Paciente.enfermedades.hipertension.value, Paciente.enfermedades.vertigo.value, Paciente.enfermedades.sincope.value, Paciente.enfermedades.urgencia_psi.value):
            hospital.listaamarillo.append(paciente)
            paciente.set_tiempoesperamaximo(60)
            count_amarillo.set(count_amarillo.get() + 1)
        elif paciente.enfermedad in (Paciente.enfermedades.otalgias.value, Paciente.enfermedades.odontalgia.value,
                                     Paciente.enfermedades.dolor_leve.value, Paciente.enfermedades.traumatismos.value, Paciente.enfermedades.esguinces.value):
            hospital.listaverde.append(paciente)
            paciente.set_tiempoesperamaximo(120)
            count_verde.set(count_verde.get() + 1)
        else:
            hospital.listaazul.append(paciente)
            paciente.set_tiempoesperamaximo(240)
            count_azul.set(count_azul.get() + 1)

   
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
    text="Actualizar Estadísticas",
    font=("Helvetica", 14),
    bg="indian red",
    fg="White",
    command=lambda: estadisticapac()
).pack()


app.mainloop()