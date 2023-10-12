import PySimpleGUI as sg
from view.window import Window
from Bots import Bot

class WindowBot(Window):
    def __init__(self, bot: Bot):
        super().__init__()
        self.__bot = bot
        self.__resposta_visivel = False  # Inicialmente, a resposta está oculta
        sg.theme('GreenMono')

    # Cria a janela específica do Bot
    def cria_janela(self) -> None:
        self.__container = [
            super().cabecalho(f"Bot {self.bot.nome}"),
            super().message_bot_box(self.bot.apresentacao()),
            super().message_bot_box("Meus comandos:")
        ]

        # Uma linha por comando do bot
        comandos = ""
        for id, comando in self.__bot.comandos.items():
            comandos = f'{comandos}\n{id} - {comando.mensagem}'

        coluna_center = super().add_row_center(center_column=None, row=super().message_bot_box(comandos))
        self.__container.append([coluna_center])
        self.__container.append(super().input_user())

        self.window = sg.Window(f'Bot: {self.__bot.nome}', self.__container, size=(800, 600))

    def mostra_resposta(self, resposta) -> None:
        pass

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
