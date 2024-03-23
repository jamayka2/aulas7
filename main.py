
# # import random

# # # posso criar um modulo
# # #posso usar algo que esta pronto no python
# # #existe um modulo chamado random == aleatorio 

# # # aleatorio = random.random() # criar numero aleatorio com ponto flutuante
# # # aleatorio2 = random.random()
# # # print(aleatorio,aleatorio2)

# # # aleatorio3 =random.randint(1,10) # criar com randint numero inteiro
# # # print(aleatorio3)

# # # aleatorio4= random.randrange(8,1520)
# # # print(aleatorio4)


# import random
# for n in range(-3,0):
#    meu_numero = int(input('digite o numero'))
#    numero_aleatorio =  random.randint(1,10)
#    if meu_numero == numero_aleatorio:
       
#        print("VOÇE GANHO o numero ",numero_aleatorio)
#        break
#    else:
#       print("VOCE ERROU FEIO o numero e ",numero_aleatorio)
#       print("VOCE TEM APENAS ",n-1, "CHANCES")


### **Atividade: Calculadora de Média de Notas**

# Crie um programa que permita ao usuário calcular a média de suas notas em diferentes disciplinas. O programa deve solicitar ao usuário que insira o número de disciplinas e, em seguida, pedir que insira as notas de cada disciplina. Depois de coletar todas as notas, o programa deve calcular e exibir a média geral.

# ### Passos para a implementação:

# 1. Solicite ao usuário que insira o número de disciplinas.
# 2. Use um loop para solicitar as notas de cada disciplina.
# 3. Calcule a média das notas.
# 4. Exiba a média geral ao usuário.

# n0= int(input('numero de disciplinas '))
# n1= int(input('materia portugues nota '))
# n2= int(input('materia matematica nota '))
# n3= int(input('materia fisica nota '))
# n4= int(input('materia ingles nota '))
# soma=n1+n2+n3+n4
# media = soma /4
# print("Nota",media)
# if media >=6:5
# 5
#     print("aprovado")
# else:
#     print("reprovado")
# if media ==5:
#     print("recuperaçao")


# 1. Solicite ao usuário que insira o número de disciplinas.
numero_dis = int(input('Digite o numero de disciplinas '))
soma = 0
# 2. Use um loop para solicitar as notas de cada disciplina.
for i in range(1,numero_dis):
    notas =  float(input(f'Digite a {i}º nota: '))
    soma = soma + notas
    # 3. Calcule a média das notas.
    media =  soma / len(range(1,numero_dis))
# 4. Exiba a média geral ao usuário.
print('Média: ',  media)2