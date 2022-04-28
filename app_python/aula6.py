conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_union = conjunto.union(conjunto2)
print('Uniao: {}'.format (conjunto_union))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Interseccao: {}' .format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferenca entre 1 e 2: {}' .format(conjunto_diferenca))
print('Diferenca entre 2 e 1: {}' .format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}' .format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A e subconjunto de B: {}' .format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B e superconjunto de A: {}' .format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)

#----------------------------------------------------------------------------------

#conjunto = {1, 2, 3, 4}
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)