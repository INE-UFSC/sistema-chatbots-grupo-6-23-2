from abc import ABC, abstractclassmethod


class Comando(ABC):
    def __init__(self, id: int, mensagem: str) -> None:
            self.__id = int(id)
            self.__mensagem = mensagem

    @property
    def mensagem(self):
          return self.__mensagem
    
    @property
    def id(self):
        return self.__id

    @abstractclassmethod
    def retorno(self):
        pass

class ComandoNotFound(KeyError):
    def __init__(self, comando, message="Comando não encontrado"):
        self.comando = comando
        self.message = f"{message}: {comando}"
        super().__init__(self.message)