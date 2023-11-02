# Atividade A
#Primeiro vamos importar a Biblioteca random
import random

# Variaveis necessárias para a pontuação no jogo
pontos_do_computador = 0
pontos_do_jogador = 0
empates = 0
# Lista de escolhas em cada rodada do jogo
op = ["Pedra","Papel","Tesoura"]
# loop infinito até que uma das condições de vitória ou empate seja acionada
while True:
 
  computador = random.choice(op)
  
  jogador = input("É a sua vez, faça sua escolha, digite um deles\n [pedra], [papel],[tesoura]\n")
  jogador = jogador.capitalize()

  if jogador not in op:
    print("Escolha invalida: Por favor, digite Pedra, Papel ou Tesoura")
    continue
  if jogador == computador:
    empates += 1
    resultado = " Deu Empate ^_^"

    
  elif jogador == 'Pedra' and computador == "Tesoura" or jogador == 'Tesoura' and computador == 'Papel' or jogador == 'Papel' and computador == 'Pedra':
    resultado = "O jogador ganhou"
    pontos_do_jogador +=1
  else:
    resultado = "O computador ganhou"
    pontos_do_computador += 1
  print(f"Resultado: {resultado}")
  print(f"Atual pontuação\n\tPontos do Jogador\tPontos do Computador\n\t{pontos_do_jogador}\t\t\t{pontos_do_computador}\n\n")
  
  if pontos_do_computador == 3:
    print("A vitória foi do computador")
    pontos_do_jogador = 0
    pontos_do_computador = 0
    novamente = input("Caso queira jogar novamente digite [sim], caso contrário digite qualquer outra coisa")
    if novamente != "sim":
      break
   
  
  if pontos_do_jogador == 3:
    print("A vitória foi do jogador")
    pontos_do_jogador = 0
    pontos_do_computador = 0
    novamente = input("Caso queira jogar novamente digite [sim], caso contrário digite qualquer outra coisa")
    if novamente != "sim":
      break
        
  if empates == 3:
     print("Deu Empate")
     pontos_do_jogador = 0
     pontos_do_computador = 0
     novamente = input("Caso queira jogar novamente digite [sim], caso contrário digite qualquer outra coisa")
     if novamente != "sim":
       break
        
# Atividade B
  
import math
soma = 0
soma_anterior = 0
for i in range (2, 60000):
    soma += 1/i/math.log(i)**2
    print(soma)
