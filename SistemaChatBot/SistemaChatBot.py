from Bots.Bot import Bot
from Bots.BotNews import BotNews

class SistemaChatBot:

    def __init__(self, nomeEmpresa):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.__selected_bot = None
    
    def boas_vindas(self):
        return f"Seja bem vindo ao Sistema de chatbots da {self.empresa}"
    
    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def lista_bots(self):
        return self.__lista_bots

    @property
    def selected_bot(self):
        return self.__selected_bot
    
    def add_bot(self, bot: Bot):
        if isinstance(bot, Bot):
            self.lista_bots.append(bot)

    def remove_bot(self, index):
        try:
            del self.lista_bots[index]
        except:
            raise InvalidBotError()
    
    def escolhe_bot(self, escolha: int):
        try:
            self.__selected_bot = self.lista_bots[int(escolha)]
        except:
            raise InvalidBotError()
        
    def deselect_bot(self):
        self.__selected_bot = None

    def le_envia_comando(self, cmd: str):
        if isinstance(self.selected_bot, BotNews): # Caso seja alterado no futuro para qualquer bot api devemos mudar aqui
            return self.selected_bot.executa_comando(1, *str(cmd).split(" "))
        elif isinstance(self.selected_bot, Bot):
            try:
                cmd = int(cmd)
                return self.selected_bot.executa_comando(cmd)
            except TypeError:
                raise TypeError("O comando para este bot deve ser do tipo numérico!")

class InvalidBotError(KeyError):
    def __init__(self, comando, message="Bot inválido!"):
        self.comando = comando
        self.message = f"{message}: {comando}"
        super().__init__(self.message)