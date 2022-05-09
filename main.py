import math
import numpy as np
import copy
import random as rd


def create_data_model():
    data = {}
    data["matriz_distancia"] = [
        [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],     #0
        [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],  #1
        [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754], #2    
        [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],  #3 
        [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],  #4
        [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],    #5
        [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],   #6
        [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],     #7
        [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],    #8
        [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],     #9
        [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354], #10    
        [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],   #11
        [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],    #12
        [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],    #13
        [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],  #14
        [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],#15    
        [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],  #16
    ]
    data["num_vehicles"] = 4
    data["depot"] = 0
    return data
 

def calcDist(matriz_distancia, inicio, destino):
  
    return matriz_distancia[inicio][destino]


def mutacao(populacao):
  
    qtd = math.ceil(tx_mutacao * len(populacao))
    
    popEscolhida = rd.choices(populacao, k=qtd)

    populacao_mutacao = []
    
    for individuo in popEscolhida:
        mutacao = str(rd.choices(["shuffle", "swap"])[0])
      
        if mutacao == "shuffle":
            populacao_mutacao.append(mutacao_shuffle(individuo))
        
    return populacao_mutacao

def crossover(populacao):
    funcao_decaimento_crossover = math.exp(-geracao / 200)
  
    qtd = funcao_decaimento_crossover * tx_crossover * len(populacao)
  
    popEscolhida = copy.deepcopy(populacao)
  
    popEscolhida = rd.choices(popEscolhida, k=math.ceil(qtd))
  
    
    for i in range(len(popEscolhida)-1):
        swap = popEscolhida[i][1]
        antigo = swap
      
        popEscolhida[i]= [popEscolhida[i][0], popEscolhida[i+1][2], popEscolhida[i][2], popEscolhida[i][3]]
      
        popEscolhida[i] = limpar(popEscolhida[i],  popEscolhida[i+1][2], antigo,1)
      
        antigo = popEscolhida[i+1][2]
      
        popEscolhida[i+1] = [popEscolhida[i+1][0] , popEscolhida[i+1][1], swap, popEscolhida[i+1][3]]
      
        popEscolhida[i+1] = limpar(popEscolhida[i+1],  swap, antigo,2)

    
    for individuo in popEscolhida:
      
        formacaoRotas(minValor, maxValor, individuo)
      
        microsMacros(individuo)
      
        minValor.clear()
        maxValor.clear()
      
        
    return popEscolhida




def formacaoRotas(iMenor,iMaior, i):
  
    if not iMenor or not iMaior:
        return
    
    menor = rd.choice(iMenor)
  
    iMenor.remove(menor)

    if len(iMaior) == 1:
        maior = rd.choice(iMaior)
      
    else:
        maior = rd.choice(iMaior)
        iMaior.remove(maior)
        
    while len(i[maior]) == 4:
      
        maior = rd.choice(iMaior)
      
        iMaior.remove(maior)

    while len(i[menor]) < 4:
        nMaior = rd.choice(i[maior])
      
        i[maior].remove(nMaior)
      
        i[menor].append(nMaior)
      
def fitness(individuo):
  
    totalzada = 0
  
    score = 0
  
    scoreVan = []
  
    j = 0
  
    for caminho_van in individuo:
        for i in range(len(caminho_van) - 1):
            score += calcDist(data["matriz_distancia"], caminho_van[i], caminho_van[i+1])
          
        totalzada += score      
        scoreVan.append(f'{score}{j}')     
        score = 0
        j += 1
      
    scoreVan.sort()
    melhores_vans = []

    for vans in scoreVan:
        melhores_vans.append(individuo[int(vans[-1])])
      
    individuo = melhores_vans
    return totalzada


def microsMacros(lista):
    for i,val in enumerate(lista):
        removeZeros(val)
      
        if len(val) < 4:
            minValor.append(i)
          
        elif len(val) == 4:
            continue
          
        else:
            maxValor.append(i)

# Funcoes dos algoritmos 

#Inicializando valores

minValor = []
maxValor = []


