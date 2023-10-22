from enum import Enum
class Paciente :
    class enfermedades(Enum):
         POLITRAUMATISMO_GRAVE = "Politraumatismo grave"
         COMA = "Coma"
         CONVULSIONES = "Convulsiones"
         HEMORRAGIA_DIGESTIVA = "Hemorragia digestiva"
         ISQUEMIA = "Isquemia"
         CEFALEA_BRUSCA = "Cefalea brusca"
         PARESIA = "Paresia"
         HIPERTENSION_ARTERIAL = "Hipertensión arterial"
         VERTIGO_AFECTACION_VEGETATIVA = "Vértigo con afectación vegetativa"
         SINCOPE = "Síncope"
         URGENCIAS_PSIQUIATRICAS = "Urgencias psiquiátricas"
         OTALGIAS = "Otalgias"
         ODONTALGIAS = "Odontalgias"
         DOLORES_INESPECIFICOS_LEVES = "Dolores inespecíficos leves"
         TRAUMATISMOS_ESGUINCES = "Traumatismos y esguinces"
         NO_URGENCIA = "no urgencia "

    def __init__(self, dni, tiempoespera, tiempoesperamax, enfermedad):
        if enfermedad in Paciente.enfermedades:
            self.enfermedad = enfermedad
        self.dni = dni
        self.tiempoespera = tiempoespera
        self.tiempoesperamax = tiempoesperamax


class Medico:
    def __init__(self, dni, horarioinicio, horariofin, presentismo):
        self.dni= dni
        self.horarioinicio= horarioinicio
        self.horariofin = horariofin
        self.presentismo = presentismo # si esta habilitado para atender o esta ocupado

    def atender(paciente):


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
    def ordenar (cola):#en esta función se está ordenando la cola de pacientes en función de la diferencia entre el tiempo de espera y el tiempo máximo de espera, según el método de mergesort
        if len(cola)>1:
            medio= len(cola)/2
            izq = cola[:medio]
            der= cola[medio:]
            ordenar(izq)
            ordenar(der)

            i=j=k=0
            while i< len(izq) and j< len(der):
                if (izq[i].tiempoespera -izq[i].tiempoesperamax) < (der[j].tiempoespera - der[j].tiempomaxespera):
                    cola[k] = izq[i]
                    i +=1
                else:
                    cola[k] = der[j]
                     j +=1
            k+=1
            while i < len(izq):
                cola[k] = izq[i]
                i+=1
                k+=1

            while j < len(der):
                cola[k] = der[j]
                j+=1
                k+=1
            return cola[0]



def dyc(self, cola):
        j=0
        for j in range(self.listamedicos):
            if j.presentismo != false:
                if self.listarojo != null:
                    j.atender(self.listarojo[0])
                    self.listarojo =self. listarojo[1:]
                else:
                    pacientemasproximo = ordenar(cola)
                    j.atender(pacientemasproximo)
                    cola = cola[1:]


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
