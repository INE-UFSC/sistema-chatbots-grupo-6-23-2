from Bots.Bot import Bot

class BotApaixonado(Bot):

    def __init__(self, nome):
        super().__init__(nome)
        self.comandos = {
                1: {
                    "cmd": 'Qual a coisa mais importante para você?',
                    'resposta': 'Você, é claro! <3'
                },
                2: {
                    "cmd": 'Que horas são?',
                    "resposta":'Hora de você me dar uma beijinho *-*'
                },
                3: {
                    "cmd": 'Qual o sentido da vida?',
                    "resposta": 'O sentido eu não sei, mas eu sei que ela'\
                        + ' perde o sentido sem você...'
                },
                4: {
                    "cmd": 'Eu já sou comprometido(a)',
                    "resposta": 'Não tem problema, eu sei guardar segredo rsrs'
                },
                -1: {
                    "cmd": 'Até logo'
                },
                "default": {"resposta": 'Estava distraído demais com sua beleza e não'\
                      + ' entendi. Pode repetir?'}
            }

    def apresentacao(self):
        return f'Oiii, tudo bem? Eu sou o {super().nome}'
        
    def executa_comando(self, cmd):
        print(self.comandos.get(cmd, "default")["resposta"])

    def boas_vindas(self):
        print('Oi, chuchu rsrs. Você vem sempre por aqui?')

    def despedida(self):
        print("Tchau... vou sentir saudades :'(")
