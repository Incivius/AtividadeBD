n = int(input('Entre com um numero maior ou igual a 50:'))
h = 1
number = 1
p = 0
numA=2
numB = 1
seSoma = True
s = 1
while number < n:
    number += 1

    if seSoma:
        h += (number * 2 - 1) / number
        s -= number / (number * number)
        seSoma = False
    else:
        h -= (number * 2 - 1) / number
        s += number / (number * number)
        seSoma = True

for i in range(n):
    numB += 2
    count = 1
    count1 = 1

    if number > 1:
        for i in range(2, numA+1):
            if (numA % i) == 0:
                numA += count

        for j in range(2, numB+1):
            if (numB % i) == 0:
                numB += count


p+= numA/(numB ** 3)





print(h)
print(s)
print(p)