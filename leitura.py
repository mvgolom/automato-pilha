arq = open("aequalb.txt", 'r')
testread = arq.readlines()

alfabeto = testread[0].replace("\r\n","").split(" ")
alfaPilha = testread[1].strip().replace("\r\n","").split(" ")
epsilon = testread[2].replace("\r\n","").split(" ")
iniPilha = testread[3].replace("\r\n","")
estados = testread[4].replace("\r\n","").split()
estadoInicial = testread[5].replace("\r\n","").split()
estadoAccept = testread[6].replace("\r\n","").split()
transicoes = []
for i in range(7,len(testread)):
    transicoes.append(testread[i].split())





