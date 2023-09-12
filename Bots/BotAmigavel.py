from Bots.Bot import Bot

class BotAmigavel(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = {
            1: {
                'comando': 'Bom dia',
                'resposta': 'Bom dia, como você está? '
            },
            2: {
                'comando': 'Conte me uma piada',
                'resposta': 'Por que o esqueleto não briga com ninguém? \nPorque ele não tem saco!'
            },
            3: {
                'comando': 'Quero um conselho',
                'resposta': 'Pegue e se cuide! Ande pela sombra sempre.'
            }
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print(f'-> Olá, sou o {self.__nome}! Fico feliz em conhecê-lo!')
 
    def mostra_comandos(self):
        for i in self.__comandos:
            comando = self.__comandos[i]['comando']
            print(f'{i} - {comando}')
            
    def executa_comando(self, cmd):
        print(self.__comandos[cmd]['resposta'])

    def boas_vindas(self):
        print(f'-> {self.__nome} diz: Obrigado por ter me escolhido. Espero que sejamos bons amigos.')

    def despedida(self):
        print('Pena que já acabou...')