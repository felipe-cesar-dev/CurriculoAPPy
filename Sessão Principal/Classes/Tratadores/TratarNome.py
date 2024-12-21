class TratarNome:
    def verificar_nome_vazio(self, nome: str) -> bool:
        return nome.strip()
    
    def verificar_is_numero(self, nome: str) -> bool:
        return nome.isalpha()

    def capturar_nome(self) -> str:
        while True:
            nome = input("Digite um nome: ")
            if self.verificar_nome_vazio(nome) and self.verificar_is_numero(nome):
                return nome
            print("Digite um nome válido (sem números).")


a = TratarNome()
a.capturar_nome()