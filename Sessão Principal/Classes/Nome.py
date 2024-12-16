from ClassesAbstratas.NomeAbs import NomeAbstrato
import re

class Nome(NomeAbstrato):
    def __init__(self, nome = ''):
        super().__init__(nome)
        self.nome = nome

    def verifica_nome_vazio(self, string):
        if not string.strip():
            raise ValueError("Nome não pode estar em branco")
        return string.title()

    def contem_numero(self, string):
        checagem = bool(re.search(r'\d', string))
        if checagem:
            raise ValueError

    def set_nome(self):
        while True:
            try:
                self.nome = self.verifica_nome_vazio(input("Digite um nome: "))
                self.contem_numero(self.nome)
                break
            except ValueError:
                print("Nome não pode estar em branco ou conter números!")

    def get_nome(self):
        return print("O nome é: %s" %self.nome)





