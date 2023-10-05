from abc import ABC, abstractmethod
import PySimpleGUI as ps


class Window(ABC):

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = None
    
    @abstractmethod
    def cria_janela(self):
        pass

    # Retorna os eventos da janela
    def le_eventos(self) -> (ps.Any | tuple[str, ps.Any] | None):
        return self.__window.read()

    def fim(self):
        self.__window.close()
