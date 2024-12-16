from abc import ABC, abstractmethod

class InfosPessoaisAbstrato(ABC):
    def __init__(self, nascimento):
        self.__nascimento = nascimento

    @abstractmethod
    def set_nascimento(self):
        pass

    @abstractmethod
    def get_nascimento(self):
        return self.__nascimento

    @abstractmethod
    def mostra_nascimento(self):
        pass







