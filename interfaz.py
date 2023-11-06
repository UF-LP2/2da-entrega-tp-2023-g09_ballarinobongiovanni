import tkinter as tk
from tkinter import *
from src.clases import Hospital
from src.clases import Medico
from src.clases import Paciente


hp=Hospital("hop")
app = Tk()
def simulacion():
  hospital = Hospital("hospital") #tengo que pasarle info
  """La cantidad de enfermeros dedicados varía. Uno cubre el turno nocturno (23 a 6), dos cubren
  la mañana (6 a 10), cinco la hora pico (10 a 16) y tres el resto del horario (16 a 23). """
  medico_uno = Medico(dni=45678910, horarioinicio=0, horariofin=72, presentismo=True)
  medico_dos = Medico(dni=12345678, horarioinicio=72, horariofin=120, presentismo=True)#mañana
  medico_tres = Medico(dni=98765432, horarioinicio=72, horariofin=120, presentismo=True)
  medico_cuatro = Medico(dni=98123732, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_cinco = Medico(dni=12345679, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_seis = Medico(dni=98765433, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_siete = Medico(dni=45678912, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_ocho = Medico(dni=12345680, horarioinicio=120, horariofin=192, presentismo=True)#hora pico
  medico_nueve = Medico(dni=98765434, horarioinicio=192, horariofin=276, presentismo=True)
  medico_diez = Medico(dni=45678913, horarioinicio=192, horariofin=276, presentismo=True)#tarde noche
  medico_once = Medico(dni=12345681, horarioinicio=192, horariofin=276, presentismo=True)
  medico_doce = Medico(dni=98765435, horarioinicio=276, horariofin=288, presentismo=True)
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
      hospital.listado() #si ingresan nuevos pacientes , es necesario listarlos
      hospital.ordenar() #ordena con mergesort

    hospital.medicoshorario(i) #crea una lista de los medicos habilitados para ese horario
    hospital.dyc() #funcion dividir y conquistar
    hospital.finalizaciondehorario(i) #desocupa los medicos
    hospital.aumentartiempodeespera()
    hospital.pacientefallecido()

  for j in hospital.listapaciente: #para comprobar si hubo alguno sin atender
    print(j)
  print ("termino el programa")

    
app.geometry('400x700')
app.configure(background="white")
app.title("Interfaz")
titulo_label = tk.Label(app, text="Sistema de Hospital",font=("Time new roman",20))
titulo_label.pack()
tk.Button(
    app,
    text = "Listar",
    font=("Courier",14),
    bg="dark sea green",
    fg="White",
    command=lambda:hp.listar()
).pack()
tk.Button(
    app,
    text = "Simulacion DyC",
    font =("Courier",14),
    bg="dark sea green",
    fg ="White",
    command=lambda:simulacion()
).pack()


"""label1=Label(ventana, text="Listar:")
label1.place(x=40, y=30)


bt1=Button(ventana, text="Listar", command=hp.listar())
bt1.place(x=60, y=80)"""

app.mainloop()