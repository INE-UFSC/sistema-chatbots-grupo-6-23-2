import PySimpleGUI as sg


class WindowFatalError:
    def __init__(self, error_message):
        sg.theme('DarkRed1')  # Define o tema como vermelho

        # Layout da janela
        layout = [
            [sg.Text(error_message, size=(30, 3))],
            [sg.Button('Fechar')]
        ]

        # Cria a janela
        self.window = sg.Window('Erro Fatal', layout, finalize=True)

    def run(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, 'Fechar'):
                break

        self.window.close()