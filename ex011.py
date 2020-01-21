altura = float(input('Digite a altura da parede que deseja pintar: '))
largura = float(input('Digite a largura da parede que deseja pintar: '))

areaTotaldaParede = (altura * largura)
quantidadedeTinta = areaTotaldaParede/2

print('A parede com tamanho de {}m² precisará de {}L de tinta para ser pintada'.format(areaTotaldaParede, quantidadedeTinta))