from abc import ABC, abstractmethod
import PySimpleGUI as ps


class Window(ABC):

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = None
    
    @abstractmethod
    def cria_conteiner(self):
        pass

    @abstractmethod
    def cria_janela(self):
        pass

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
