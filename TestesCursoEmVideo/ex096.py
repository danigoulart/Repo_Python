def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


#Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGUA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
