##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.nome = nome
        self.comandos = {}

    #nao esquecer o decorator
    def nome(self):
        pass

    #nao esquecer o decorator
    def nome(self, nome):
        pass

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass