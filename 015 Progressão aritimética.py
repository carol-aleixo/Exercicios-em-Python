termo = int(input('Digite o primeiro termo a progressão aritimética: '))
razao = int(input('Digite a razão: '))
constante =  razao * 20
soma = 0
for i in range(termo, constante ,razao):
    soma = i + termo
    print(i, end=', ')


