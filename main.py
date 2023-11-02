import random
from src.clases import Paciente
from src.clases import Medico
from src.clases import Hospital

def main() -> None:
  hospital = Hospital("hospital") #tengo que pasarle info
  medico_uno = Medico(dni= 45678910,horarioinicio=1,horariofin=5,presentismo=True)
  medico_dos = Medico(dni=12345678, horarioinicio=9, horariofin=14, presentismo=True)
  medico_tres = Medico(dni=98765432, horarioinicio=8, horariofin=12, presentismo=True)
  medico_cuatro = Medico(dni=98123732, horarioinicio=7, horariofin=1, presentismo=True)
  medico_cinco = Medico(dni=12345679, horarioinicio=10, horariofin=15, presentismo=True)
  hospital.agregarmedico(medico_uno)
  hospital.agregarmedico(medico_dos)
  hospital.agregarmedico(medico_tres)
  hospital.agregarmedico(medico_cuatro )
  hospital.agregarmedico(medico_cinco)
  hospital.pacientesarchivo()
  
  for i in range (24): #empieza en la hora 1 am y suma una hora por pasada 
    hospital.listado() #tendriamos que ver si los listamos dentro del for
    hospital.medicoshorario(i) #crea una lista de los medicos habilitados para ese horario
    hospital.ordenar() #ordena con mergesort
    hospital.dyc() #funcion dividir y conquistar
    hospital.finalizaciondehorario(i) #desocupa los medicos
    #hospital.interfaz()
    hospital.aumentartiempodeespera()
  
  


if __name__ == "__main__":
  main()
