import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)


#apenas para acessar os valores da chave 'nome' do arquivo json usar:
print(dados)
print(dados['nome'])

#para converter o json em um arquivo de str (texto)

texto = json.dumps(dados, indent=4, ensure_ascii=False)
print(texto)

#convertendo json em str
pessoaNova = '{"primeironome": "Vânia", "Idade": 50}'

dadosNovo= json.loads(pessoaNova)
print(dadosNovo)

#atualizando os dados 
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

dados['idade'] = 36 #alterando
dados['redesocial'] = "bruna.sil@" 
del dados['telefone'] #excluir dado existente

#escrever - 

with open('dados.json', 'w', encoding='utf*8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dado adicionado com sucesso!")
print('Telefone removido com sucesso!')
print(dados) 


