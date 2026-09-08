#começamos importando a galeria do csv 
import csv

#leitura - o código ler e traz o que tem no arquivo 
with open('listaprodutos.csv', 'r') as arquivo:
        csv_reader = csv.reader(arquivo, delimiter=';')
        for line in csv_reader:
                print(line)


import csv
 
#leitura
with open('listaprodutos.csv', 'r') as arquivo:
     csv_reader = csv.reader(arquivo, delimiter=';')
     for line in csv_reader:
         print(line)
 
 
#atualizar e excluir
dados = []
 
with open('listaprodutos.csv', 'r', newline='', encoding='utf-8') as arquivo:
    csv_reader = csv.reader(arquivo, delimiter=';')
 
    for linha in csv_reader:
        if linha[0] == "mouse":
            linha[2] = "35.99"  # novo valor
 
        # Remove apenas o registro com valor 49.9
        if len(linha) >= 3 and linha[0] == "fone" and linha[2] == "49.9":
            continue
        dados.append(linha)
 
with open('listaprodutos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    csv_writer = csv.writer(arquivo, delimiter=';')
    csv_writer.writerows(dados)
 
print("Produto atualizado!")
print("Registro removido!")
 
#adicionar um novo produto
novo_produto = ["fone", 5, f"{49.90:.2f}"]
 
with open('listaprodutos.csv', 'a', newline='') as arquivo:
    csv_writer = csv.writer(arquivo, delimiter=';')
    csv_writer.writerow(novo_produto)
 
print("Produto adicionado!")
 
 