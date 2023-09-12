#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotNews import BotNews
from Bots.BotApaixonado import BotApaixonado
from Bots.BotAmigavel import BotAmigavel
from Bots.BotFitness import BotFitness

###construa a lista de bots disponíveis aqui
lista_bots = [BotNews('Bernardo Nogueira'), BotApaixonado('Ricardo Nascimento'), BotAmigavel("Grupo05"), BotFitness("Grupo04")] 

sys = scb.SistemaChatBot("BotLand", lista_bots)
sys.inicio()
