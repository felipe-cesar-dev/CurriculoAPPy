class TratarNome:
    def __init__(self, nome = ''):
        self.nome = nome
    
    def verificar_alfanum(self, string: str):
        while True:
            try:
                if not string.isalpha():
                    raise ValueError("Digite um nome válido e sem números!")
                else:
                    break
            except ValueError as e:
                print(e)
                string = input("Digite novamente: ")

    
        