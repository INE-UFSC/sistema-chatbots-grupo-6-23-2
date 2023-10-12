from Bots.Bot import Bot
from Bots.ComandoTexto import ComandoTexto


class BotTexto(Bot):

    def __init__(self, nome, apresentacao, boas_vindas, despedida):
        super().__init__(nome)
        if isinstance(apresentacao, str) and isinstance(boas_vindas, str) and isinstance(despedida, str):
            self.__apresentacao = apresentacao
            self.__boas_vindas = boas_vindas
            self.__despedida = despedida
        else:
            raise ValueError("Todos os parâmetros do BotTexto devem ser do tipo str.")

    def apresentacao(self):
        return self.__apresentacao

    def boas_vindas(self):
        return self.__boas_vindas

    def despedida(self):
        return self.__despedida
    
    def to_dict(self):
        bot_dict = {"nome": super().nome, "comandos": {}, "apresentacao": self.apresentacao(), "boas_vindas": self.boas_vindas(), "despedida": self.despedida()}
        for cmd_id, cmd_obj in super().comandos.items():
            if isinstance(cmd_obj, ComandoTexto):
                cmd_dict = {
                    "id": cmd_obj.id,
                    "mensagem": cmd_obj.mensagem,
                    "respostas": cmd_obj.respostas,
                }
                bot_dict["comandos"][cmd_id] = cmd_dict
        return bot_dict
