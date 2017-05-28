def insere(op):
    tsl = []
    for i in range(len(op)):
        tsl.append(op[i])

    tsl.reverse()
    return tsl

ts = "GOLOM"
pilha = []
pilha = insere(ts)
print pilha