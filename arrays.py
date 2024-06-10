#Lista - arrays ou vetores
#ut-avel e dinâmica, Heterogenea e indexada


lista = ['ato1', 'ato2', 'ato3', 'ato4', 'ato5']

print(type(lista))
#print(dir(lista))
print(lista[0])
print(lista[2])
print(lista[-1])
print(lista[0:2])
print(lista[::2])

lista[0] = 'alterado'
print(lista)

lista.append('Império Romano')
print(lista)

lista.remove('ato4')
print(lista)

del lista[2]
print(lista)

print(len(lista))
print(lista.count('ato2'))
print(lista.index('alterado'))

lista.reverse()
print(lista)

lista.sort()
print(lista)

#lista.clear() apaga o conteudo da lista
#print(lista)



