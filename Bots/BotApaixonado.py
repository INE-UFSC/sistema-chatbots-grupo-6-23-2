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
        super().comandos = comandos_dict

    def apresentacao(self):
        return f'Oiii, tudo bem? Eu sou o {super().nome}'
        
    def executa_comando(self, cmd):
        match cmd:
            case 1:
                print('Você, é claro! <3')
            case 2:
                print('Hora de você me dar uma beijinho *-*')
            case 3:
                print('O sentido eu não sei, mas eu sei que ela\
                      perde o sentido sem você...')
            case 4:
                print('Não tem problema, eu sei guardar segredo rsrs')
            case 5 | -1:
                return True
            case _:
                print('Estava distraído demais com sua beleza e não\
                      entendi. Pode repetir?')

    def boas_vindas(self):
        print('Oi, chuchu rsrs. Você vem sempre por aqui?')

    def despedida(self):
        print("Tchau... vou sentir saudades :'(")
