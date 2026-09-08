#Exercício 1 Petshop - Cálculo Banho (Bruna)
#criar uma função - a função sempre precisa vir primeiro que os inputs ou da erro 
def calcularBanho(peso):
    if peso <=10:
        return 30.00
    elif peso <=20:
        return 50.00
    else:
        return 70.00


nomePet = input("Informe o nome do Pet:")
pesoPet = float(input('Informe o peso do Pet (Kg):')) 

valorFinal = calcularBanho(pesoPet)

print("O pet {} pagará: R$ {:.2f}".format(nomePet, valorFinal)) #se utiliza o .2f para indormar as casas dcimais


input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

#Exercício 2 - Empresa de Frotas

quantidade_motos = int(input('Informe a quantidade de Motos:'))

#o acumulador precisa comecar zerado 
total_quilometros = 0 

#Criamos o laço para que ele passe por cada moto
for m in range(quantidade_motos):
    km_moto = float(input("Informe a quilometragem da {} moto:" .format(m + 1)))
    total_quilometros += km_moto

#Laço com o calculando a média de quilomentragem
mediaKm = total_quilometros / quantidade_motos

print("\n--- Relatório da Frota ---")
print('Total de quilômetros: {:2f} km' .format(total_quilometros))
print('Média por Moto: {:.2f} km'.format(mediaKm))


input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)


#Exercício 3 - Lanchonete

totalcompra = float()
somaitens = float()

print("Cardápio:")
print("1: Hot Dog Simples - R$ 10.00")
print("2: Hot Dog Duplo - R$ 15.00")
print("3: Refrigerante - R$ 6.00")

quantidadeitens = int(input("Digite quantos itens deseja comprar: "))

for itematual in range(quantidadeitens):
    print("Item escolhido: ")
    item = int(input("Digite o número do item (1, 2 ou 3): "))

    if item == 1:
        somaitens += 10.00
    elif item == 2:
        somaitens += 15.00
    elif item == 3:
        somaitens += 6.00
    else:
        print("Opção inválida!")

totalcompra = somaitens

if totalcompra > 50.00:
    desconto = totalcompra * 0.10
    totalcompra = totalcompra - desconto
    print("Você ganhou desconto de R$" , desconto)

print("Valor total da compra: R$" , totalcompra)
print()



input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

#Exercício 4 - Consultoria

print("Classificação de risco:")
print("0 a 3 - Baixo")
print("4 a 7 - Médio")
print("8 a 10 - Alto")

try:
    nota = int(input("Digite a nota de risco: "))

    if nota >= 0 and nota <= 3:
        print("Classificação de risco: Baixo")
    elif nota >= 4 and nota <= 7:
        print("Classificação de risco: Médio")
    elif nota >= 8 and nota <= 10:
        print("Classificação de risco: Alto")
    else:
        print("Você digitou uma nota inválida!")

except ValueError:
    print("Erro: Você precisa digitar um número!")




input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

#Exercício 5

#Empresa de Limpeza controle de Equipe
 
def mostrar_funcionarios(lista):
    print("\nFuncionários cadastrados:")
    funcionarios = ["Lia", "Rafael", "Liz"]
    for funcionario in funcionarios:
        print(funcionario)
 
 
funcionario = []
texto = ""
 
while texto != "fim":
 
    texto = input("Digite o nome do funcionário (ou 'fim' para encerrar): ")
    if texto != "fim":
   
       funcionario.append("texto")
 
print("\nQuantidade total de funcionários cadastrados:", len(funcionario))
 
mostrar_funcionarios("funcionarios")



input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)


#Exercício 6 - Site livros 


import requests
from bs4 import BeautifulSoup

# 1. Fazendo a requisição para a página de livros
pagina = requests.get('https://books.toscrape.com/')

# 2. Analisando o HTML da página
dados_pagina = BeautifulSoup(pagina.text, "html.parser")

# 3. Encontrando todos os blocos de produtos (livros) na página
todos_livros = dados_pagina.find_all('article', class_='product_pod')

print(f"Foram encontrados {len(todos_livros)} livros:\n")

# 4. Percorrendo cada livro para extrair o Título e o Preço
for livro in todos_livros:
    # O título fica no atributo 'title' dentro da tag <a> do <h3>
    titulo = livro.find('h3').find('a')['title']
    
    # O preço fica na tag <p> com a classe 'price_color'
    preco = livro.find('p', class_='price_color').text
    
    print(f"Título: {titulo}")
    print(f"Preço: {preco}")
    print("-" * 40)


 