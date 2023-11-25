# #Exemplo 1

# def divisao(a, b):
#   try:
#     total = a / b
#     return total
#   except ZeroDivisionError:
#     return None

# resultado = divisao(10, 2)

# if resultado is not None:
#   print("Primeira divisão: ", resultado)
# else:
#   print("Não foi possivel realizar a divisão")

# #Exemplo 2

# def divisao2(a, b):
#   if(b == 0):
#     raise ValueError("Não pode dividir por 3!")  
#   else:
#     total = a/b
#     print(total)

# try:
#   divisao2(18,3)
# except ZeroDivisionError as e:
#   print(f"Cálculo não permitido.{e}")

# #Elemplo 3 - Idade

# def validaIdade(idade):
#   if(idade >= 18):
#     print("Maior de idade")
#   elif (idade > 0 and idade < 18):
#     print("Menor de idade")
#   elif (idade < 0):
#     raise ValueError("Idade não pode ser negativa")
#   else:
#     raise ValueError("Idade não pode ser zero")

# try:
#   idade = float(input("Digite a sua idade: "))
#   if idade.is_integer():
#     validaIdade(idade)
#   else:
#     raise ValueError("Idade não pode ser número quebrado")
# except ValueError as e:
#   print(f"Erro da execução, {e}")

#Exercício 1 - Faça um programa que leia um número inteiro do usuário e imprima o seu quadrado. Se o usuário digitar um valor não inteiro ou valor negativo, imprima uma mensagem de erro.

try:
  num1 = int(input("Digite um número para saber o seu quadrado: "))
  if num1 < 0:
    raise ValueError("O número não pode ser negativo!")
  resultado = num1 ** 2
  print(f'O número digitado ao quadrado é:{resultado}')
except ValueError as e:
  print(f"Erro {e}")

#Exercício 2 - Faça um programa que leia dois números inteiros do usuário e imprima a sua soma. Se o usuário digitar um número não inteiro, imprima uma mensagem de erro.

try:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  resultado = num1 + num2
  print(f"A soma dos números é: {resultado}")
except ValueError as f:
  print(f"Error {f}")
  
#Exercício 3 - Faça um programa que leia um número inteiro do usuário e imprima o seu fatorial. Se o usuário digitar um número não inteiro ou menor que zero, imprima uma mensagem de erro.

try:
  num1 = int(input("Digite um número: "))
  if num1 < 0:
    raise ValueError("O número não pode ser negativo")

  resultado = 1
  for i in range(1, num1 + 1):
    resultado = resultado * i
    print(f'O fatorial de {num1} é {resultado}')
except ValueError as g:
  print(f'Error {g}')
  
#Exercício 4 - Faça um programa que leia um número inteiro do usuário e imprima o seu próximo primo. Se o usuário digitar um número menor que 2, imprima uma mensagem de erro.

def numeroprimo(numero):
  if(numero <= 1):
    return False

  for i in range(2,numero // 2 + 1):
    if numero % i == 0:
      return False
  return True

def numeroprimo2(numero):
  while True:
    numero = numero + 1
    if numeroprimo(numero):
      return numero

numero = int(input("Digite um número inteiro: "))
numero2 = numeroprimo2(numero)
print("O próximo primo é: ", numero2)

#Exercício 5 - Faça um programa que leia uma string do usuário e imprima o seu comprimento. Se o usuário digitar uma string vazia, imprima uma mensagem de erro.

try:
  string = input("Digite uma string: ")
  if string == "":
    raise ValueError("A string está vazia")
  print(f"O comprimento da string é : {len(string)}")
except ValueError as h:
  print(f"Erro {h}")

#Exercício 1: Lidando com NameError

try:
 soma = sum(lista_numeros)
 media = soma / len(lista_numeros)
 print("A média é:", media)
except NameError:
 print("Lista não declarada")

#Exercício 2: Lidando com ValueError

try:
  numero = int(input("Digite um número inteiro: "))
  print("O número digitado é:", numero)

except ValueError:
  print("Você não digitou um número!")

#Exercício 3: Lidando com AttributeError

try:
 minha_string = "Olá, mundo!"
 comprimento = minha_string.comprimento
 print("O comprimento da string é:", comprimento)
except AttributeError:
  print("A string não possui o método comprimento!")

#Exercício 4: Lidando com Key

try:
 meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
 valor = meu_dicionario['d']
 print("O valor é:", valor)
except KeyError:
  print("A chave não existe")

#Exercício 5: Lidando com SyntaxError

try:
 for i in range(5):
  print(i)
except SyntaxError:
  print(f"Erro {SyntaxError}")

#Exercício 6: Lidando com IndexError

try:
 minha_lista = [1, 2, 3, 4, 5]
 elemento = minha_lista[10]
 print("O elemento é:", elemento)
except IndexError:
  print("O índice está fora dos limites da lista")

#Descrição do Desafio:
#Desenvolva um jogo em Python onde o computador escolhe aleatoriamente um número e desafia o usuário a adivinhá-lo de acordo com o nível de dificuldade. Utilize a estrutura try-except para lidar com possíveis erros quando o usuário inserir uma entrada que não seja um número. Passos necessários:

#O jogo solicita a idade do jogador, que deve ser um número inteiro.
#Idade menor que 10 anos: nível de dificuldade fácil;
#Idade entre 11 e 18 anos: nível de dificuldade intermediário;
#Idade maior que 19 anos: nível de dificuldade difícil.
#O programa deve gerar aleatoriamente um número inteiro dentro de um intervalo definido, dependendo do nível de dificuldade selecionado:
#Nível fácil: sortear números de 0 a 10
#Nível intermediário: sortear números de 0 a 50
#Nível difícil: sortear números de 0 a 100
#Solicite ao jogador que insira um número como tentativa de adivinhar o número gerado pelo programa.
#Utilize try-except para garantir que o programa consiga lidar com possíveis erros quando o jogador inserir uma entrada que não seja um número válido (tanto para idade quanto para o número que está adivinhando).
#Verifique se o número inserido pelo jogador corresponde ao número gerado pelo programa.
#Caso o jogador adivinhe corretamente, exiba uma mensagem de parabéns e encerre o jogo. Caso contrário, informe se o número é maior ou menor do que a tentativa do jogador e dê outra chance para adivinhar.
#Repita o processo até que o usuário adivinhe o número correto ou atinja um limite máximo de tentativas.

import random
try:
  numero_secreto = 0
  idade = int(input("Digite sua idade: "))
  if idade <= 10:
    dificuldade = "Facíl"
    numero_secreto = random.randint(0, 10)
    print("Nível facíl selecionado")
    print("Tente adivinhar o número secreto entre 0 e 10")
  if idade == 11 <= 18:
      dificuldade = "Média"
      numero_secreto = random.randint(0, 50)
      print("Nível médio selecionado")
      print("Tente adivinhar o número secreto entre 0 e 50")
  if idade > 19:
        dificuldade = "Difícil"
        numero_secreto = random.randint(0, 100)
        print("Nível difícil selecionado")
        print("Tente adivinhar o número secreto entre 0 e 100")
        
  tentativas = 0
  while True:
      tentativas += 1
      chute = int(input(f"Tentativa {tentativas}: "))
      if chute == numero_secreto:
        print("Parabéns você acertou")
        break
      if chute > numero_secreto:
        print("O número secreto é menor")
        continue
      print("O número secreto é maior")
      continue
  if tentativas <= 3:
   print("Parabéns, você ganhou o jogo")
   print(f"Você acertou em {tentativas} tentativas")

except ValueError:
  print("Você digitou uma entrada inválida")
      


      
  
    



    
    









    
    
  



