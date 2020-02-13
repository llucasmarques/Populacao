import numpy as np
from random import *

#Funcao pra gerar a nova populacao
def nova_popula(qtd_individuos):
	crossover = int(0.6 * qtd_individuos)
	individuo_selecionado = np.zeros(crossover)
	
	
	#Seleciona os individuos para reproducao
	for i in range(qtd_individuos):
		individuo_selecionado[i] = roleta(valor_funcao,avaliacao)
		
	
	#Cruza os individuos selecionados a partir do crossover selecionado 
		
	
	
	#Executa a mutacao em um individuo
	
	
	
	#Ponto de aceitacao, coloca a nova descendencia 
	
	
	
#Funcao f(x)
def funcao_x():
	_funcao = x*x - 3*x +4
	return _funcao

	
	
#Funcao que realiza a mutacao
def mutacao(indice, individuos):	
	#Gera um numero randomico para mudar o numero do codigo genetico nesta posicao
	num_random = randint(0, 23)
	
	#Se for 0 vira 1
	if(individuos[indice][num_random] == 0)
		individuos[indice][num_random] = 1
	#Se for 1 vira 0
	else
		individuos[indice][num_random] = 0
	
	
#Funcao de selecao ROLETA
#[Soma] Calcule a soma dos valores de adequação de todos os cromossomas da população - soma S. 
#[Seleção] Gere um número aleatório no intervalo (0,S) - r. 
#[Repetição] Percorra toda a população e some a adequação de 0 - soma s. Quando a soma s for maior que r, pare e retorne o cromossoma atual. 
def roleta():
	soma_peso = 0
	
	for i in range(qtd_individuos):
		soma_peso = soma_peso + peso[i]
		

	sorteio = randint(0, soma_peso)
	posicao_escolhida = 0
	sorteio= sorteio - peso[posicao_escolhida]
	
	
	#aqui mapeamos a posição escolhida, vamos decrescendo do sorteio os pesos de cada posição. No momento em que o sorteio for zerado ou for negativo, 
	#significa que encontramos a nossa posição que queremos.
	while(sorteio>0):  
		posicao_escolhida = posicao_escolhida + 1
		sorteio= sorteio - peso[posicao_escolhida]
	
	
#Funcao para converter o numero binario para decimal
def converteDec(indiv,qtd,dec,sinal):
	pos = 0
	for i in range(qtd):
		cont = 0
		soma = 0
		for j in range(24):
			resto = j%4
			resto = 3-resto 
			
			if resto == 0:
				if pos > 9:
					pos = 9.0
				#print pos
				soma = soma + pos/10**cont
				pos = indiv[i][j] * (2**resto)
				cont = cont + 1
				
			else:
				pos = pos + indiv[i][j] * (2**resto)
		if i<len(sinal) :
			if  sinal[i] == 1.0:
				soma = soma * -1
		
		dec[i] = soma

		
#Maximo e minimos assumidos
x_max = 10
x_min = -10
#Variaveis auxiliares
probabilidade_mutacao = 0.10
numero_de_geracoes = 20

#Main
def main():
	qtd_individuos = int(raw_input('Entre com a quantidade de individuos: '))
	#Taxa de crossover
	crossover = int(0.6 * qtd_individuos)
	indiv_dec = np.zeros(qtd_individuos)
	individuos = np.zeros((qtd_individuos + crossover,24))
	sinais = np.zeros(qtd_individuos)

	for i in range(qtd_individuos):
		sinais[i] = randint(0,1)
		for j in range(24):
			valor = randint(0,1)
			individuos[i][j] = valor
			
			
	converteDec(individuos,qtd_individuos,indiv_dec,sinais)
	print individuos
	print indiv_dec
	
main()

	
#Ploting
#Ploting  Function
x = arange(x_min,x_max,0.01)
y = x_function(x)
#figure(1)
plot(x,y)
xlabel('x')
ylabel('F(x)')
title(r'$F(x)$')

#Ploting data for last generation
figure(2)
plot(gen_2_xvalues,gen_2_fvalues, 'bo')
xlabel('x')
ylabel('F(x)')
title(r'Dados da ultima geracao')

#Ploting data for maximum values for each generation
figure(3)
plot(range(number_of_generations),generations_f, 'ro')
xlabel('Geracoes')
ylabel('F(x) Maximo')
title(r'$F(x)$')
show()
