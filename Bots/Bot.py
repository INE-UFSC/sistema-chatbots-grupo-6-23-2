from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def mostra_comandos(self):
        print("--------- COMANDOS ------------")
        for i, comando in self.comandos.items():
            if i != "default":
                print(f"{i} - {comando['cmd']}")

    @abstractmethod
    def executa_comando(self, cmd): # RETORNAR TRUE SE O COMANDO FOR PARA ENCERRAR O CHAT
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass