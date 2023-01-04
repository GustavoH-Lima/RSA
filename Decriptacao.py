import Encriptar
import Chaves
import os

def decriptar(pedaço): #decodifica e mensagem encriptada
    return pow(int(pedaço),Chaves.d,Chaves.n)

def junta(msg_descriptada):#Junta a mensagem em uma string
    mensagem=""
    for i in msg_descriptada:
        mensagem+=str(i)
    return mensagem

def decodificar(mensagem): #Pega o dicionario e transforma na mensagem final
    letra=''
    final=''
    for i in range(len(mensagem)):
        letra+=mensagem[i]
        if (i%Chaves.tam_letras==Chaves.tam_letras-1):
            final+=Encriptar.Chaves.dicio[int(letra)]
            letra=''
    return final


    
msg_descriptada=[]
for i in (Encriptar.msg_encriptada):
    msg_descriptada.append(decriptar(i))

os.system('cls')
print("")
print("Blocos criados:",Encriptar.blocos)
print("Blocos codificados:",Encriptar.msg_encriptada)
print("Blocos decodificados:",msg_descriptada)
mensagem=junta(msg_descriptada)
print("Mensagem junta:",mensagem)
final=(decodificar(mensagem))
print("Mensagem final:",final)