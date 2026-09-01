#calculos
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

soma =  int(num1) + int(num2) 
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2) 

print(soma)
print(subtracao)
print(divisao) 
print(moduloresto)
print(multiplicacao)
print(potenciacao)

# o comando type retorna o tipo da váriavel 
print(type(num1))
print(type(soma))

#Calcular área
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')

area = float(lado1) * float(lado2)

print('A area do quadrado é: {} ' . format(area))

nomecompleto = input('Informe o seu nome completo:')
# função len retorno a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres:', len(nomecompleto))

# upper = transformar um texto em maiusculo 
# lower = transformar um texto em minusculo 
# capitalize = somente a primeira letra em minusculo 
print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em minusculo:', nomecompleto.lower())
print('4. primeira letra em maiusculo:', nomecompleto.capitalize())
