arq = open("aequalb.txt", 'r')
testread = arq.readlines()

transicoes = []
for i in range(7,len(testread)):
    transicoes.append(testread[i].split())