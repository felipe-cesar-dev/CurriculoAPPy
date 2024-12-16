from abc import ABC, abstractmethod

class NomeABS(ABC):
    def __init__(self, tratarnome: any, nome = ''):
        self._nome = nome
        self._tratarnome = tratarnome

    @abstractmethod
    def set_nome(self):
        pass


