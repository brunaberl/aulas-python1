# exercicios 1
 
#aqui vamos criar a base das funções
#pedir para o usuário colocar seu nome e a quantidade de unhas decoradas
 
nome = input("Digite o nome da cliente: ")
quantidade_unhas = int(input("Digite a quantidade de unhas decoradas: "))
 
#depois vamos estabelecer os valores e as funções para apresentar os resultados
valor_manicure = 60
valor_decoracoes = 3
valor_decoracoes = quantidade_unhas * valor_decoracoes
valor_total = valor_manicure + valor_decoracoes
 
#o comando para imprimir na tela o nome da cliente em maiusculo
#o comando para contar a quantidade de caracteres que tem no nome
#e por fim o valor total da manicure
 
print("Cliente:", nome.upper())
print("Quantidade de caracteres:", len(nome))
print("Valor total: R$", valor_total)

#colocar esse código ao final do execicio para facilitar a execução
input('digite ENTER PARA CONTINUAR')
 



#exercicio 2
#peça o nome do cliente e depois peça para escolher o tipo de lavagem)
#é importante que o int esteja na frente parar trasforma o sqr em inteiros
 
nome = input("digite o nome do cliente")
tipo = int(input("Digite o tipo de lavagem (1 ou 2): "))
 
if tipo == 1:
 
#Se for 1, o serviço escolhido é lavagem simples.
    print("Serviço escolhido: Lavagem simples")
#Mostra o valor da lavagem simples.
    print("Valor a pagar: R$ 25,00")
 
   
# Se for 2, o serviço escolhido é lavagem completo.
elif tipo == 2:
    print("Serviço escolhido: lavagem completa")
    print("valor a pagar: R$ 50,00")
 
#se não for nenhuma das opçoes 1 ou 2 sera mostrado como erro
else:
    print("erro! lavagem invalida")
 


input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)
 



#Execicio 03
#coleta de dados estacionamento pago 

nome_motorista = input("digite nome do motorista: ")
quantidade_horas_estacionadas = float(input ("horas estacionadas: "))
valor_hora = 5 

#fazer cálculo das horas 

valor_total =  quantidade_horas_estacionadas * valor_hora

print( valor_total )

#valor acima de 30% informar 

if valor_total > 30:
    print( 'Cliente recebeu desconto de 10%')


    porcentagem = 10

    resultado = valor_total * porcentagem /100

    total_pagar = valor_total - resultado

    print(total_pagar)

else: 
    print(valor_total)


 

input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)
 


#Execício 04 - Escola Infantil turma matrículada (Bruna)

nome_crianca = input("Informe nome da criança:")
idade_crianca = int(input("Informe idade da crinaça:"))

                      

#turma pela idade

if idade_crianca == 7 or idade_crianca == 8:
    print('Pré-Escola')


elif idade_crianca == 5 or idade_crianca == 6:
    print('Jardim')

elif idade_crianca == 3 or idade_crianca == 4:
    print('Maternal')

else:
    print('Fora da faixa atendida')



print("nome da criança maiúscula:", nome_crianca.upper())

print('nome da criança minúscula:', nome_crianca.lower())

print('nome caracteres:', len(nome_crianca))


 
input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)
 





#EXERCICIO 5
 
#preço pastel
 
Pastel_De_Queijo = 8.00
 
Pastel_De_Carne = 9.00
 
#solicite
 
qtd_pasteis_carne=int(input("informe a quantidade de pasteis de carne:"))
 
qtd_pasteis_queijo=int(input("informe a quantidade de pasteis de queijo:"))
 
#calcule
 
valortotalcarne= int(qtd_pasteis_carne) * int(Pastel_De_Carne)
 
valortotalqueijo= int(qtd_pasteis_queijo) * int(Pastel_De_Queijo)
 
qtd_pasteis= int(qtd_pasteis_queijo) + int(qtd_pasteis_carne)
 
#valor e quantidade de pasteis
 
print("O valor total em Pasteis De Carne: R$", (valortotalcarne))
 
print("O valor total em Pasteis de Queijo: R$",(valortotalqueijo))
 
print("quantidade de pasteis vendidos:",(qtd_pasteis))
 
if  qtd_pasteis > 10:
    print("o cliente comprou mais de 10 pasteis")
else:print(("o cliente não comprou mais de 10 pasteis"))  


 
input('digite ENTER PARA CONTINUAR')
 
import subprocess
import os
 
comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)
 


#EXERCICIO 6
#Lista De Cores
 
cores = ['Azul', 'Branco', 'Verde', 'Amarelo']
cor= cores.index("Verde")
 
#Verificação se existe a cor em estoque
 
if "Verde" in cores:
    print("Cor disponível!")
else:
    print("Cor Indisponível")  
 
#lista ordenada das cores usando sort().
 
cores.sort()
print(cores)
 
#mostrar a quantidade de cores cadastradas usando len()
print(" A Quantidade De Cores Cadastradas é : ",len(cores))


