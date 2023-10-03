from Bots.Bot import Bot
from Bots.ComandoAPI import ComandoAPI

class BotNews(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        super().add_comando(ComandoAPI(1, "Veja as últimas notícias buscando-as por palavra chave!"))

    def apresentacao(self):
        return 'Oi, sou o BotNews!'
    
    def boas_vindas(self):
        print(f"Olá, eu sou {super().nome}, um bot de notícias! :)")

    def despedida(self):
        print(f"Até mais, obrigado pelo interesse!")