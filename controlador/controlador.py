import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import *
from Bots.BotNews import *
from view.window import Window
from datetime import datetime
from Bots.Comando import ComandoNotFound
from Bots.ComandoAPI import APIConnectionError
from SistemaChatBot.SistemaChatBot import InvalidBotError


class Controlador:

    # Inicialização de View e de Model
    def __init__(self, nome_empresa: str):
        self.__sistemacb = SistemaChatBot(nome_empresa)
        self.__view = Window()
        self.__view.cria_janela(self.__sistemacb.boas_vindas(), self.__sistemacb.lista_bots)
    
    def inicio(self) -> None:
        bot = self._main()

    def _main(self) -> None:
        while True:
            evento, valores = self.__view.le_eventos()

            if evento == sg.WINDOW_CLOSED:
                self.__view.fim()
                return

            if evento == 'Enviar':
                try:
                    self.__view.add_input_user(valores['input'])
                    if self.__sistemacb.selected_bot is None:
                        self.__sistemacb.escolhe_bot(valores['input'])
                        self._bot_selecionado(self.__sistemacb.selected_bot)
                    else:
                        dict_resposta = self.__sistemacb.le_envia_comando(valores['input'])
                        self._bot_responde(dict_resposta)
                except InvalidBotError as e:
                    self.__view.add_message_bot(str(e), error=True)
                except TypeError as e:
                    self.__view.add_message_bot(str(e), error=True)
                except ComandoNotFound as e:
                    self.__view.add_message_bot(str(e), error=True)
                except APIConnectionError as e:
                    self.__view.add_message_bot(str(e), error=True)

                self.__view.update_scroll()
            elif evento == '-SWAP-BUTTON-':
                self.__sistemacb.deselect_bot()
                self.__view.add_selecao_bot_component(self.__sistemacb.lista_bots)
                self.__view.update_scroll()

    def _bot_selecionado(self, bot: Bot):
        self.__view.add_message_bot(bot.apresentacao())
        self.__view.add_message_bot("O que eu posso fazer:")
        
        comandos = ""
        for id, comando in bot.comandos.items():
            comandos = f'{comandos}\n{id} - {comando.mensagem}'
        self.__view.add_message_bot(comandos)
        self.__view.habilitar_troca_bot()

    def _bot_responde(self, resposta: dict):
        if 'resposta_texto' in resposta:
            self.__view.add_message_bot(resposta["resposta_texto"])
        else:
            for noticia in resposta.values():
                self.__view.add_message_bot(f'{noticia["titulo"]} | {datetime.strptime(noticia["data"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")}')
            
