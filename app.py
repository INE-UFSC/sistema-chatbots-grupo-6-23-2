#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotNews import BotNews
from Bots.BotApaixonado import BotApaixonado

###construa a lista de bots disponíveis aqui
lista_bots = [BotNews('Bernardo Nogueira'), BotApaixonado('Ricardo Nascimento')] 

sys = scb.SistemaChatBot("BotLand", lista_bots)
sys.inicio()
