#tupla é imútavel () e a lista é mutavel []
cores = ('vermelho', 'azul', 'verde')
print(cores)
print(cores[1])

#contar elementos quantas vezes o mesmo elemento aparece na lista
valores = (1, 2, 2, 3)
print(valores.count(2))
print(valores.count(1))
print(valores.count(3))

#encontra posição 
print(valores.index(1))

#pecorrer o nome valor no print - guardar os valores que estão na tupla
for valor in valores:
    print(valor)
