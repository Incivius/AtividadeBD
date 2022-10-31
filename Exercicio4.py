respostas = 0
primeiro_n = int(input('Qual será o primeiro número da sequencia? '))
cont = 1
cont1 = 0
soma = 0
soma1 = 0
total = 0
total2 = 0
soma2 = 0

while respostas < 10:
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


respostas = 0
primeiro_n = int(input('Qual será o primeiro número da sequencia? '))
cont = 1
cont1 = 0
Novo_valor = 0
Valor_anterior = 0

while respostas < 7:
    sucessor = int(input('Qual o proximo número da sequancia?'))
    if sucessor == primeiro_n :
        cont += 1
        if cont > cont1:
            cont1 = cont
            Valor_Anterior = sucessor
            primeiro_n = sucessor
            respostas += 1
            print (sucessor)
            print (primeiro_n)
            print (cont)
            print (cont1)
            print (Valor_Anterior)
        elif cont < cont1:
                primeiro_n = sucessor
                respostas += 1
        elif cont == cont1:
            if sucessor > Valor_Anterior:
                Valor_Anterior = sucessor
                respostas += 1
                primeiro_n = sucessor
    else:
        primeiro_n = sucessor
        cont = 1
        respostas += 1

if cont1 > 0:
    print (f'A maior sequencia consecutiva de números em ordem contante foi de {cont1}x dado pelo seguinte número: {Valor_Anterior}')
else: 
    print ('Não houve sequencia consecutiva de números em ordem constante ')
