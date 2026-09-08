#Criar um help desk 
# 1. Coleta dos dados do chamado
nome_cliente = input("Digite o nome do cliente: ")
descricao_problema = input("Digite a descrição do problema: ")
ticket_input = input("Digite o número do ticket: ")

# 2. Conversão do número do ticket para inteiro e verificação do tipo
numero_ticket = int(ticket_input)
print(f"Tipo da variável do ticket: {type(numero_ticket)}")

# 3 Exibição da mensagem de boas-vindas formatada
print(f"\n--- Resumo do Chamado ---")
print(f"Olá, {nome_cliente.upper()}! Seja bem-vindo(a) ao suporte.")

# 4 Cálculo da quantidade de caracteres da descrição
quantidade_caracteres = len(descricao_problema)
print(f"Número do Ticket: {numero_ticket}")
print(f"Descrição do problema ({quantidade_caracteres} caracteres): {descricao_problema}")

#Alimentos 
nome_prato = input('informe o nome do drink ou prato: ')
quantidade_porcao = float(input('digite a quantidade padrao (ml/g) por porção: '))
quantidade_pessoas = int(input('Digite a quantidade de pessoas a serem servidas: '))

#Para fazer calculo total dos ingredientes 

total_ingredientes = quantidade_porcao * quantidade_pessoas

#Criação do dicionario de exibição 
receita_info = {'prato': nome_prato, 'total_ingredientes': total_ingredientes}

print('\n--- Resumo da Receita ---')
print(receita_info)

#Logistica 

#coletar dados do entregador 

quantidade_entregas = int(input('informe a quantidade de entregras feitas no dia: '))
valor_por_entrega = float(input('Informe o valor ganho por entrega (R$):'))
valor_combustivel = float(input('Informe o valor gasto com combustí (R$): '))

#calculo do ganho bruto e liquido 
ganho_bruto = quantidade_entregas * valor_por_entrega
ganho_liquido = ganho_bruto - valor_combustivel

#Exibir mensagem final já formatada 
print(f'\n--- Resumo Financeiro do Dia ---')
print(f'Ganho bruto: R$ {ganho_bruto:.2f}')
print(f'Gasto com combustível: R$ {valor_combustivel:2f}')
print(f'Seu ganho líquido final é: R$ {ganho_liquido:.2f}')

#Gestão de atividades 

#informações profissional 

nome_servico = input('Informe o nome do serviço:')
valor_total = float(input ('Informe o valor total cobrado pelo serviço (R$):'))
total_horas = float(input('Informe o total de horas trabalhadas:'))

# cálculo do valor por hora usando divisão
valor_por_hora = valor_total / total_horas

#criar lista (list) com 3 tarefas do dia

taferas_dia = ["Responder e-mails de clientes", "desenvolver o escopo do projeto", "Reunião de alinhamento"]

#criar tupla
 

status_projeto = ('Aprovado', 'Em andamento')

#Mostrar resultados no terminal 
print(f'\n--- Reumo de Gestão: {nome_servico} ---')
print(f'valor por hora trabalhada: R$ {valor_por_hora:2f}')


print('\ntarefas do dia:')
print(taferas_dia)

print('\n status do projeto:')

print(status_projeto)
