import time
import math
import Gerador
import random
# 0 é composto e 1 é primo
def Miller_Robin(num,base): #Teste de composição
    x=num-1
    i=0
    while(x%2==0): 
        x=x/2
        i+=1

    for j in range(i):
        resto=pow(base,2**j*int(x),num)
        if (j==0 and resto==1 or j==0 and resto==num-1): return 1
        elif(j!=0 and resto==num-1): return 1
    return 0
        
def Test_comp(num): #Testa a composição de um número para várias bases
    if (Miller_Robin(num,2)==1):
        if (Miller_Robin(num,3)==1):
            if(Miller_Robin(num,5)==1):
                if(Miller_Robin(num,7)==1):
                    if(Miller_Robin(num,11)==1):
                        return 1
                    else: return 0
                else: return 0
            else: return 0
        else: return 0
    else: return 0
    

def alg_lixo(num): #Algoritmo de fatoração super básico
    for i in range(3,int(math.sqrt(num))+1,2):
        if(num%i==0): return 0
    else: return 1

def seleciona(candidatos): # Seleciona os candidatos que falharam no teste de composição pra irem pro algoritmo super ineficiente
    selecionados=[]
    for i in (range(1,len(candidatos),2)):

        if(str(candidatos[i])[-1]=='5'): continue

        elif (Test_comp(candidatos[i])==1): selecionados.append(candidatos[i])

    return selecionados

def teste_definitivo(selecionados): #Passa os selecionados no pente fino no algoritmo horrivel
    primos=[]
    for i in selecionados:
        if (alg_lixo(i)==1): primos.append(i)
    return primos

def Verifica(Lista):
    primos=[]
    primos=seleciona(Lista)
    
    return primos

TI=time.perf_counter()
p=[]
q=[]
p=Verifica(Gerador.lista1)
q=Verifica(Gerador.lista2)
TF=time.perf_counter()
print((p))
print()
print((q))
print("Tempo de execução:",TF-TI,"segundos")