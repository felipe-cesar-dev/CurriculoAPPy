from datetime import datetime

class Data:
    def __init__(self):
        self._nasc = ''
    
    def captura_data(self):
        while True:
            self._nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
            try:
                datetime.strptime(self._nasc, '%d/%m/%Y')
                return self._nasc
            except ValueError:
                print("Formato inválido")
    
    def imprime_data(self):
        print(self._nasc)

