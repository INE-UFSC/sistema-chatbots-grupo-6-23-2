from view.window import Window
import PySimpleGUI as sg


class WindowSelecao(Window):

    def __init__(self):
        super().__init__()
        sg.theme('GreenMono')

    def cria_janela(self, boas_vindas: str, lista_bots):
        self.__container = [
            [sg.Text(boas_vindas, key='boas_vindas', size=(60, 1), font=('Arial', 18), justification='center')],
            [sg.Column([
                [sg.Image(filename='view/bot.png', background_color='white'), sg.Text("Por favor, escolha o bot:", size=(50, 2), font=('Arial', 16), background_color='white')],
                *[
                    [sg.Image(filename='view/bot.png', background_color='white'), sg.Text(f"{i} - Bot: {bot.nome}\nMensagem de apresentação: {bot.apresentacao()}", size=(50, 2), font=('Arial', 16), background_color='white')] for i, bot in enumerate(lista_bots)
                ]
            ], pad=((0, 0), (30, 0)), size=(800, 450), vertical_scroll_only=True, scrollable=True)],
            [sg.InputText("", tooltip='Digite aqui...', key='escolha', size=(55, 1), font=('Arial', 16), pad=((0, 0), (20, 0))),
                sg.Button("Escolher", font=('Arial', 16), pad=((10, 0), (20, 0)))]
        ]
        self.window = sg.Window('Selecione um Bot', self.__container, size=(800, 600))
