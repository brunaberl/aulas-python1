#loop for 
for i in range(1, 6):
    print(i)

frutas = ['maçã', 'banana', 'uva']
for fruta in frutas:
    print(fruta)

#loop for com continue (pula o 5)
for j in range(1, 11): # no local do j eu posso colocar qualquer nomeclatura
    if j == 5: #informa a posicao do numero e nao o numero do andar em caso de elevador

        continue
    print(j)

#loop for com break (para no 4)
for m in range(1, 11):
    if m == 5:
        break
    print(m)

#usando o continue e break juntos
for n in range(1, 11):
    if n == 5: 
        continue #pula o número 5

    if n == 8: 
        break #para o loop quando chegar no 8

    print(n)   

#loop while 
texto = ''
while texto != 'sair':
    texto = input('digite algo (ou "sair" para parar):')


contador = 1

while contador <= 5:
    print(contador)
    contador += 1 #incremento = somar vai somando até chegar no numero que queremos parar nesse exemplo 5 - podemos utilizado para quantidades determinadas ex: capsulas de compridos 

#não devemos fazer - loop infinito - pode queimar a maquina
#while True:
    #print('este loop é infinito!')


#loop com try e except
while True:
    try:
        n = int(input('Digite um número: '))
        print(n)
        break #necessario para nao ficar no loop infinito 
    except ValueError:
        if input('Tentar novemente? (s/n): ').lower() != 'S':
            break


