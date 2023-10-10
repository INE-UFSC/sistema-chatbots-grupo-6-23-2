import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot
from Bots.BotApaixonado import *
from Bots.BotNews import *
from view.window_selecao import WindowSelecao
from view.window_bot import WindowBot


class Controlador:

    # Inicialização de View e de Model
    def __init__(self, nome_empresa: str):
        self.__sistemacb = SistemaChatBot(nome_empresa)
        self.adicionar_bots()
        self.__view_selecao = WindowSelecao()
        self.__view_selecao.cria_janela(self.__sistemacb.boas_vindas(), self.__sistemacb.lista_bots)

    def adicionar_bots(self):
        # AQUI TERÁ TAMBÉM A PARTE DE PERSISTÊNCIA FUTURAMENTE
        self.__sistemacb.add_bot(BotApaixonado("Ricardo Nascimento"))
        self.__sistemacb.add_bot(BotNews("Bernardo Nogueira"))
    
    def inicio(self) -> None:
        self.__mostra_selecao()

    # Função responsável pela tela de seleção
    def __mostra_selecao(self) -> None:
        while True:
            evento, valores = self.__view_selecao.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.__view_selecao.fim()
                return

            if evento == 'Escolher':
                self.__sistemacb.escolhe_bot(valores['escolha'])
                janela_bot = WindowBot(self.__sistemacb.selected_bot)
                janela_bot.cria_janela()
                self.__tela_bot(janela_bot)

    # Função responsável pela tela do bot selecionado
    def __tela_bot(self, janela_bot) -> None:
        while True:
            evento, valores = janela_bot.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                janela_bot.fim()
                return

            if evento == 'Enviar':
                dict_resposta = self.__sistemacb.le_envia_comando(valores['escolha_comando'])
                dict_str = "\n".join([f"{key}: {value}" for key, value in dict_resposta.items()])
                janela_bot.mostra_resposta(dict_str)
