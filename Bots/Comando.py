from abc import ABC, abstractclassmethod


class Comando(ABC):
    def __init__(self, id: int, mensagem: str) -> None:
            self.__id = int(id)
            self.__mensagem = mensagem
            self.__retorno = None

    @property
    def mensagem(self, mensagem: str):
          self.__mensagem = mensagem

    @property
    @abstractclassmethod
    def retorno(self):
        pass