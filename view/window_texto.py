import PySimpleGUI as ps
from window import Window
from Bots import Bot


class WindowBot(Window):

    def __init__(self, controlador, bot: Bot):
        super().__init__(controlador)
        self.__bot = bot

    # Cria a janela específica do Bot
    def cria_janela(self) -> None:
        self.__container = [
            [ps.Text(self.__bot.apresentacao(), key='apresentacao')],
            [ps.Text(f'Seguem abaixo os comandos do {self.__bot.nome}:')]
        ]

        # Uma linha por comando do bot
        for id, comando in self.__bot.comandos.items():
            comando = [ps.Button(f'{id}'), ps.Text(f'{comando}')]
            self.__container.append(comando)

        # Texto da resposta que será atualizado conforme o botão
        # pressionado
        resposta = [ps.Text('', key=resposta)]
        self.__window = ps.Window(f'Bot: {self.__bot.nome}', self.__container)

    def mostra_resposta(self, resultado) -> None: 
        self.__window.Element('resposta').Update(resultado)

    # Retorna os eventos da janela
    def le_eventos(self) -> (ps.Any | tuple[str, ps.Any] | None):
        return self.__window.read()

    def fim(self) -> None:
        self.__window.close()
