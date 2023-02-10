#3 - criar uma função que vai receber algumas cidades(5)
#Organizar em ordem alfabética
#Podem subir no github e mandar o link aqui.
#Podem mandar o link de um google docs com as soluções também.

lista = []

while True:
    valor = str(input('digite o nome da cidade ou x para sair: '))
    if valor == 'x':
        break
    else:
        lista.append(valor)

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista [j+1]:
            lista[j], lista [j+1] = lista[j+1], lista[j]
print(lista)