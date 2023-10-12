from view.window import Window
import PySimpleGUI as sg


class WindowSelecao(Window):

    def __init__(self):
        super().__init__()
        sg.theme('GreenMono')

    def cria_janela(self, boas_vindas: str, lista_bots):
        center_column = super().add_row_center(center_column=None, row=super().message_bot_box("Por favor, escolha o bot:"))
        for i, bot in enumerate(lista_bots):
            center_column = super().add_row_center(center_column=center_column, row=super().message_bot_box(f"{i} - Bot: {bot.nome}\nMensagem de apresentação: {bot.apresentacao()}"))

        self.__container = [
            super().cabecalho(boas_vindas),
            [center_column],
            super().input_user()
        ]
        self.window = sg.Window('Selecione um Bot', self.__container, size=(800, 600))
