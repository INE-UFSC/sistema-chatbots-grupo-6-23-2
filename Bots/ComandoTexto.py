from Comando import Comando
import random


class ComandoTexto(Comando):
    def __init__(self, id: int, mensagem: str) -> None:
        super().__init__(id, mensagem)
        self.__retornos = []

    def add_retorno(self, retorno: str):
        self.__retornos.append(retorno)

    def remove_retorno(self, index: int):
        self.__retornos.pop(index)

    def get_random_retorno(self):
        return random.choice(self.__retornos)
    
    @property
    def retorno(self):
        return {'resposta': self.get_random_retorno()}