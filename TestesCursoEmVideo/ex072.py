cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:

    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
print('')
resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
if resp == 'N':
    break
print('-' * 40)
print('PROGRAMA ACABOU')
