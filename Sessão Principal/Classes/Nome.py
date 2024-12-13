import re

class Nome:
    def __init__(self, nome = ''):
        self.nome = nome

    def valida_nome(self, nome):
        if not nome.strip():
            raise ValueError("Nome não pode estar vazio")
        return nome.title()

    def contem_numero(self, string):
        checagem =  bool(re.search(r'\d', string))
        if checagem:
            raise ValueError

    def set_nome(self):
        while True:
            try:
                self.nome = self.valida_nome(input("Digite seu nome: "))
                self.contem_numero(self.nome)
                break
            except ValueError:
                print('Nome não pode ser em branco ou conter números')

    def get_nome(self):
        return self.nome

    def mostra_nome(self):
        print("Nome: %s" %self.nome)



nome = Nome()
nome.set_nome()
nome.mostra_nome()


