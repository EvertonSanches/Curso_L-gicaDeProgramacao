'''Utilizando o for para percorrer uma lista de nomes e imprimir cada um deles'''

nomes = ["Ian", "João", "Everton", "Pedro"]

for n in nomes:
    print(n)


usuarios = ["Ian", "João", "Everton", "Pedro"]

for usuario in usuarios:
     print("Enviando email para " + usuario)

''' 
    O que foi feito? 
    Loop percorreu a lista de usuários e para cada usuário
    imprimiu uma mensagem personalizada dizendo "Enviando email para [nome do usuário]".
'''
'''
Exercício: 1- Faça um programa que Mostre os numeros de 1 a 10 usando Loop
'''
contador = 1

while contador <= 10:
    print(contador)
    contador += 1

#Exercício: 1.1 - Agora faça o inverso, ou seja, mostre os numeros de 10 a 1 usando Loop

contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

print("Fim")
'''
2- Faça um programa que Mostre os numeros pares de 2 a 20 usando Loop
'''
numeros_pares = 0
for numero_atual in range(2, 21, 2):
   if numero_atual % 2 == 0:
       print(f"Os numeros pares de 2 a 20 sao: {numero_atual}")
'''
3 - Faça um programa que Mostre os numeros impares de 1 a 19 usando Loop
'''
numeros_impares = 1
for numero_atual in range(1, 20, 2):
    if numero_atual % 2 != 0:
        print(f"Os numeros impares de 1 a 20 sao: {numero_atual}")

tabuada = int(input("Digite um numero para ver a sua tabuada: "))

for t in range(1, 11):
   resultado = tabuada * t
   print(f"{tabuada} x {t} = {resultado}")

num_pares = 2
for numero_atual in range(2, 51, 2):
   if numero_atual % 2 == 0:
       print(f"Os numeros pares de 1 a 50 sao: {numero_atual}")

contador = 0

for i in range(5):
    
    numero = int(input("Digite um numero: "))

    if numero > 0:
        contador += 1
print(f"Voce digitou {contador} numeros positivos.")


contador = 0

for num in range(5):
    numero = int(input("Digite um numero: "))

    contador += numero

print(f"A soma dos numeros digitados é: {contador}")

contador = 0

for nota in range(4):
    nota_aluno = float(input("Digite a nota do aluno: "))
    contador = contador + nota_aluno

media = contador / 4
print(f"A media do aluno é: {media:.2f}")
'''
Informe o maior numero digitado
'''
numero = int(input("Digite um numero: "))

maior = numero

for i in range(4):
    numero = int(input("Digite um numero: "))

    if numero > maior:
        maior = numero

print(f"O maior numero digitado é: {maior}")