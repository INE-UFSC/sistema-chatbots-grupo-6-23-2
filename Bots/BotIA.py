from Bots.Bot import Bot

class BotIA(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        super().comandos = {1: "Perguntar qualquer coisa.", 2: "Sair"}

    def executa_comando(self,cmd):
        if cmd == 2:
            return True
        elif cmd == 1:
            pergunta = input("Qual é a sua pergunta: ")
            #conexão com a API de IA
        else:
            print("Comando não encontrado")

    def boas_vindas(self):
        print(f"Olá eu sou {super().nome} um bot com inteligência artificial! :)")

    def despedida(self):
        print(f"Até mais, obrigado pela conversa!")