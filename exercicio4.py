countSeq = 1
maiorSeq = 1
for i in range(4):
    n = int(input(f"Informe o {i+1}° numero:"))
    if  countSeq <= n:
        countSeq+=1
        if countSeq > maiorSeq:
            maiorSeq = countSeq + i

print('o tamanho da maior seq:',countSeq)
print('o tamanho da maior seq com criterio de desempate:',maiorSeq)