from window import Window
import PySimpleGUI as ps


class WindowSelecao(Window):

    def __init__(self, controlador):
        super().__init__(controlador)

    def cria_conteiner(self):
        self.__container = [
            [ps.Text(self.__controlador.boas_vindas(), key='boas_vindas', size=(60, 1))],
            [ps.Text("------- ESCOLHA O BOT -------")],
        ]
        for i, bot in enumerate(self.__controlador.lista_bots):
            self.__container.append([ps.Text(f"{i} - Bot: {bot.nome} | Mensagem de apresentação: {bot.apresentacao()}")])
        self.__container.append([ps.Text("Escolha: "), ps.InputText("", key='escolha'), ps.Button("Escolher")],)