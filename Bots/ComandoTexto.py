from Bots.Comando import Comando
import random


class ComandoTexto(Comando):
    def __init__(self, id: int, mensagem: str) -> None:
        super().__init__(id, mensagem)
        self.__respostas = []

    def add_resposta(self, retorno: str):
        self.__respostas.append(retorno)
        return self

    def remove_resposta(self, index: int):
        self.__respostas.pop(index)

    def get_random_resposta(self):
        return random.choice(self.__respostas)
    
    def retorno(self):
        return {'resposta': self.get_random_resposta()}