import Chaves

def get_key(val): #Pegar o item do dicionário e transformar em número
    for key, value in Chaves.dicio.items():
        if val == value:
            return key
    return "key doesn't exist"

def transf_num(mensagem): #Pega a mensagem e trasnforma ela em números
    mensagem_sep=[]
    for i in range(len(mensagem)): #Roda pela mensagem
        mensagem_sep.append(mensagem[i]) #Adiciona a mensagem em numeros em uma blocos
    msg_encriptada=""
    for i in ((mensagem_sep)):
        msg_encriptada+=(str(get_key(i))) #transforma esses números em strings
    return msg_encriptada

def sep_blocos(msg_encriptada): #Separa a mensagem trasnformada em numeros para blocos para por ser codificada
    blocos=[]
    bloco=""
    blocoaux=""
    for i in range(len(msg_encriptada)): #Pega a mensagem transformada em número
        bloco+=msg_encriptada[i] #Adiciona caracter por caracter no bloco
        if(int(bloco)>=Chaves.n):#quando esse bloco for maior que o "n",separa ele
            for j in range(len(bloco)-1):   blocoaux+=bloco[j] #diminui o bloco de um para ficar menor que "n"
            if(bloco[0]=='0'): blocos.append('0') #Caso o bloco inicie com 0, isola o 0  
            blocos.append(blocoaux) #Coloca o bloco na mensagem
            blocoaux='' #Reinicia a variavel auxiliar
            bloco=bloco[-1] #Põe a variavel tirada antes no começo do outro bloco
    if(bloco!=""): #Se tiver algum numero que nao foi posto quando terminou o loop, coloca ele ao final
        bloco=blocoaux+bloco
        blocos.append(bloco)
    return blocos

def codificando(pedaço): #Codificando a mensagem
    return (pow(int(pedaço),Chaves.e,Chaves.n))

blocos=[]
msg_encriptada=[]
mensagem=input("Insira a mensagem a ser encriptada: ")
msg_numerada=transf_num(mensagem)
blocos=sep_blocos(msg_numerada)
for i in range(len(blocos)):
    msg_encriptada.append(codificando(blocos[i]))