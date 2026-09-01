numero = int(input('informe um numero: '))

resultado = int(numero % 2)

print('Se o resultado for 0 é par e se for 1 é impar, o resultado é:', resultado)
input('Digite ENTER para continuar')

# if é usado para tomada de decisão 
if resultado == 0:
    resultado = "o número é par"

else: 
    resultado ='o número é impar'

print(resultado)

input('Digite ENTER para continuar')

import subprocess
import os

comando = 'cls' if os.name == 'nt' else 'clear'
subprocess.run(comando, shell=True)

# Entra da nota 
nota = float(input('Digite a nota do estudante:'))

# Verificação da situação
if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')

    
