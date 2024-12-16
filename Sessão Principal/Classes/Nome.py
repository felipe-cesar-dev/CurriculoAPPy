from ClassesAbstratas.NomeABS import NomeABS
from Tratadores.TratarNome import TratarNome


class Nome(NomeABS):
    def __init__(self, tratarnome: TratarNome, nome = ''):
        super().__init__(tratarnome, nome = '')
        self._nome = nome
        self._tratarnome = tratarnome

    def set_nome(self):
        self._nome = input("Digite um nome: ")
        self._tratarnome.verificar_alfanum(self._nome)
        

n = Nome(TratarNome())
n.set_nome()
