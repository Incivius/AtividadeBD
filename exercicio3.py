populacaoA = 15000
populacaoA1 = 15000
populacaoB = 45000
populacaoC = 65000

taxaA = 0.1
taxaB = 0.05
taxaC = 0.025
anosAB = 0
anosAC = 0

while populacaoA <= populacaoB:
    populacaoA = (populacaoA * taxaA) + populacaoA
    populacaoB = (populacaoB * taxaB) + populacaoB
    anosAB += 1

while populacaoA1 <= populacaoC + (populacaoC*23)/100:
    populacaoA1 = (populacaoA1 * taxaA) + populacaoA1
    populacaoC = (populacaoC * taxaC) + populacaoC
    anosAC += 1


print (f"Levará cerca de {anosAB} anos para que a população de A se iguale a ou ultrapasse a população B e" f"\n cerca de {anosAC} para que a população A ultrapasse a população C  em 23%")
