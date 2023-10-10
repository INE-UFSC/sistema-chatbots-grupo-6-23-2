from view.window import Window
import PySimpleGUI as sg


class WindowSelecao(Window):

    def __init__(self):
        super().__init__()
        sg.theme('GreenMono')

    def cria_janela(self, boas_vindas: str, lista_bots):
        self.__container = [
            [sg.Text(boas_vindas, key='boas_vindas', size=(60, 1), font=('Arial', 18), justification='center')],
            [sg.Text('', size=(1, 10))],
            [sg.Text("Por favor, escolha o bot:", size=(80, 2), font=('Arial', 16), background_color='white')],
        ]
        for i, bot in enumerate(lista_bots):
            self.__container.append([sg.Text(f"{i} - Bot: {bot.nome} | Mensagem de apresentação: {bot.apresentacao()}")])
        self.__container.append([sg.InputText("", tooltip='Digite aqui...', key='escolha', size=(95, 1)), sg.Button("Escolher")])
        self.window = sg.Window('Selecione um Bot', self.__container, size=(800, 600))
