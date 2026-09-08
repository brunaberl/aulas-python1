#funcao - void 
def saudacao(): #definir a funcao 
    print('Olá, tudo bem?')


#acessando a função 
saudacao() #definiu a função como saudacao  é um funcao vazia eu preciso colocar o valor logo a baixo nesse caso um print('') o que eu quero. pode ser reaproveitada quantas vezes eu quiser. 

#função com parâmetro 
def saudacao(nome):
    print('olá,', nome)

#acessando a função 
saudacao('João')

#função de retorno 
def soma(a, b):
    return a + b

resultado = soma (5, 3)
print(resultado)

#exemplo com tratamento de erro  try tentar uma acao se nao consegui vai para o except que é a exceção
try:
    numero = int(input('digite um número:'))
    print(numero)
except:
    print('Você digitou algo inválido!')
#legal utilizar quando estamos fazendo formularios 

#try e except usando else e finally juntos
try:
    numero = float(input('Digite um NOVO número:'))
except ValueError:
    print('Erro: entrada inválida')
else:
    print('Você digitou:', numero)
finally:
    print('Programa finalizado')

#exemplo de função com try e except 
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
     return "Erro divisão zero"

print(dividir(10,2))
print(dividir(23,0))
#forma de validar uma função dividida por zero. 
#podemos deixar que o usuario dê entrada nos numeros 

#entrada do usúario 
a = float(input('Digite o primeiro número:'))
b = float(input('Digite o segundo número:'))
print(dividir(a, b))

