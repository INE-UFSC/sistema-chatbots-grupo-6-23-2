from Bots.Bot import Bot

class BotApaixonado(Bot):

    def __init__(self, nome):
        super().__init___(nome)
        comandos_dict = {
            1: 'Qual a coisa mais importante para você?',
            2: 'Que horas são?',
            3: 'Qual o sentido da vida?',
            4: 'Eu já sou comprometido(a)',
            5: 'Até logo',
            }
        super().comandos(comandos_dict)

    def executa_comando(self, cmd):
        for cmd in range(4):

            if (cmd + 1) == 1:
                print('Você, é claro! <3')
            elif (cmd + 1) == 2:
                print('Hora de você me dar uma beijinho *-*')
            elif (cmd + 1) == 3:
                print('O sentido eu não sei, mas eu sei que ela\
                      perde o sentido sem você...')
            elif (cmd + 1) == 4:
                print('Não tem problema, eu sei guardar segredo rsrs')
            elif (cmd + 1) == 5:
                return True
            else:
                print('Estava distraído demais com sua beleza e não\
                      entendi. Pode repetir?')

    def boas_vindas(self):
        return 'Oi, chuchu rsrs. Você vem sempre por aqui?'

    def despedida(self):
        return "Tchau... vou sentir saudades :'("
