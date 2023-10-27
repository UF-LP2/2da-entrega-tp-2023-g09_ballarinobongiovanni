import random

def main() -> None:
  cant = 0 
  hora = 1
  minutospasados = 0
  valor = random.choice([True, False])
  medico = Medico(dni, horarioinicio, horariofin, presentismo) #tengo que pasarle info
  ordenar = ordenar()
  hospital = Hospital(nombre) #tengo que pasarle info
  
  for range in (24): #empieza en la hora 1 am y suma una hora por pasada 

    if (23 < hora and hora < 6): 
     cant = 1 #hay un enfermero disponible, igual al final si no tenemos enfermeros nose como podria ponerse en uso mas que esto
     minutospasados = hora

    if (6 < hora and hora < 10): 
      cant = 2 #hay dos enfermeros disponibles
      minutospasados = hora/2 #el tiempo que pasa dividido la cant. de enfermeros que pueden atender

    if (10 < hora and hora < 16): 
      cant = 5 
      minutospasados = hora/5

    if (16 < hora and hora < 23): 
      cant = 3 
      minutospasados = hora/3
  
    medico.set_presentismo(valor)
    hospital.pacientesarchivo()
    hospital.finalizaciondehorario(hora)
    hospital.agregarmedico(medico)
    hospital.listado()
    hospital.dyc(ordenar)


if __name__ == "__main__":
  main()
