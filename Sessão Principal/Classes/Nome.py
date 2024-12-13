class Nome:
    def __init__(self, nome = ''):
        self.nome = nome

    def valida_nome(self, nome):
        if not nome.strip():
            raise ValueError("Nome não pode estar vazio")
        return nome.title()

    def set_nome(self):
        while True:
            try:
                self.nome = self.valida_nome(input("Digite seu nome: "))
                break
            except ValueError as e:
                print(e)

    def get_nome(self):
        return self.nome

    def mostra_nome(self):
        print("Nome: %s" %self.nome)



nome = Nome()
nome.set_nome()
nome.mostra_nome()


