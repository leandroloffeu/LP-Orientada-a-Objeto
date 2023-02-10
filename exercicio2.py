#criar um programa para organizar um array(lista/tupla)
#-> por ordem alfabética = NÂO PODE USAR O SORT SORTED e AFINS
#NÂO PODE USAR FUNÇÂO PRONTA DO PYTHON

lista = []

while True:
    valor = str(input('digite um numero ou x para sair: '))
    if valor == 'x':
        break
    else:
        lista.append(valor)

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista [j+1]:
            lista[j], lista [j+1] = lista[j+1], lista[j]
print(lista)