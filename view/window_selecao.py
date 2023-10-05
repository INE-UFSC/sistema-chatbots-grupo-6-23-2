from window import Window
import PySimpleGUI as sg


class WindowSelecao(Window):

    def __init__(self):
        super().__init__()

    def cria_janela(self):
        self.__container = [
            [sg.Text(self.__controlador.boas_vindas(), key='boas_vindas', size=(60, 1))],
            [sg.Text("------- ESCOLHA O BOT -------")],
        ]
        for i, bot in enumerate(self.__controlador.lista_bots):
            self.__container.append([sg.Text(f"{i} - Bot: {bot.nome} | Mensagem de apresentação: {bot.apresentacao()}")])
        self.__container.append([sg.Text("Escolha: "), sg.InputText("", key='escolha'), sg.Button("Escolher")],)
        self.window = sg.Window('Selecione um Bot', self.__container)
