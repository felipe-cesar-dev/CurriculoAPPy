from datetime import datetime
from Tratadores.TratarData import TratarData

class Data:
    def __init__(self):
        self._nasc = TratarData()
        self.data = ""
    
    def tratar_data(self):
        self.data = self._nasc.captura_data()

    
    def imprime_data(self):
        print(self.data)


a = Data()
a.tratar_data()
a.imprime_data()

