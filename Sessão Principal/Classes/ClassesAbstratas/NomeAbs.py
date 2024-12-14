from abc import ABC, abstractmethod

class NomeAbstrato(ABC):
    def __init__(self, nome):
        self.nome = nome
    @abstractmethod
    def verifica_nome_vazio(self, string):
        pass
    @abstractmethod
    def contem_numero(self, string):
        pass
    @abstractmethod
    def set_nome(self):
        pass
    @abstractmethod
    def get_nome(self):
        return self.nome
