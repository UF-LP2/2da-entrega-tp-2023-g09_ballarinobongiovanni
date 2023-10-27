from enum import Enum
import csv
class Paciente:
    class enfermedades(Enum):
         politraumatismo = "Politraumatismo grave"
         coma = "Coma"
         convulsion = "Convulsiones"
         hemorragia_dig = "Hemorragia digestiva"
         isquemia = "Isquemia"
         cefalea = "Cefalea brusca"
         paresia = "Paresia"
         hipertension = "Hipertensión arterial"
         vertigo = "Vértigo con afectación vegetativa"
         sincope = "Síncope"
         urgencia_psi = "Urgencias psiquiátricas"
         otalgias = "Otalgias"
         odontalgia = "Odontalgias"
         dolor_leve = "Dolores inespecíficos leves"
         traumatismos = "Traumatismos"
         esguinces = "Esguinces"
         no_urgencia = "no urgencia"

    def __init__(self, dni, tiempoespera, tiempoesperamax, enfermedad):
       
        
        self.enfermedad = enfermedad
        self.dni = dni
        self.tiempoespera = tiempoespera
        self.tiempoesperamax = tiempoesperamax

    def set_tiempoesperamaximo(self, tiempoesperamaximo):
        self.tiempoesperamax = tiempoesperamaximo
    def __lt__(self,other):
         return (self.tiempoesperamax - self.tiempoespera ) < (other.tiempoesperamax - other.tiempoespera)
  
   
         
class Medico:
    def __init__(self, dni, horarioinicio, horariofin, presentismo):
        self.dni = dni
        self.horarioinicio = horarioinicio
        self.horariofin = horariofin
        self.presentismo = presentismo #si esta habilitado para atender o esta ocupado

    def atender(self, paciente):
        print("faltaponeralgo")
        self.presentismo = False

    def set_presentismo(self,valor):
        self.presentismo=valor

