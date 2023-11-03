from src.clases import Paciente
from src.clases import Medico
from src.clases import Hospital

"""def lista_de_medicos():
    hp = Hospital("hospital")
    hp.agregarmedico(medico_uno = Medico(dni= 45678910,horarioinicio=1,horariofin=5,presentismo=True))
    hp.agregarmedico(medico_dos = Medico(dni=12345678, horarioinicio=9, horariofin=14, presentismo=False))
    hp.agregarmedico(medico_tres = Medico(dni=98765432, horarioinicio=8, horariofin=12, presentismo=True))
    hp.agregarmedico(medico_cuatro = Medico(dni=98123732, horarioinicio=7, horariofin=1, presentismo=True))
    hp.agregarmedico(medico_cinco = Medico(dni=12345679, horarioinicio=10, horariofin=15, presentismo=True))
    medico_seis = Medico(dni=98765433, horarioinicio=9, horariofin=13, presentismo=False)
    medico_siete = Medico(dni=45678912, horarioinicio=3, horariofin=7, presentismo=True)
    medico_ocho = Medico(dni=12345680, horarioinicio=11, horariofin=16, presentismo=False)
    medico_nueve = Medico(dni=98765434, horarioinicio=10, horariofin=14, presentismo=True)
    medico_diez = Medico(dni=45678913, horarioinicio=4, horariofin=8, presentismo=False)
    medico_once = Medico(dni=12345681, horarioinicio=12, horariofin=17, presentismo=True)
    medico_doce = Medico(dni=98765435, horarioinicio=11, horariofin=15, presentismo=False)
    medico_trece = Medico(dni=45678914, horarioinicio=5, horariofin=9, presentismo=True)
    medico_catorce = Medico(dni=12345682, horarioinicio=13, horariofin=18, presentismo=False)
    medico_quince = Medico(dni=98765436, horarioinicio=12, horariofin=16, presentismo=True)
    medico_dieciseis = Medico(dni=45678915, horarioinicio=6, horariofin=10, presentismo=False)
    medico_diecisiete = Medico(dni=12345683, horarioinicio=14, horariofin=19, presentismo=True)
    medico_dieciocho = Medico(dni=98765437, horarioinicio=13, horariofin=17, presentismo=False)
    medico_diecinueve = Medico(dni=45678916, horarioinicio=7, horariofin=11, presentismo=True)
    medico_veinte = Medico(dni=12345684, horarioinicio=15, horariofin=20, presentismo=False)
    """

def test_ordenar():
    hp = Hospital("hospital")
    p1 = Paciente(dni=4567839, tiempoespera=5, tiempoesperamax=10, enfermedad="Isquemia")
    p2 = Paciente(dni=4567895, tiempoespera=116, tiempoesperamax=120, enfermedad="Otalgias")
    p3 = Paciente(dni=4567867, tiempoespera=239, tiempoesperamax=240, enfermedad="no urgencia")
    
    hp.agregarpaciente(p2)
    hp.agregarpaciente(p1)
    hp.agregarpaciente(p3)  
    
    hp.ordenar()  
    
    assert (hp.listapaciente[0].tiempoespera, hp.listapaciente[0].tiempoesperamax, hp.listapaciente[0].enfermedad) == (p3.tiempoespera, p3.tiempoesperamax, p3.enfermedad)

def test_dyc():
    hp = Hospital("hospital")
    p1 = Paciente(dni=4567839, tiempoespera=5, tiempoesperamax=10, enfermedad="Isquemia")
    p2 = Paciente(dni=4567895, tiempoespera=116, tiempoesperamax=120, enfermedad="Otalgias")
    p3 = Paciente(dni=4567867, tiempoespera=239, tiempoesperamax=240, enfermedad="no urgencia")
    p4 = Paciente(dni = 123456789,tiempoespera= 0, tiempoesperamax=0,enfermedad= "Politraumatismo grave")
    medico_uno = Medico(dni= 45678910,horarioinicio=1,horariofin=10,presentismo=True)
    medico_dos = Medico(dni=12345678, horarioinicio=9, horariofin=14, presentismo=True)
    medico_tres = Medico(dni=98765432, horarioinicio=8, horariofin=12, presentismo=True)
   
    hp.agregarmedico(medico_uno )
    hp.agregarmedico(medico_dos )
    hp.agregarmedico(medico_tres)
   
    hp.agregarpaciente(p2)
    hp.agregarpaciente(p1)
    hp.agregarpaciente(p3)
    hp.agregarpaciente(p4)
   
    hp.medicoshorario(9)
    hp.listado()
    hp.ordenar()
    hp.dyc()

    assert(hp.listapaciente[0].dni) == (p1.dni)

