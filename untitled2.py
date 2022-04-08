# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DNyynWulGn2CZiq3IDbqUCbHZ75YY_8o
"""

'''import numpy as np
entradas = np.array( [ [0,0],
                       [0,1],
                       [1,0],
                       [1,1] ] ) 
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
  if (soma >= 1) :
    return 1
  return 0

def calculaSaida(registro):
  s = registro.dot(pesos)
  return stepFunction(s)

def treinar():
  erroTotal = 1
  while(erroTotal != 0):
    erroTotal = 0
    for i in range(len(saidas)):
      saidaCalculada = calculaSaida(np.asarray(entradas[i]))
      erro = saidas[i] - saidaCalculada
      erroTotal += erro
      for j in range(len(pesos)):
        pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
        print('Peso atualizado: ' + str(pesos[j]))
      print('Total de erros: ' + str(erroTotal))

treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))'''

pip install /home/pybrain-0.3.3.zip

pip install sklearn

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

rede = buildNetwork(2,3,1, hiddenclass = SigmoidLayer, bias = False,)#outclass = Softmaxlayer

print(rede['in'])

print(rede['hidden0'])

print(rede['out'])

print(rede['bias'])

dados = SupervisedDataSet(2,1)
dados.addSample((0,0), (0))
dados.addSample((0,1), (1))
dados.addSample((1,0), (1))
dados.addSample((1,1), (0))

print(dados['input'])

dados['target']

treinamento = BackpropTrainer(rede, dataset=dados, learningrate=0.01, momentum=0.06)

erro = 0
for i in range(50000):
  erro = treinamento.train()
  #if i % 1000 == 0:
    #print("Erro: ", erro)
print("Erro: ", erro)

val1 = rede.activate([0,0])
val1 = round(val1[0])
print(val1)

val2 = rede.activate([0,1])
val2 = round(val2[0])
print(val2)

val3 = rede.activate([1,0])
val3 = round(val3[0])
print(val3)

val4 = rede.activate([0,0])
val4 = round(val4[0])
print(val4)