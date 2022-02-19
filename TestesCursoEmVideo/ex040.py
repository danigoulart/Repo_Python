nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Primeira Nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1} a média do aluno é {:.1f}'.format(nota1, nota2, média))
'''if média >= 5 and média < 7:'''
if 7 > média >= 5:
    print('O aluno está em recuperação!')
elif média < 5:
    print('O aluno está REPROVADO')
elif média >= 7:
    print('Parabéns, você foi aprovado!!')

