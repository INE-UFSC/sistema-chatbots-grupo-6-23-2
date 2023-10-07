from abc import ABC, abstractmethod
from Bots.Comando import Comando, ComandoNotFound
from Bots.ComandoAPI import ComandoAPI
from Bots.ComandoTexto import ComandoTexto


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

    def add_comando(self, comando: Comando):
        if isinstance(comando, Comando):
            self.comandos[comando.id] = comando
    
    def remove_comando(self, id: int):
        if id in self.comandos:
            del self.comandos[id]
    
    def mostra_comandos(self):
        return self.comandos

    def executa_comando(self, cmd: int, *args: str):
        if cmd in self.comandos:
            comando = self.comandos[cmd]
            if isinstance(comando, Comando):
                if isinstance(comando, ComandoAPI):
                    return comando.retorno(*args)
                else:
                    return comando.retorno()
            else:
                raise TypeError("Este tipo de comando não é válido!")
        else:
            raise ComandoNotFound(f"O comando {cmd} não está disponível para este bot.")

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass

    @abstractmethod
    def apresentacao(self):
        pass

    