from ClassesAbstratas.InfosPessoaisAbs import InfosPessoaisAbstrato
from datetime import datetime

class InfosPessoais(InfosPessoaisAbstrato):
    def __init__(self, nascimento = ''):
        super().__init__(nascimento)
        self.__nascimento = nascimento

    def set_nascimento(self):
        while True:
            try:
                data = input("Digite a data de nascimento (DD/MM/AAAA): ")
                datetime.strptime(data, "%d/%m/%Y")  # Valida formato
                self.__nascimento = data
                break
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

    def get_nascimento(self):
        return self.__nascimento

    def mostra_nascimento(self):
        return print("A data de nascimento é %s" % self.__nascimento)










