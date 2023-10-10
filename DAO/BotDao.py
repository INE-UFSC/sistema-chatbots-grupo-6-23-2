import Dao
from Bots.Bot import Bot

class BotDao(Dao):
    def __init__(self, datasource="bots.json"):
        super().__init__(datasource)

    def add(self, key, bot: Bot):
        if isinstance(bot, Bot):
            self.objectCache[key] = bot.to_dict()
            self.dump()

    def get(self, key):
        return self.objectCache.get(key)

    def remove(self, key):
        if key in self.objectCache:
            del self.objectCache[key]
            self.dump()

    def get_all(self):
        return list(self.objectCache.values())