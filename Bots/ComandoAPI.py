from Bots.Comando import Comando
import requests


class ComandoAPI(Comando):
    def __init__(self, id: int, mensagem: str) -> None:
        super().__init__(id, mensagem)

    def retorno(self, *keywords: str):
        palavras = ""
        for keyword in keywords:
            palavras = f"{palavras} {keyword}"
        return self.get_news_API(palavras)

    def get_news_API(self, palavras: str):
        url = f"https://newsapi.org/v2/everything?language=pt&pageSize=3&q={palavras}&apiKey=e6f66d10a1ac4f669f92e6e447fe58f9"
        response = requests.get(url).json()
        if response["status"] == "ok":
            i = 0
            retorno = {}
            for noticia in response["articles"]:
                retorno[i] = {
                    'titulo': noticia["title"],
                    'fonte': noticia["url"],
                    'descricao': noticia["description"],
                    'imagem': noticia["urlToImage"],
                    'data': noticia['publishedAt']
                }
                i += 1
            return retorno
        else:
            raise APIConnectionError("Falha na conexão com a News API. Tente mais tarde.")

class APIConnectionError(Exception):
    def __init__(self, message="Erro de conexão com a API"):
        self.message = message
        super().__init__(self.message)