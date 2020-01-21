n = input('Digite algo: ')
print('O que foi digitado é um alfanumerico? {} \n'
      'O que foi digitado é um caracter? {} \n'
      'O que foi digitado é um número? {} \n'
      'O que foi digitado é um número decimal? {} \n'
       .format(n.isalnum(), n.isalpha(), n.isnumeric(), n.isdecimal()))

print(type(n))


