import pytest
from clases import Paciente
from clases import Medico
from clases import Hospital

def lista_de_medicos():
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
    




