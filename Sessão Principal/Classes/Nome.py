from Tratadores.TratarNome import TratarNome

class Nome:
    def __init__(self):
        self._nome = ""
        self.tratador = TratarNome()

    def capturar_nome(self):
        self._nome = self.tratador.capturar_nome()

    def imprimir_nome(self):
        print("O nome é: %s" %self._nome)

nome = Nome()
nome.capturar_nome()
nome.imprimir_nome()