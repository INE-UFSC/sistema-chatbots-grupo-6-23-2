import PySimpleGUI as sg
from SistemaChatBot.SistemaChatBot import *
from Bots.BotNews import *
from view.window import Window
from view.window_fatal_error import WindowFatalError
from datetime import datetime
from Bots.Comando import ComandoNotFound
from Bots.ComandoAPI import APIConnectionError
from SistemaChatBot.SistemaChatBot import InvalidBotError
from DAO.BotDao import InvalidJsonBotError
import sys


class Controlador:

    # Inicialização de View e de Model
    def __init__(self, nome_empresa: str):
        try:
            self.__view = Window()
            self.__sistemacb = SistemaChatBot(nome_empresa)
            self.__view.cria_janela(self.__sistemacb.boas_vindas(), self.__sistemacb.lista_bots)
        except InvalidJsonBotError as e:
            self.fatal_error(str(e))

    def fatal_error(self, error: str):
        view = WindowFatalError(error)
        view.run()
        sys.exit()
    
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
            elif evento == 'Add Bot':
                self.add_new_bot_window()

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

    def add_new_bot_window(self):
        layout = [
            [sg.Text('Selecione um arquivo JSON:')],
            [sg.InputText(key='-FILE-', enable_events=True), sg.FileBrowse(file_types=(("JSON Files", "*.json"),))],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Adicionar Bot', layout)
        
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                window.close()
                return
            if event == 'OK' and values['-FILE-']:
                file_path = values['-FILE-']
                try:
                    self.__sistemacb.add_bot_file(file_path)
                    sg.popup("Bots adicionados!")
                except InvalidJsonBotError as e:
                    sg.popup(e)
                except FileNotFoundError:
                    sg.popup(e)
                self.__sistemacb.deselect_bot()
                self.__view.add_selecao_bot_component(self.__sistemacb.lista_bots)
                self.__view.update_scroll()
                window.close()
                return
