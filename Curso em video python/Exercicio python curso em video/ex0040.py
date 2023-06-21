nota1 = float(input('Primeira nota'))
nota2 = float(input('segunda nota'))
media = (nota1+nota2) / 2
print('tiranto {:.1f} e {:.1f}, a media do alunno é {:.1f}'.format(nota1, nota2, media))
if media >=5 and media <7:
    print('O aluno está em Recuperação')
elif media <5:
    print('O aluno está Reprovado.')
elif media >=7:
    print('O aluno está Aprovado')