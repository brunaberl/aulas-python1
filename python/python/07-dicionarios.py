#no dicíonario podemos colocar qualquer tipo de gênero pprecisamos usar a chave


pessoa = {
    'nome': 'Ana',
    'idade': 30
}

print(pessoa)
print(pessoa['nome'])

#alterando valores 
pessoa['idade'] = 31
print(pessoa)

#adcionando novo dado 
pessoa['cidade'] = 'São Paulo'
print(pessoa)

#adicionando novo dado
pessoa['estado'] = 'SP'
print(pessoa)

#removendo chave
del pessoa['idade']
print(pessoa)

#removendo apenas valor
pessoa['estado'] = None
print(pessoa)

pessoasNovas = {
    1: {
        'nome': 'Vânia',
        'idade': 50
    },
    2: { 
        'nome': 'Carlos',
        'idade': 35
    }
}

#Exibindo na tela 
print(pessoasNovas)

#excluindo apenas o Carlos (ID 2)
del pessoasNovas[2]
print(pessoasNovas)

#ver chaves -saber quantas pessoas tem naquela chave ideial quando temos varios cadastros 
print(pessoasNovas.keys())

#ver valores 
print(pessoasNovas.values())

#exemplo de diversos itens e dicionarios 
#novo dicionário 
paes = {
    'nome1': 'Brioche',
    'tamanho': 20,
    'nome2': 'francês',
    'tamanho2': 15
    }

print(paes)
print(paes.keys())
print(paes.values())


#ver ao mesmo tempo qual é a chave e o valor de casa item use esse código

#ver chave o valor
print(paes.items())

#verificar se existe chave
print('nome1' in paes)
print('nome3' in paes)

#usar get

print(paes.get('nome1'))

#percorrer
for chave, valor in paes.items():
    print(chave, ':', valor)

    

bebidas = {
    10: {
        'nome': 'Coca-cola',
        'volume': 350


    },

    20: {
'nome': 'Suco de laranja',
'volume': 1000
    }
}

print(bebidas)
print(bebidas.keys())
print(bebidas.values())



