#comentário de uma linha
 
''' comentários: auxiliam
a deixar
"anotações" no código fonte'''
 
# concatenação
print('Boas vindas a aula de' + ' Python!')
 
# interpolação
print('Olá {}' . format(input('Qual o seu nome? ')))
 
#tipo de dados em python - números
# Inteiro
idade = 30
print(idade)
 
# Decimal (float)
altura = 1.75
print(altura)

# número complex 
numero_complexo = 2 + 3j
print(numero_complexo)

#texto(srt)
nome = "Bruna"
print(nome)

#booleando(bool)
ativo = True
print(ativo)

logado = False
print(logado)

#nenhum valor (NoneType)
valor = None
print(valor)

#Lista(list) mutável 
frutas = ["maçã", "banana", "uva"]
print(frutas)

#tuplas(tuple) imutável
cores = ("vemelho", "azul", "verde")
print(cores)

#conjunto(set)
numeros = {1, 2, 3, 4}
print(numeros)

#Dicionário(dict) pares chave-valor
pessoa = {
    "nome": "Bruna",
    "idade": 30
}
print(pessoa)


'''Python não tem constantes
verdadeiras, mas usamos uma conveção
para indicar que um valor não deve ser alterado.'''
PI = 3.14159
GRAVIDADE = 9.8

print("O valor de PI é", PI, "\nO valor de Gravidade é" , GRAVIDADE)
