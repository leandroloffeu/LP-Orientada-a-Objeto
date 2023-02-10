#1 - cálculo de média de 4 notas => 7 aprovado <7 >= 4 = Exame final <4 reprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunta nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = float(nota1+nota2+nota3+nota4)/4
   
if media >= 7 and media < 10:
    print(f'\nSua média é {media}. Você está aprovado!')
elif media < 7:
    print(f'\nSua média é {media}. Você está reprovado!')
else:
    media == 10
    print(f'\nSua média é {media}. Você está aprovado com méritos')