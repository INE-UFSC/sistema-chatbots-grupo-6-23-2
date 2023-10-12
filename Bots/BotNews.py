from Bots.Bot import Bot
from Bots.ComandoAPI import ComandoAPI

class BotNews(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        super().add_comando(ComandoAPI(1, "Veja as últimas notícias buscando-as por palavra chave!"))

    def apresentacao(self):
        return f"Olá, eu sou {super().nome}, um bot de notícias! :)"
    
    def boas_vindas(self):
        return f"Bem vindo ao meu canal de notícias!"

    def despedida(self):
        return f"Até mais, obrigado pelo interesse!"