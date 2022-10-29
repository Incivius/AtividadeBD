salario = float(input('Qual o valor do seu salário? '))
vendas = float(input('Qual o valor das suas vendas? '))

if vendas > 1500:
    diferença = (vendas - 1500) * 0.07
    montante = 1500 * 0.05
    comissao = diferença + montante
else:
    comissao = vendas * 0.05

total =  salario + comissao

print ('O valor total a ser paga é de: R$ %.2f' %total)