def test_listado():
    hp = Hospital("hospital")
    p1 = Paciente(dni=4567839, tiempoespera=5, tiempoesperamax=10, enfermedad="Isquemia")
    p2 = Paciente(dni=4567895, tiempoespera=116, tiempoesperamax=120, enfermedad="Otalgias")
    p3 = Paciente(dni=4567867, tiempoespera=239, tiempoesperamax=240676767, enfermedad="no urgencia")
    p4 = Paciente(dni=123456789,tiempoespera=0, tiempoesperamax=0,enfermedad="Politraumatismo grave")
    hp.agregarpaciente(p2)
    hp.agregarpaciente(p1)
    hp.agregarpaciente(p3)
    hp.agregarpaciente(p4)

    hp.listado()

    assert(hp.listarojo[0].dni) == (p4.dni)
    assert(hp.listaazul[0].tiempoesperamax) == 240
   
def test_pacientesarchivo(tmp_path): #funcion de pytest que genera un directorio temporal
    hp = Hospital(nombre = "h")
    p = tmp_path / "sub" 
    p.mkdir() 
    test_csv = p / "Pacientes.csv" #crea un archivo csv
      
    with open(test_csv, "w") as file: #escribir el archivo
        file.write("dni,tiempoespera,tiempoesperamax,enfermedad\n")
        file.write("123456789, 0, 0, Politraumatismo grave\n")
        file.write("987654321, 8, 10, Coma\n")

    hp.pacientesarchivo()
    assert int(len(hp.listaarchivo)) > 0
    
def test_greedy():
    hp = Hospital("hospital")
    p1 = Paciente(dni=4567839, tiempoespera=5, tiempoesperamax=10, enfermedad="Isquemia")
    p2 = Paciente(dni=4567895, tiempoespera=116, tiempoesperamax=120, enfermedad="Otalgias")
    p3 = Paciente(dni=4567867, tiempoespera=239, tiempoesperamax=240, enfermedad="no urgencia")
    p4 = Paciente(dni = 123456789,tiempoespera= 0, tiempoesperamax=0,enfermedad= "Politraumatismo grave")
    p5= Paciente(dni = 891234567,tiempoespera=0, tiempoesperamax=12232323,enfermedad="Coma")
    p6 = Paciente(dni=912345678, tiempoespera=0, tiempoesperamax=10, enfermedad="Convulsiones")

    medico_uno = Medico(dni= 45678910,horarioinicio=1,horariofin=10,presentismo=True)
    medico_dos = Medico(dni=12345678, horarioinicio=9, horariofin=14, presentismo=True)
    medico_tres = Medico(dni=98765432, horarioinicio=8, horariofin=12, presentismo=True)
   
    hp.agregarmedico(medico_uno)
    hp.agregarmedico(medico_dos)
    hp.agregarmedico(medico_tres)
   
    hp.agregarpaciente(p2)
    hp.agregarpaciente(p1)
    hp.agregarpaciente(p3)
    hp.agregarpaciente(p4)
    hp.agregarpaciente(p5)
    hp.agregarpaciente(p6)

    hp.medicoshorario(9)
    hp.listado()
    hp.greedy()

    assert int(len(hp.listanaranja)) == 1
    assert int(len(hp.listarojo)) == 0
    
def test_aumentotiempo():
    hp = Hospital("hospital")
    p1 = Paciente(dni=4567839, tiempoespera=5, tiempoesperamax=10, enfermedad="Isquemia")
    p2 = Paciente(dni=4567895, tiempoespera=116, tiempoesperamax=120, enfermedad="Otalgias")
    p3 = Paciente(dni=4567867, tiempoespera=239, tiempoesperamax=240, enfermedad="no urgencia")
    hp.agregarpaciente(p2)
    hp.agregarpaciente(p1)
    hp.agregarpaciente(p3)
    hp.aumentartiempodeespera()

    assert p2.tiempoespera == 117
    assert p1.tiempoespera == 6
    assert p3.tiempoespera == 240
