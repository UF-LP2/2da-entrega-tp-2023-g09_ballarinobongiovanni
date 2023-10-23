from enum import Enum
class Paciente :
    class enfermedades(Enum):
         politraumatismo = "Politraumatismo grave"
         coma = "Coma"
         convolusion = "Convulsiones"
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
         esguinces= "Esguinces"
         no_urgencia = "no urgencia "

    def __init__(self, dni, tiempoespera, tiempoesperamax, enfermedad):
        if enfermedad in Paciente.enfermedades:
            self.enfermedad = enfermedad
        self.dni = dni
        self.tiempoespera = tiempoespera
        self.tiempoesperamax = tiempoesperamax

    def set_tiempoesperamaximo(self, tiempoesperamaximo):
        self.tiempoesperamax = tiempoesperamaximo

class Medico:
    def __init__(self, dni, horarioinicio, horariofin, presentismo):
        self.dni = dni
        self.horarioinicio = horarioinicio
        self.horariofin = horariofin
        self.presentismo = presentismo # si esta habilitado para atender o esta ocupado

    def atender(self, paciente):
        print("faltaponeralgo")
        self.presentismo = False


class Hospital:
    def __init__(self, nombre):
        self.listapaciente = []
        self.listamedicos = []
        self.listarojo = []
        self.listanaranja = []
        self.listaamarillo = []
        self.listaverde = []
        self.listaazul = []
        self.nombre =nombre
    def medicoshorario(self, horaactual): #retorna una lista
        listamedicohabilitado = []

        for medico in self.listamedicos:
            if medico.horarioinicio <= horaactual and medico.horariofin >= horaactual:
                listamedicohabilitado.append(medico)

        return listamedicohabilitado

    def agregarpaciente(self, paciente):
        self.listapaciente.append(paciente)
    def agregarmedico(self, medico):
        self.listamedicos.append(medico)
    def listado(self,listaespera):
            for paciente in listaespera:
                if paciente.enfermedad in (Paciente.enfermedades.politraumatismo, Paciente.enfermedades.coma):
                    self.listarojo.append(paciente)
                elif paciente.enfermedad in (Paciente.enfermedades.convolusion, Paciente.enfermedades.hemorragia_dig,Paciente.enfermedades.isquemia):
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

    def ordenar(self, listaespera):  # en esta función se está ordenando la cola de pacientes en función de la diferencia entre el tiempo de espera y el tiempo máximo de espera, según el método de mergesort
        if len(listaespera) > 1:
            medio = len(listaespera) / 2
            izq = listaespera[:medio]
            der = listaespera[medio:]
            self.ordenar(izq)
            self.ordenar(der)

            i = j = k = 0
            while i < len(izq) and j < len(der):
                if (izq[i].tiempoespera - izq[i].tiempoesperamax) < (der[j].tiempoespera - der[j].tiempomaxespera):
                    listaespera[k] = izq[i]
                    i += 1
                else:
                    listaespera[k] = der[j]
                    j += 1
            k += 1
            while i < len(izq):
                listaespera[k] = izq[i]
                i += 1
                k += 1

            while j < len(der):
                listaespera[k] = der[j]
                j += 1
                k += 1
            return listaespera[0]

    def dyc(self, listaespera):
        j = 0

        for j in range(self.listamedicos):
            if j.presentismo != False:
                if self.listarojo != None:
                    j.atender(self.listarojo[0])
                    self.listarojo = self.listarojo[1:]
                else:
                    pacientemasproximo = self.ordenar(listaespera)
                    j.atender(pacientemasproximo)
                    listaespera = listaespera[1:]

    def greedy(self, horaactual):
        j = 0
        for j in (self.medicoshorario(horaactual)):
            if j.capacidad != False:
                if self.listarojo != None:
                    j.atender(self.listarojo[0])
                    self.listarojo = self.listarojo[1:]  # por ahi hay que hacerlo con get y set

                if self.listanaranja != None:
                    j.atender(self.listanaranja[0])
                    self.listanaranja = self.listanaranja[1:]

            if self.listaamarillo != None:
                j.atender(self.listaamarillo[0])
                self.listaamarillo = self.listaamarillo[1:]
            if self.listaverde != None:
                j.atender(self.listaamarillo[0])
                self.listaverde = self.listaverde[1:]

            if self.listaazul != None:
                j.atender(self.listaazul[0])
                self.listanaazul = self.listanaazul[1:]



"""
fjjfipjdckpkcjspdjpjdsjdkskj.c..c..c.c..cdlcslcsld,
función ordenar(cola): //en esta función se está ordenando la cola de pacientes en función de la diferencia entre el tiempo de espera y el tiempo máximo de espera, según el método de mergesort

	si len(cola) >1:
		medio = len(cola)/2
		izq = cola[:mid]
		der = cola[mid:]
		ordenar(izq)
		ordenar(der)
		
		i=J=k=0
		mientras i < len(izq) and j < len (der):
			si (izq[i].tiempoespera -izq[i]tiempomaxespera) < (der[j].tiempoespera  -                                                              -der[j].tiempomaxespera):
				cola[k] = izq[i]
				i += 1
			sino: 
				cola[k] = der[j]
				j +=1
			k +=1
		 mientras i < len(izq):
			cola[k] = izq[i]
                                  i++
			k++
		 mientras j< len (der):
			cola[k] = der[j]
			j ++
			k++

	devolver cola[0]

"""
