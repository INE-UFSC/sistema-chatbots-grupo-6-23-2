#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotIA import BotIA
from Bots.BotApaixonado import BotApaixonado

###construa a lista de bots disponíveis aqui
lista_bots = [BotIA('Igor Amaral'), BotApaixonado('Ricardo Nascimento')]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
