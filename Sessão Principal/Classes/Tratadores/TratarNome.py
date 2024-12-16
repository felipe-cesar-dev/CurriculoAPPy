class TratarNome:
    def verificar_nome(self, nome: str) -> bool:
        return nome.strip().isalpha()

    def capturar_nome(self) -> str:
        while True:
            nome = input("Digite um nome: ")
            if self.verificar_nome(nome):
                return nome
            print("Digite um nome válido (sem números).")