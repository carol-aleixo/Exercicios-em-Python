num = int(input('Digite um número para saber sua tabuada: '))
for i in range(0, 11):
    resultado = num * i
    print('{} X {:2} = {:2}'.format(num, i, resultado))


