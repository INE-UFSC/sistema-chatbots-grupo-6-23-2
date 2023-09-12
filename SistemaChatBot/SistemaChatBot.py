from Bots.Bot import Bot

class SistemaChatBot:

    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []

        for obj in lista_bots:
            if isinstance(obj, Bot):
                self.__lista_bots.append(obj)
        self.__bot = None
    
    def boas_vindas(self):
        print(f"Seja bem vindo ao Sistema de chatbots da {self.empresa}")
    
    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def lista_bots(self):
        return self.__lista_bots

    @lista_bots.setter
    def lista_bots(self, lista_bots):
        self.__lista_bots = lista_bots

    @property
    def bot(self):
        return self.__bot
    
    @bot.setter
    def bot(self, bot: Bot):
        if isinstance(bot, Bot):
            self.__bot = bot

    def mostra_menu(self):
        print("------- ESCOLHA O BOT -------")
        for i, bot in enumerate(self.lista_bots):
            print(f"{i} - Bot: {bot.nome} | Mensagem de apresentação: {bot.apresentacao()}")
    
    def escolhe_bot(self):
        self.bot = self.lista_bots[int(input("ESCOLHA: "))]

    def mostra_comandos_bot(self):
        self.bot.mostra_comandos()

    def le_envia_comando(self):
        escolha = int(input("Comando desejado: "))
        if self.bot.executa_comando(escolha):
            return True

    def inicio(self):
        self.boas_vindas() ##mostra mensagem de boas-vindas do sistema
        self.mostra_menu() ##mostra o menu ao usuário
        self.escolhe_bot() ##escolha do bot      
        self.bot.boas_vindas() ##mostra mensagens de boas-vindas do bot escolhido

        while(True): #entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
            self.mostra_comandos_bot()
            if self.le_envia_comando() == True:
                break
        self.bot.despedida() #ao sair mostrar a mensagem de despedida do bot