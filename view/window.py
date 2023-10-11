from abc import ABC, abstractmethod
import PySimpleGUI as sg


class Window(ABC):

    def __init__(self):
        self.__container = []
        self.__window = None
        self.__bot = None
    
    @abstractmethod
    def cria_janela(self):
        pass

    # Retorna os eventos da janela
    def le_eventos(self) -> (sg.Any | tuple[str, sg.Any] | None):
        return self.__window.read()

    def fim(self):
        self.__window.close()

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, window):
        self.__window = window
    
    # Implementar função e mensagem de erro
    def error(self, mensagem: str):
        print(mensagem)
