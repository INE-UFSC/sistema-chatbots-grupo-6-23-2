import PySimpleGUI as sg
from view.window import Window
from Bots import Bot


class WindowBot(Window):

    def __init__(self, bot: Bot):
        super().__init__()
        self.__bot = bot

    # Cria a janela específica do Bot
    def cria_janela(self) -> None:
        self.__container = [
            [sg.Text(self.__bot.apresentacao(), key='apresentacao')],
            [sg.Text(f'Seguem abaixo os comandos de {self.__bot.nome}:')]
        ]

        # Uma linha por comando do bot
        for id, comando in self.__bot.comandos.items():
            comando = [sg.Text(f'{id} - {comando.mensagem}')]
            self.__container.append(comando)
        
        selecao = [sg.Text('O que deseja dizer ao bot?'), sg.InputText(key='escolha_comando'), sg.Button('Enviar')]
        self.__container.append(selecao)

        # Texto da resposta que será atualizado conforme o botão
        # pressionado
        resposta = [sg.Text('', key='resposta')]
        self.__container.append(resposta)

        self.window = sg.Window(f'Bot: {self.__bot.nome}', self.__container)

    def mostra_resposta(self, resposta) -> None: 
        self.window.Element('resposta').Update(resposta)

    # Retorna os eventos da janela
    def le_eventos(self) -> (sg.Any | tuple[str, sg.Any] | None):
        return self.window.read()

    def fim(self) -> None:
        self.window.close()

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot
