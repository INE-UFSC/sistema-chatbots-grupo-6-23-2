from Bots.Bot import Bot
from Bots.BotNews import BotNews
from DAO.BotDao import BotDao, InvalidJsonBotError

class SistemaChatBot:

    def __init__(self, nomeEmpresa):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.__selected_bot = None
        self.__data = BotDao()
        self.add_bot(BotNews("Bernardo Nogueira"))
        self.load_bot_texto()
    
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
    
    def load_bot_texto(self):
        for bot in self.__data.get_all():
            self.add_bot(bot)
    
    def add_bot(self, bot: Bot):
        if isinstance(bot, Bot):
            self.lista_bots.append(bot)
    
    def add_bot_file(self, filesource: str):
        try:
            dao_aux = BotDao(filesource)
            bots = dao_aux.get_all()
            for bot in bots:
                self.add_bot(bot)
                key = len(self.__lista_bots) - 1
                self.__data.add(key, bot)
        except FileNotFoundError:
            raise FileNotFoundError("O caminho do arquivo é inválido")


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
            except ValueError:
                raise TypeError("O comando para este bot deve ser do tipo numérico!")

class InvalidBotError(KeyError):
    def __init__(self, message="Bot inválido!"):
        self.message = f"{message}"
        super().__init__(self.message)