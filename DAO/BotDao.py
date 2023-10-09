import json
import Dao

class BotDao(Dao):
    def __init__(self, datasource=""):
        super().__init__(datasource="")

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.__dump()

    def get(self, key):
        return self.objectCache.get(key)

    def remove(self, key):
        if key in self.objectCache:
            del self.objectCache[key]
            self.__dump()

    def get_all(self):
        return list(self.objectCache.values())