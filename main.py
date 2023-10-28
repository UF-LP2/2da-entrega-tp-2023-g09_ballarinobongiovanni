
import random
from src.clases import Paciente
from clases import Medico
from src.clases import Hospital
import tkinter as tk

def main() -> None:
  """prueba dendnnndnnnndj"""
  hospital = Hospital("hospital") #tengo que pasarle info
  hospital.agregarmedico(medico_uno = Medico(dni= 45678910,horarioinicio=1,horariofin=5,presentismo=True))
  hospital.agregarmedico(medico_dos = Medico(dni=12345678, horarioinicio=9, horariofin=14, presentismo=True))
  hospital.agregarmedico(medico_tres = Medico(dni=98765432, horarioinicio=8, horariofin=12, presentismo=True))
  hospital.agregarmedico(medico_cuatro = Medico(dni=98123732, horarioinicio=7, horariofin=1, presentismo=True))
  hospital.agregarmedico(medico_cinco = Medico(dni=12345679, horarioinicio=10, horariofin=15, presentismo=True))
  hospital.pacientesarchivo()
  
  for i in range (24): #empieza en la hora 1 am y suma una hora por pasada 
    hospital.listado() #tendriamos que ver si los listamos dentro del for
    hospital.medicoshorario(i) #crea una lista de los medicos habilitados para ese horario
    ordenar=hospital.ordenar() #ordena con mergesort
    hospital.dyc(ordenar) #funcion dividir y conquistar
    hospital.finalizaciondehorario(i) #desocupa los medicos

  paciente = hospital.ordenar() 
  ventana = tk.Tk()
  etiqueta = tk.Label(ventana, text="Paciente: " + paciente, bg="white", fg="black", font=("Arial", 12), width=20, height=2, anchor="center")
  etiqueta.pack()
  ventana.mainloop()


if __name__ == "__main__":
  main()
