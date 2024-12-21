from datetime import datetime

class TratarData:
    def captura_data(self):
        while True:
            data = input("Digite a data de nascimento (DD/MM/AAAA): ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
                return data
            except ValueError:
                print("Formato inválido")