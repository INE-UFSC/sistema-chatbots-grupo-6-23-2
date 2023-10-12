import time
import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import SistemaChatBot
from Bots.BotApaixonado import *
from Bots.BotNews import *
from view.window import Window


class Controlador:

    # Inicialização de View e de Model
    def __init__(self, nome_empresa: str):
        self.__sistemacb = SistemaChatBot(nome_empresa)
        self.adicionar_bots()
        self.__view = Window()
        self.__view.cria_janela(self.__sistemacb.boas_vindas(), self.__sistemacb.lista_bots)

    def adicionar_bots(self):
        # AQUI TERÁ TAMBÉM A PARTE DE PERSISTÊNCIA FUTURAMENTE
        self.__sistemacb.add_bot(BotApaixonado("Ricardo Nascimento"))
        self.__sistemacb.add_bot(BotNews("Bernardo Nogueira"))
    
    def inicio(self) -> None:
        bot = self._main()

    def _main(self) -> None:
        while True:
            evento, valores = self.__view.le_eventos()

            print(evento)

            if evento == sg.WINDOW_CLOSED:
                self.__view.fim()
                return

            if evento == 'Enviar':
                self.__view.add_input_user(valores['input'])

                if self.__sistemacb.selected_bot is None:
                    self.__sistemacb.escolhe_bot(valores['input'])
                    self._bot_selecionado(self.__sistemacb.selected_bot)
                else:
                    dict_resposta = self.__sistemacb.le_envia_comando(valores['input'])
                    self._bot_responde(dict_resposta)

                self.__view.update_scroll()

    def _bot_selecionado(self, bot: Bot):
        self.__view.add_message_bot(bot.apresentacao())
        self.__view.add_message_bot("O que eu posso fazer:")
        
        comandos = ""
        for id, comando in bot.comandos.items():
            comandos = f'{comandos}\n{id} - {comando.mensagem}'
        self.__view.add_message_bot(comandos)

    def _bot_responde(self, resposta: dict):
        if len(resposta) > 1: #Lógica implicia (se tiver mais de uma resposta é porque é do tipo botnews) ALTERAR!!
            self.__view.add_message_bot(resposta[0]['titulo'])
        else:
            self.__view.add_message_bot(resposta["resposta"])
