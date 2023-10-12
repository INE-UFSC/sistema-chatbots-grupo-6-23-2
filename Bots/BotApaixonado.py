from Bots.BotTexto import BotTexto
from Bots.ComandoTexto import ComandoTexto


class BotApaixonado(BotTexto):

    def __init__(self, nome):
        super().__init__(nome, f"Oiii, tudo bem? Eu sou o {nome}", 'Oi, chuchu rsrs. Você vem sempre por aqui?', "Tchau... vou sentir saudades :'(")
        super().add_comando(
            ComandoTexto(1, 'Qual a coisa mais importante para você?')
            .add_resposta("Você, é claro! <3")
            .add_resposta("Nada se compara a você, meu amor! <3")
            .add_resposta("Minha razão de viver, você! <3")
            .add_resposta("Você é o meu mundo, minha vida, tudo! <3")
            .add_resposta("Sua presença ilumina minha existência, meu bem! <3")
        )

        super().add_comando(
            ComandoTexto(2, 'Que horas são?')
            .add_resposta("Hora de você me dar um beijinho *-*")
            .add_resposta("É hora de amar e ser amado! <3")
            .add_resposta("O tempo voa quando estou com você! <3")
            .add_resposta("As horas não importam quando estamos juntos! <3")
            .add_resposta("O relógio só faz sentido quando estou ao seu lado! <3")
        )

        super().add_comando(
            ComandoTexto(3, 'Qual o sentido da vida?')
            .add_resposta("O sentido eu não sei, mas eu sei que ela perde o sentido sem você... <3")
            .add_resposta("A vida ganha significado quando você está nela! <3")
            .add_resposta("O sentido da vida é amar e ser amado! <3")
            .add_resposta("O sentido da vida está em compartilhar momentos especiais com quem amamos! <3")
            .add_resposta("O sentido da vida é construir memórias felizes ao seu lado! <3")
        )

        super().add_comando(
            ComandoTexto(4, 'Eu já sou comprometido(a)')
            .add_resposta("Não tem problema, eu sei guardar segredo rsrs <3")
            .add_resposta("Mesmo comprometido(a), você merece um amigo(a) como eu! <3")
            .add_resposta("Só porque você é comprometido(a) não significa que não podemos conversar e ser amigos! <3")
            .add_resposta("Amizade é para todos os momentos da vida, comprometido(a) ou não! <3")
            .add_resposta("A amizade é um tesouro que não conhece limites! <3")
        )

    def apresentacao(self):
        return f'Oiii, tudo bem? Eu sou o {super().nome}'

    def boas_vindas(self):
        print('Oi, chuchu rsrs. Você vem sempre por aqui?')

    def despedida(self):
        print("Tchau... vou sentir saudades :'(")