def mutacao_shuffle(individuo):
  
    novoIndividuo = []
  
    caminhoVan = []
  
    caminho = []
  
    for van in individuo:
        for i in van:
            if i != 0:
                caminho.append(i)
              
        caminhoVan.append(caminho) 
        caminho = []

    for i,ca in enumerate(caminhoVan):
      
        rd.shuffle(ca)
      
        ca.insert(0,0)
      
        ca.append(0)
      
        novoIndividuo.append(ca)
      
    return novoIndividuo

def tiraZeroMatriz(individuo):
    for lista in individuo:
      
        if lista[0] == 0:
            lista.pop(0)
          
        if lista[-1] == 0:
            lista.pop(-1)
      
def removeZeros(lista):
    if not lista:
        return
      
    if lista[0] == 0:
        lista.pop(0)
      
    if lista[-1] == 0:
        lista.pop(-1)
  
def colocaZero(individuo):
  for lista in individuo:
    
    if lista[0] != 0:  
      lista.insert(0,0)
      
    if lista[-1] != 0:
      lista.append(0)
      
  return individuo


def comparador(lista, numero):
    return True if numero in lista else False

def limpar(individuo, troca, antigo,index):
    removeZeros(troca)
  
    nao_entre = 0
  
    antigo_copia = copy.deepcopy(antigo)
  
    antigo_copia.insert(0,0)
  
    troca = list(set(np.append(troca, antigo_copia)))
  
    individuo[index] = troca
  
    novoIndividuo = []
  
    novo_el = []
    
    for el in individuo:
        if(nao_entre !=index):
            for i in el:
              
                if not comparador(troca, i):
                    novo_el.append(i)
                  
            contexto = copy.deepcopy(novo_el)
          
            novoIndividuo.append(contexto)
          
            novo_el.clear()
            
        nao_entre += 1
        
    novoIndividuo.insert(index, troca)
    troca.append(0)
  
    individuo = novoIndividuo
  
    return individuo
  
def criaIndividuo(data):
  
  cidades = len(data['matriz_distancia'][0])
  
  liberados = list(range(1, cidades))
  
  escolha = []
  
  cidades_por_van = int(cidades/data['num_vehicles'])
  
  added = 0
  
  choice = []

  while len(liberados) > 0:
    num = rd.randint(0, len(liberados) -1)
    
    if added ==  cidades_por_van:
      choice.insert(0,0)
      
      choice.append(0)
      
      escolha.append(choice)
      
      choice = []
      
      added = 0
      
    else:
      added += 1
      
      choice.append(liberados[num])
      
      liberados.pop(num)
      
      if len(liberados) == 0:
        
        choice.insert(0,0)
        
        choice.append(0)
        
        escolha.append(choice)

  return escolha


def selecao_tragedia(populacao, geracao):
  
    if (geracao % geracoes_tragedia == 0):
        tamanho_tragedia = math.ceil(tamanho_populacao*tx_tragedia)
        novos_individuos = [criaIndividuo(data) for _ in range(
            0, tamanho_populacao - tamanho_tragedia)]
      
        return sorted(populacao[0:tamanho_tragedia] + novos_individuos, key=fitness)
      
    else:
        nova_populacao = sorted(populacao, key=fitness)
      
        return nova_populacao[0:tamanho_populacao]

# hiperparâmetros
tamanho_populacao = 100
tx_mutacao = 0.50
tx_crossover = 0.15
tx_tragedia = 0.05
geracoes_max = 20
geracoes_tragedia = 100
geracao = 0

data = create_data_model()

populacao = [criaIndividuo(data) for a in range(0, tamanho_populacao)]

populacao = sorted(populacao, key=fitness)








while geracao < geracoes_max:
  
    geracao += 1
    populacao_crossover = crossover(populacao)
   
  #OUTPUT
melhor_individuo = populacao[0]
for index, caminho_van in enumerate(melhor_individuo):
  
    print(f'Van {index + 1}')
    caminho_sem_deposito = [str(numero) for numero in caminho_van]
    caminho_sem_deposito = caminho_sem_deposito[1:len(caminho_sem_deposito)-1]
    print(' -> '.join(caminho_sem_deposito),end='\n\n')

print("Distância percorrida com todas as vans: " + str(fitness(populacao[0])))
