#encoding: utf-8
from controlador.controlador import Controlador
from Bots.BotNews import BotNews
from Bots.BotApaixonado import BotApaixonado

###construa a lista de bots disponíveis aqui
lista_bots = [BotNews('Bernardo Nogueira'), BotApaixonado('Ricardo Nascimento')] 
nome_empresa = 'Botland'

sys = Controlador(nome_empresa, lista_bots)
