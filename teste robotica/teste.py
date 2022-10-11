import numpy as np
import aula as au

vet = au.cria_vetor3([5,3,4])
au.checa_vetor3(vet)
matriz = au.matriz_rotacao_x(0.30*180/4)
operador = au.cria_operador4(matriz,vet)
print ("Matriz de rotação: \n",matriz)
print ("Matriz de rotação mista: \n",operador)

vet2= au.cria_vetor3([6,5,12])
au.checa_vetor3(vet2)
matriz2 = au.matriz_rotacao_x(0.60*180/4)
operador2 = au.cria_operador4(matriz2,vet2)
print ("Matriz de rotação: \n",matriz2)
print ("Matriz de rotação mista: \n",operador2)

vet3= au.cria_vetor3([6,5])
au.checa_vetor3(vet3)
matriz3 = au.matriz_rotacao_x(0.60*180/4)
operador3 = au.cria_operador4(matriz3,vet3)
print ("Matriz de rotação: \n",matriz3)
print ("Matriz de rotação mista: \n",operador3)