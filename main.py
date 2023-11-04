from src.clases import Paciente
from src.clases import Medico
from src.clases import Hospital

def main() -> None:
  hospital = Hospital("hospital") #tengo que pasarle info
  """La cantidad de enfermeros dedicados varía. Uno cubre el turno nocturno (23 a 6), dos cubren
  la mañana (6 a 10), cinco la hora pico (10 a 16) y tres el resto del horario (16 a 23). """
  medico_uno = Medico(dni=45678910, horarioinicio=0, horariofin=6, presentismo=True)
  medico_dos = Medico(dni=12345678, horarioinicio=6, horariofin=10, presentismo=True)#mañana
  medico_tres = Medico(dni=98765432, horarioinicio=6, horariofin=10, presentismo=True)
  medico_cuatro = Medico(dni=98123732, horarioinicio=10, horariofin=16, presentismo=True)#hora pico
  medico_cinco = Medico(dni=12345679, horarioinicio=10, horariofin=16, presentismo=True)#hora pico
  medico_seis = Medico(dni=98765433, horarioinicio=10, horariofin=16, presentismo=True)#hora pico
  medico_siete = Medico(dni=45678912, horarioinicio=10, horariofin=16, presentismo=True)#hora pico
  medico_ocho = Medico(dni=12345680, horarioinicio=10, horariofin=16, presentismo=True)#hora pico
  medico_nueve = Medico(dni=98765434, horarioinicio=16, horariofin=23, presentismo=True)
  medico_diez = Medico(dni=45678913, horarioinicio=16, horariofin=23, presentismo=True)#tarde noche
  medico_once = Medico(dni=12345681, horarioinicio=16, horariofin=23, presentismo=True)
  medico_doce = Medico(dni=98765435, horarioinicio=23, horariofin=24, presentismo=True)
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
  for i in range (24): #empieza en la hora 1 am y suma una hora por pasada 
    listar = hospital.dearchivo_a_paciente(i)
    if listar == True:
      hospital.listado() #tendriamos que ver si los listamos dentro del for
      hospital.ordenar() #ordena con mergesort

    hospital.medicoshorario(i) #crea una lista de los medicos habilitados para ese horario
    hospital.dyc() #funcion dividir y conquistar
    hospital.finalizaciondehorario(i) #desocupa los medicos
    #hospital.interfaz()
    hospital.aumentartiempodeespera()
    hospital.pacientefallecido()

  for j in hospital.listapaciente: #para comprobar si hubo alguno sin atender
    print(j)
  print ("termino el programa")


if __name__ == "__main__":
  main()
