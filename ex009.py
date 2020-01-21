numero = int(input('Digite o número em que deseja saber a tabuada: '))
print('\nTabuada:\n')

x = 0

while(x <= 10):
    m = numero * x
    print('{} x {} = {}'.format(numero, x, m))
    x = x + 1