class Hospital:
    def __init__(self, nombre):
        self.listapaciente = []
        self.listamedicos = []
        self.listarojo = []
        self.listanaranja = []
        self.listaamarillo = []
        self.listaverde = []
        self.listaazul = []
        self.listamedicoshab = []
        self.nombre = nombre
    
    def pacientesarchivo(self):
        with open("src/Pacientes.csv",'r') as file:
            reader=csv.DictReader(file) #crea un diccionario con el encabezado, es decir que permite recorrer cada lista y ser reconocida por su encabezado
            for row in reader: #almacenamos en cada variable el valor de cada columna
                Dni= row['dni']
                tiempoespe = row['tiempoespera']
                tiempomax = row['tiempoesperamax']
                enfermed = row ['enfermedad']

                pac = Paciente(Dni, tiempoespe, tiempomax, enfermed)
                self.agregarpaciente(pac)

    def medicoshorario(self, horaactual): #retorna una lista
        

        for medico in self.listamedicos:
            if medico.horarioinicio <= horaactual and medico.horariofin >= horaactual:
                self.listamedicoshab.append(medico)

       
   
    def finalizaciondehorario(self,horaactual): #cuando termina la hora queda habilitado el medico para recibir otro paciente

        for medico in self.listamedicoshab:
            if medico.presentismo == False:
                medico.set_presentismo(True)
   
    def agregarpaciente(self, paciente):
        self.listapaciente.append(paciente)

    def agregarmedico(self, medico):
        self.listamedicos.append(medico)

    def listado(self):
           
            for paciente in self.listapaciente:
                if paciente.enfermedad in (Paciente.enfermedades.politraumatismo, Paciente.enfermedades.coma):
                    self.listarojo.append(paciente)
                    self.listapaciente.pop(paciente)
                elif paciente.enfermedad in (Paciente.enfermedades.convulsion, Paciente.enfermedades.hemorragia_dig,Paciente.enfermedades.isquemia):
                    self.listanaranja.append(paciente)
                    paciente.set_tiempoesperamaximo(10)
                    #nose si directamente se puede poner paciente.tiempoesperamax = 20 o tengo que hacer set
                elif paciente.enfermedad in (Paciente.enfermedades.cefalea, Paciente.enfermedades.paresia,
                                             Paciente.enfermedades.hipertension,Paciente.enfermedades.vertigo,Paciente.enfermedades.sincope, Paciente.enfermedades.urgencia_psi):
                    self.listaamarillo.append(paciente)
                    paciente.set_tiempoesperamaximo(60)
                elif paciente.enfermedad in (Paciente.enfermedades.otalgias, Paciente.enfermedades.odontalgia,
                                             Paciente.enfermedades.dolor_leve, Paciente.enfermedades.traumatismos,Paciente.enfermedades.esguinces):
                    self.listaverde.append(paciente)
                    paciente.set_tiempoesperamaximo(120)
                else:
                    self.listaazul.append(paciente)
                    paciente.set_tiempoesperamaximo(240)

    def ordenar(self): #en esta función se está ordenando la cola de pacientes en función de la diferencia entre el tiempo de espera y el tiempo máximo de espera, según el método de mergesort
       elprimero= merge_sort(self.listapaciente)
       return elprimero
       """ if len(self.listapaciente) > 1:
            medio = int(len(self.listapaciente) / 2)
            izq = self.listapaciente[:medio]
            der = self.listapaciente[medio:]
            self.ordenar(izq)
            self.ordenar(der)

            i = j = k = 0
            while i < len(izq) and j < len(der):
                if (izq[i].tiempoespera - izq[i].tiempoesperamax) < (der[j].tiempoespera - der[j].tiempomaxespera):
                    self.listapaciente[k] = izq[i]
                    i += 1
                else:
                    self.listapaciente[k] = der[j]
                    j += 1
            k += 1
            while i < len(izq):
                self.listapaciente[k] = izq[i]
                i += 1
                k += 1

            while j < len(der):
                self.listapaciente[k] = der[j]
                j += 1
                k += 1
            
        return self.listapaciente[0]"""
       
       

    def dyc(self, ordenar): #recibe la lista completa sin los rojos, y llama el ordenar
        j = 0               #si ponemos los pacientes en hp. listapaciente, hay que sacar la variable

        for j in self.listamedicoshab :
            if j.presentismo != False:
                if self.listarojo != None:
                    j.atender(self.listarojo[0])
                    self.listarojo = self.listarojo[1:]
                else:
                    
                    j.atender(ordenar)
                    listaespera = listaespera[1:]
def merge_sort(lista_pacientes):
    if int (len(lista_pacientes)) > 1:
        medio = int(len(lista_pacientes) / 2)
        izq = lista_pacientes[:medio]
        der = lista_pacientes[medio:]
        merge_sort(izq)
        merge_sort(der)

        i = j = k = 0
        while i < len(izq) and j < len(der):
            if izq[i]  < der[j] :
                lista_pacientes[k] = izq[i]
                i += 1
            else:
                lista_pacientes[k] = der[j]
                j += 1
            k += 1
        while i < len(izq):
            lista_pacientes[k] = izq[i]
            i += 1
            k += 1
        while j < len(der):
            lista_pacientes[k] = der[j]
            j += 1
            k += 1
    return lista_pacientes[0]
"""
    def greedy(self, horaactual): #recibe la hora del for 
        j = 0

        for j in (self.medicoshorario(horaactual)):
            if j.capacidad != False:
                if self.listarojo != None:
                    j.atender(self.listarojo[0])
                    self.listarojo = self.listarojo[1:] #por ahi hay que hacerlo con get y set

                if self.listanaranja != None:
                    j.atender(self.listanaranja[0])
                    self.listanaranja = self.listanaranja[1:]

                if self.listaamarillo != None:
                    j.atender(self.listaamarillo[0])
                    self.listaamarillo = self.listaamarillo[1:]
                
                if self.listaverde != None:
                    j.atender(self.listaverde[0])
                    self.listaverde = self.listaverde[1:]

                if self.listaazul != None:
                    j.atender(self.listaazul[0])
                    self.listanaazul = self.listanaazul[1:]
                 
"""

