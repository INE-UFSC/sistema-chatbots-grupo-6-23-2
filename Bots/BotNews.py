from Bots.Bot import Bot
import requests

class BotNews(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        super().comandos = {1: "Pergunte notícias por palavras chaves", 2: "Sair"}

    def executa_comando(self,cmd):
        if cmd == 2:
            return True
        elif cmd == 1:
            palavras = input("Digite as palavras chaves (separada por espaços): ").replace(" ", "+")
            url = f"https://newsapi.org/v2/everything?language=pt&pageSize=3&q={keyword}&apiKey=e6f66d10a1ac4f669f92e6e447fe58f9"

            response = requests.get(url).json()
            if response["status"] == "ok":
                i = 0
                for noticia in response["articles"]:
                    titulo = noticia["title"]
                    fonte = noticia["url"]
                    print(f"{i}: {titulo} - (disponível em: {fonte})")
                    i += 1
                noticia = response["articles"][int(input("Qual notícia você quer saber mais: "))]
                print(f'{noticia["title"]} ({noticia["url"]}):\n{noticia["content"]}')
            else:
                print("Problema interno, me desculpe! :(")
        else:
            print("Comando não encontrado")

    def boas_vindas(self):
        print(f"Olá, eu sou {super().nome}, um bot de notícias! :)")

    def despedida(self):
        print(f"Até mais, obrigado pelo interesse!")