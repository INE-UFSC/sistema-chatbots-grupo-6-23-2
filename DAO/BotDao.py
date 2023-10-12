from Bots.BotTexto import BotTexto
from DAO.Dao import Dao
from Bots.Bot import Bot
from Bots.ComandoTexto import ComandoTexto

class BotDao(Dao):
    def __init__(self, datasource="bots.json"):
        super().__init__(datasource)

    def add(self, key, bot: Bot):
        if isinstance(bot, Bot):
            self.objectCache[str(key)] = bot.to_dict()
            self.dump()

    def get(self, key):
        try:
            bot_dict = self.objectCache.get(str(key))
            print(self.objectCache)
            bot = BotTexto(bot_dict['nome'], str(bot_dict['apresentacao']), str(bot_dict['boas_vindas']), str(bot_dict['despedida']))
            for comando in bot_dict['comandos'].values():
                cmd = ComandoTexto(comando['id'], comando['mensagem'])
                for resposta in comando['respostas']:
                    cmd.add_resposta(resposta)
                bot.add_comando(cmd)
            return bot
        except KeyError as e:
            raise InvalidJsonBotError(str(e))

    def remove(self, key):
        if key in self.objectCache:
            del self.objectCache[str(key)]
            self.dump()

    def get_all(self):
        bots = []
        for key in self.objectCache.keys():
            bots.append(self.get(key))
        return bots
    
class InvalidJsonBotError(KeyError):
    def __init__(self, message="Arquivo json inválido para adicionar um novo bot"):
        self.message = f"{message}"
        super().__init__(self.message)
