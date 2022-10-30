respostas = 0
primeiro_n = int(input('Qual será o primeiro número da sequencia? '))
cont = 1
cont1 = 0
soma = 0
soma1 = 0
total = 0
total2 = 0
soma2 = 0

while respostas < 15:
    sucessor = int(input('Qual o proximo número da sequancia?'))
    if sucessor == primeiro_n + 1:
        cont += 1
        if cont > cont1:
            cont1 = cont
            soma2 = primeiro_n + sucessor + total2
            total2 = soma2 - sucessor
            soma1 = soma2
            primeiro_n = sucessor
            respostas += 1
            print (sucessor)
            print (primeiro_n)
            print (cont)
            print (cont1)
            print (soma2)
            print (soma1)
        elif cont < cont1:
            soma2 = primeiro_n + sucessor + total2 
            total2 = soma2 - sucessor
            primeiro_n = sucessor
            respostas += 1
        elif cont == cont1:
            soma2 = primeiro_n + sucessor + total2
            total2 = soma2 - sucessor
            primeiro_n = sucessor
            respostas += 1
            if soma2 > soma1:
                soma1 = soma2
                cont1 = cont
                print (cont1)
                print (soma1)
    else:
        primeiro_n = sucessor
        cont = 1
        total2 = 0
        respostas += 1
print (f'A maior sequencia de números em ordem crescentes foi de: {cont1}, somando um total de {soma1}')