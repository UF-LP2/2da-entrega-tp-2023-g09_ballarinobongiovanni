import tkinter as tk
from tkinter import *


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
         hipertension = "Hipertension arterial"
         vertigo = "Vertigo con afectacion vegetativa"
         sincope = "Sincope"
         urgencia_psi = "Urgencias psiquiatricas"
         otalgias = "Otalgias"
         odontalgia = "Odontalgias"
         dolor_leve = "Dolores inespecificos leves"
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

    def __lt__(self,other): #sobrecarga del < , retorna true o false
         return (self.tiempoesperamax - self.tiempoespera ) < (other.tiempoesperamax - other.tiempoespera)

    def set_tiempoespera(self,tiempoespera):
        self.tiempoespera = tiempoespera

    def get_tiempoespera(self):
        return self.tiempoespera
         
class Medico:
    def __init__(self, dni, horarioinicio, horariofin, presentismo):
        self.dni = dni
        self.horarioinicio = horarioinicio
        self.horariofin = horariofin
        self.presentismo = presentismo #si esta habilitado para atender o esta ocupado

    def atender(self, valor):
        self.presentismo = valor

    def set_presentismo(self,valor):
        self.presentismo = valor

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
        self.listaarchivo = []
        self.nombre = nombre


    def listar(self):
        self.pacientesarchivo()
        lista_como_cadena = ""  #inicializo la cadena vacía
        i=1
        for paciente in self.listaarchivo:

            detallepaciente = "{}.El Paciente {} con enfermedad {}".format(i,paciente.dni, paciente.enfermedad)
            lista_como_cadena += detallepaciente + "\n"  #agrego el detalle del paciente a la cadena con un salto de línea
            i+=1
        
        lista_label = tk.Label(text="Lista de pacientes:\n{}".format(lista_como_cadena), font=("time new roman", 8),justify='left')
        
        lista_label.pack(fill=tk.BOTH, expand=True)
    def pacientesarchivo(self):
        with open("src/Pacientes.csv",'r') as file:
            reader = csv.DictReader(file) #crea un diccionario con el encabezado, es decir que permite recorrer cada lista y ser reconocida por su encabezado
            for row in reader: #almacenamos en cada variable el valor de cada columna
                Dni = row['dni']
                tiempoespe = int(row['tiempoespera'])
                tiempomax = int(row['tiempoesperamax'])
                enfermed = row ['enfermedad']

                pac = Paciente(Dni, tiempoespe, tiempomax, enfermed)
                self.listaarchivo.append(pac)
                #self.print_file() esto seria solo si queres agregar un paciente nuevo

    def print_file(self): 
        with open("src/Pacientes.csv") as file: 
            writer = csv.writer(file) 
            for row in writer: 
                writer.writerow(row)

                dni = int(input("Ingrese el dni del paciente: "))
                tiempoespera = int(input("Ingrese el tiempo del paciente: "))
                tiempomax = int(input("Ingrese el tiempo del paciente: "))
                enfermedad = input("Ingrese la enfermedad del paciente en minutos: ")
                pac = Paciente(dni, tiempoespera, tiempomax, enfermedad)
                self.agregarpaciente(pac)

    def aumentartiempodeespera(self): #aumenta el tiempo de espera de los pacientes
        for paciente in self.listapaciente:
            paciente.set_tiempoespera(paciente.get_tiempoespera() + 5 ) #aumenta el tiempo

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

    def dearchivo_a_paciente(self,valor):#funcion que pasa de la lista archivos a la lista paciente, los pacientes.
                                         #se realiza esto para simular que ingresan pacientes en el medio del programa
        if valor == 0:
            h=0 
            while h < 6:
                self.agregarpaciente(self.listaarchivo[0])
                self.listaarchivo.pop(0)
                h+=1
            return True
        elif valor ==84 :
            h=0 
            while h < 22:
                self.agregarpaciente(self.listaarchivo[0])
                self.listaarchivo.pop(0)
                h+=1
            return True
        elif valor == 180:
             h=0 
             while h < 12:
                self.agregarpaciente(self.listaarchivo[0])
                self.listaarchivo.pop(0)
                h+=1
             return True
        else:
            return False

    def listado(self):
            listapacientescopia = self.listapaciente.copy()
            for paciente in listapacientescopia:
                if paciente.enfermedad in (Paciente.enfermedades.politraumatismo.value , Paciente.enfermedades.coma.value):
                    self.listarojo.append(paciente)
                    self.listapaciente.remove(paciente)
                elif paciente.enfermedad in (Paciente.enfermedades.convulsion.value, Paciente.enfermedades.hemorragia_dig.value,Paciente.enfermedades.isquemia.value):
                    self.listanaranja.append(paciente)
                    paciente.set_tiempoesperamaximo(10)
                    
                elif paciente.enfermedad in (Paciente.enfermedades.cefalea.value, Paciente.enfermedades.paresia.value,
                                             Paciente.enfermedades.hipertension.value,Paciente.enfermedades.vertigo.value,Paciente.enfermedades.sincope.value, Paciente.enfermedades.urgencia_psi.value):
                    self.listaamarillo.append(paciente)
                    paciente.set_tiempoesperamaximo(60)
                elif paciente.enfermedad in (Paciente.enfermedades.otalgias.value, Paciente.enfermedades.odontalgia.value,
                                             Paciente.enfermedades.dolor_leve.value, Paciente.enfermedades.traumatismos.value,Paciente.enfermedades.esguinces.value):
                    self.listaverde.append(paciente)
                    paciente.set_tiempoesperamaximo(120)
                else:
                    self.listaazul.append(paciente)
                    paciente.set_tiempoesperamaximo(240)

    def ordenar(self): #en esta función se está ordenando la cola de pacientes en función de la diferencia entre el tiempo de espera y el tiempo máximo de espera, según el método de mergesort
     
       self.listapaciente = merge_sort(self.listapaciente) #ordena la lista
    
       elprimero = self.listapaciente[0] #accede al primer elemento
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
       
    def dyc(self): #recibe la lista completa sin los rojos, y llama el ordenar
        j = 0      #si ponemos los pacientes en hp. listapaciente, hay que sacar la variable
       
        for j in self.listamedicoshab:
            if j.presentismo != False:
                if int( len(self.listarojo)) != 0:
                    j.atender(False)
                    if int(len(self.listarojo)) == 1:
                        self.listarojo.clear()
                    else:
                        self.listarojo.pop(0)
                     
                elif self.listapaciente:               
                    j.atender(False)
                    self.listapaciente.pop(0)
               

    def greedy(self): #recibe la hora del for 
        j = 0

        for j in self.listamedicoshab:
            if j.presentismo != False:
                if int(len(self.listarojo)) != 0:
                    j.atender(False)
                    self.listarojo.pop(0) 

                elif int(len(self.listanaranja)) != 0:
                    j.atender(False)
                    self.listanaranja.pop(0) 

                elif int(len(self.listaamarillo)) != 0:
                    j.atender(False)
                    self.listaamarillo.pop(0) 
                
                elif int(len(self.listaverde)) != 0:
                    j.atender(False)
                    self.listaverde.pop(0) 

                elif int(len(self.listaazul)) != 0:
                    j.atender(self.listaazul[0])
                    self.listaazul.pop(0)

    def pacientefallecido(self):
        j=0
        if len(self.listapaciente)==0:
            return
        for paciente in self.listapaciente:
            if paciente.tiempoespera == paciente.tiempoesperamax:
                print("el paciente",paciente.dni," con enfermedad ",paciente.enfermedad,"a fallecido")
                fallecido_label=tk.Label(text="El Paciente{} con enfermedad {} a fallecido".format(paciente.dni, paciente.enfermedad),font=("Arial",8),fg="red",justify='left' )
                fallecido_label.pack(fill=tk.BOTH, expand=True)
                self.listapaciente.remove(paciente)
        
#fuera de la clase 
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
    return lista_pacientes

