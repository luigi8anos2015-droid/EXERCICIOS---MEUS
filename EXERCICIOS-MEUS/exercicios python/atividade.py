#1: for i in range(1,21):
#     if i % 2 ==0:
#         print(i)

#2: contador = 1
# soma = 0

# while contador <= 100:
#     soma = soma + contador
#     contador = contador + 1

# print(soma)

#3: while True:
#     entrada = input("Digite um número: ")
#     try:
#         numero = int(entrada)
#         break
#     except ValueError:
#         print("Isso não é um número válido, tenta de novo!")

# print("Você digitou:", numero)


# 4:lista=[]
# for i in range(10):
#     lista.append(i**2)
# print(lista)

# 5:notas=[7.5, 8.0, 5.5, 9.0, 6.0]
# media=sum(notas)/ len(notas)
# print(media)

# 6:numeros=[3,2,29,45,98,67]
# maior = numeros[0]

# for n in numeros:
#     if n > maior:
#         maior = n

# print(maior)

# 7: numeros=[]

# 7:while len(numeros) < 5:
#     entrada = input("Digite um número: ")
    
#     if entrada.isnumeric():
#         numeros.append(int(entrada))
#     else:
#         print("Isso não é um número válido, tenta de novo!")

# soma = sum(numeros)
# media = soma / len(numeros)

# print("Números digitados:", numeros)
# print("Soma:", soma)
# print("Média:", media)


# 8: while True:
#     print("1 - Somar")
#     print("2 - Multiplicar")
#     print("3 - Sair")
    
#     opcao = input("Escolha uma opção: ")
    
#     if opcao == "1":
#         a = int(input("Digite o primeiro número: "))
#         b = int(input("Digite o segundo número: "))
#         print("Resultado:", a + b)
    
#     elif opcao == "2":
#         a = int(input("Digite o primeiro número: "))
#         b = int(input("Digite o segundo número: "))
#         print("Resultado:", a * b)
    
#     elif opcao == "3":
#         print("Saindo...")
#         break
    
    # else:
    #     print("Opção inválida, tenta de novo!")

# 9:contador = 10

# while contador >= 0:
#     print(contador)
#     contador =- 1

# print("Fim!")
        
'''questoes de logica parte 2'''

#1: for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)

# 2:contador = 0

# while contador <= 100:
#     print(contador)
#     contador = contador + 5

# 3:
# try:
#     numero_tabuada = int(input('Digite um número: '))
#     for i in range(1, 11):
#         resultado = numero_tabuada * i
#         print(f'{numero_tabuada} x {i} = {resultado}')

# except ValueError:
#     print('Digite um número válido')


# 4:numeros = [3, 8, 12, 5, 20, 7, 15]
# contador = 0

# for i in numeros:
#     if i > 10:
#         print(f'O número {i} é maior que 10')
#         contador = contador + 1

# print(f'No total, {contador} números são maiores que 10')


# 5: numeros = [3, 8, 12, 5, 20, 7, 15]

# pares = []
# impares = []

# for i in numeros:
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

# print(f'Pares: {pares}')
# print(f'Ímpares: {impares}')
    
# 6: lista_numeros = []
# contador_numeros = 0

# while True:
#     entrada = input('Digite um número (ou "parar" para sair): ')
    
#     if entrada == 'parar':
#         break
#     elif entrada.isnumeric():
#         lista_numeros.append(int(entrada))
#         contador_numeros = contador_numeros + 1
#     else:
#         print('Isso não é um número válido, tenta de novo!')

# print(f'Você digitou {contador_numeros} números: {lista_numeros}')


# 7: palavra = input('Digite uma palavra: ')
# contador = 0

# for letra in palavra:
#     if letra in 'aeiou':
#         contador += 1

# print(f'Sua palavra tem {contador} vogais')


# 8: palavra = input('Digite uma palavra: ')
# invertida = ''

# for letra in palavra:
#     invertida = letra + invertida

# print(f'Palavra invertida: {invertida}')
    

# 9:numeros = []

# while True:
#     pergunta = int(input('Digite um número para somar (limite é 50): '))
#     numeros.append(pergunta)
    
#     soma = sum(numeros)
    
#     if soma > 50:
#         print(f'O valor passou de 50! A soma final foi {soma}, com {len(numeros)} números digitados.')
#         break
#     else:
#         print(f'Soma até agora: {soma}')


# 10:notas_turma=[[7, 8, 6], [9, 10, 8], [5, 4, 6]]
# for aluno in notas_turma:
#     media = sum(aluno) / len(aluno)
#     print(media)
    

    
    







        
    




    

    
    