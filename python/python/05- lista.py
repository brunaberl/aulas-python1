frutas = ["maçã", "banana", "uva"]
print(frutas)

#ver primeiro elemento da lista
print(frutas[0])


#retornando demais elementos no seu index
print(frutas[1])
print(frutas[2])

#modificado para modificar usar esse código 
frutas[1] = "laranja"
print(frutas)

#para adicionar itens 
frutas.append("pêra")
print(frutas)

#adicionar no comeco da lista
frutas.insert(0, "abacaxi")
print(frutas)

#para procurar algo na lista usar código

indice= frutas.index("uva")
print(indice)

if "uva" in frutas:
    print('uva está na lista!')

#para remover itens

#removendo itens
frutas.remove("uva")
print(frutas)
 
if "uva" in frutas:
    print("Uva está lista!")
else:
    print("Uva foi removida")
 
#tamanho da lista
numeros = [100, 28, 4, 31]
print(len(numeros))
 
#ordenar
numeros.sort()
print(numeros)
 
frutas.sort()
print(frutas)
 
#inverter
numeros.reverse()
print(numeros)
 
frutas.reverse()
print(frutas)

#verificar se existe
print(2 in numeros)
print(100 in numeros) 

#adicionar varios numeros ou ate textos
#varios elementos ao mesmo tempo junta a lista antetiror e vai atualizar

numeros = [10, 20, 30] + numeros 
print(numeros)

#para adicionar e ordenar elementos 
numeros.sort()
print(numeros) 

#percorrer com for 
for n in numeros:
    print(n)

print(type(n))
print(type(numeros))
