import PySimpleGUI as sg
from textwrap import wrap

from SistemaChatBot.SistemaChatBot import InvalidBotError


class Window:

    def __init__(self):
        self.__container = []
        self.__window = None
        self.__bot = None
        sg.theme('GreenMono')
        self.__center_column = []

    def cria_janela(self, boas_vindas: str, lista_bots):
        self.__container = [
            [sg.Menu([['Add Bot', 'Add Bot']])],
            self._cabecalho(boas_vindas),
            [sg.Column(self.center_column, expand_y=True, key='-COLUMN-', size=(800, 450), vertical_scroll_only=True, scrollable=True)],
            self._input_user_label()
        ]
        self.window = sg.Window(f'Sistema ChatBots',  self.__container, size=(800, 600), return_keyboard_events=True, finalize=True)
        self.add_selecao_bot_component(lista_bots)

    def add_selecao_bot_component(self, lista_bots):
        self._add_row_center(self._message_bot_box("Por favor, escolha o bot:"))
        for i, bot in enumerate(lista_bots):
            self._add_row_center(self._message_bot_box(f"{i} - Bot: {bot.nome}\nMensagem de apresentação: {bot.apresentacao()}"))
        self.window['input'].set_size((55, 1))
        self.window["-SWAP-BUTTON-"].update(visible=False)


    @property
    def center_column(self):
        return self.__center_column
    
    @property
    def container(self):
        return self.__container
    
    @property
    def bot(self):
        return self.__bot

    # Retorna os eventos da janela
    def le_eventos(self):
        self.window.refresh()
        return self.__window.read()

    def fim(self):
        self.__window.close()

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, window):
        self.__window = window

    def _wrap_text(self, text: str, max_line_length):
        lines = text.splitlines()  # Divide a string em linhas com base nas quebras de linha existentes
        wrapped_lines = []

        for line in lines:
            wrapped = wrap(line, width=max_line_length)
            wrapped_lines.extend(wrapped)

        result = '\n'.join(wrapped_lines)
        return result, result.count('\n')+1

    def _create_box_message(self, msg: str, user: bool, error: bool):
        component = None
        msg, height_line = self._wrap_text(msg, 60)
        height_line = 2 if height_line < 2 else height_line
        if error:
            component = [sg.Image(filename='view/bot.png', background_color='#FF6B6B'), sg.Text(msg, size=(50, height_line), font=('Arial', 16), background_color='#FF6B6B', text_color='white')]
        else:
            if user:
                component = [sg.Text(msg, pad=((80, 0), (0, 0)), size=(50, height_line), font=('Arial', 16), background_color='white'), sg.Image(filename='view/user.png', background_color='white')]
            else:
                component = [sg.Image(filename='view/bot.png', background_color='white'), sg.Text(msg, size=(50, height_line), font=('Arial', 16), background_color='white')]

        return component


    def _error_box(self, msg: str):
        return self._create_box_message(msg, False, True)

    def _message_user_box(self, msg: str):
        return self._create_box_message(msg, True, False)

    def _message_bot_box(self, msg: str):
        return self._create_box_message(msg, False, False)
    
    def _cabecalho(self, msg: str):
        return [sg.Text(msg, size=(60, 1), font=('Arial', 18), justification='center')]
    
    def _add_row_center(self, row: list):
        self.center_column.append(row)
        self.window['-COLUMN-'].contents_changed()
        self.window.extend_layout(self.window['-COLUMN-'], [row])
        self.window.refresh()

    def _input_user_label(self):
        return [sg.InputText("", tooltip='Digite aqui...', key='input', size=(55, 1), font=('Arial', 16), pad=((0, 0), (20, 0))),
            sg.Button("Enviar", tooltip='Press enter', font=('Arial', 16), pad=((10, 0), (20, 0))), sg.Button("Trocar de bot", key="-SWAP-BUTTON-", tooltip='Press esc', visible=False, font=('Arial', 16), pad=((10, 0), (20, 0)))]
    
    def habilitar_troca_bot(self):
        self.window['input'].set_size((40, 1))
        self.window["-SWAP-BUTTON-"].update(visible=True)
    
    def add_message_bot(self, message: str, error=False):
        try:
            if error:
                self._add_row_center(self._error_box(message))
            else:
                self._add_row_center(self._message_bot_box(message))
        except AttributeError:
            raise InvalidBotError()

    def add_input_user(self, input: str):
        self._add_row_center([sg.VerticalSeparator(color = None, pad = ((0, 0), (10, 10)))])
        self.window['input'].update("")
        self._add_row_center(self._message_user_box(input))

    def update_scroll(self):
        self._add_row_center([sg.VerticalSeparator(color = None, pad = ((0, 0), (10, 10)))])
        self.window['-COLUMN-'].Widget.canvas.yview_moveto(1.0)

