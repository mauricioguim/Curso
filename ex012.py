preco = float(input('Informe o preço do produto que deseja saber o preço final após o desconto: R$ '))
desconto = int(input('Informe qual a porcentagem do desconto: '))

descontoCalc = (desconto - 100) / 100

valorAposDesconto = preco * descontoCalc

print('O produto com preço de {} ficará por {} com o desconto de {}%'.format(preco,valorAposDesconto, desconto))