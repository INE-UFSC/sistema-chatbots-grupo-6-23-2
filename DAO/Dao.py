import json
from abc import ABC, abstractclassmethod

class Dao(ABC):
    def __init__(self, datasource=""):
        self.datasource = datasource
        self.objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.dump()

    def dump(self):
        with open(self.datasource, "w") as arquivo:
            json.dump(self.objectCache, arquivo)
    
    def __load(self):
        with open("datasource.json") as arquivo:
            self.objectCache = json.load(self.datasource)

    @abstractclassmethod
    def add(self, key, obj):
        pass

    @abstractclassmethod
    def get(self, key):
        pass

    @abstractclassmethod
    def remove(self, key):
        pass

    @abstractclassmethod
    def get_all(self):
        pass