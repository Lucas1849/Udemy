'''
Autor: Lucas
Data: 16/02
Versão: 1.0
'''
#Meu primeiro codigo 

print("Ola")
print("Tudo bem?")
print("Que dia é hoje?")

#Meu segundo código
print("Quarta")
#Variável 
x = "A Maria Clara é extremamente linda"
print(x)

x = str(3)
y = int(4) 
z = float(5)

print(x + x)
print(y + y)
print(z + z)

#O Lucas tem 16 e é apaixanodo na Maria Clara
nome = input('Qual é o seu nome: ')
idade = input('Qual a sua idade: ')
idade = str(idade)
namorada = input('Qual o nome da menina mais linda do mundo:')
print("O " + nome + " tem " + idade + "e é apaixanodo na " + namorada)

nascimento = input('Qual o seu ano de nascimento?')
idade = 2023- int(nascimento)
print(idade)

#Slicing

amor ='Maria'
#index 01234

print(amor[1:5])
#Só é possivel realizar o Slicing com strings(str)

#Forma mais simples de escrever textos nos print

nome2 = 'Lucas'
sobrenome = 'Vieira'
Sentimentos = 'ama'

texto = f'O {nome2} {sobrenome} {Sentimentos} a Maria Clara'
print(texto)

#Operadores de comparação
# ==
# != - Diferença
# >
# <
# >=
# <=

# Operadores de atribuição (assignment operetors)
# forma mais reduzida de fazer calculos

x = 10
#x += 5
#x -= 5
#x *= 5
#x /= 5
#x %= 5

# if, else and elif

velocidade = 40

if velocidade > 110:
  print('Acima da Velovidade Permitida')
  print('Favor reduzir a sua velocidade')
elif velocidade < 60:
  print('Favor dirigir acima de 80km/h')
else:
  print('Velocidade OK')

#Operadores Logicos (Logical Operators)

renda = True
nome_limpo = True

if renda and nome_limpo:
  print('Financiamento Aprovado')
else:
  print('Financiamento Negado')

  #Operador Ternário (Ternary Operator)

idade = 14
#if idade >= 16
#print('Voto Permitido')
#else:
#print('Voto Negado')

resultado = 'Voto Permitido' if idade >= 16 else 'Voto Negado'
print(resultado)

#Multiplos operadores de comparação (Multiple Comparison Operators)

valor = 10

#if valor >= 20 and valor < 40:
if 20<= valor < 40:
 print('Produto Aceito')
else:
  print('Produto Negado')

#For Loops (Looping)

for numero in range(1,18,7):
  print(numero)

#For Loops (Strings)
for letra in 'Google':
 print(letra)

#Foor Loops with IF and ELSE

compra = True
dados_da_compra = 'Compra no valor de R$ 15,00.Data de entrega prevista para dia 11/03.'

for enviar in range(3):
   if compra:
    print(dados_da_compra)
    print('Detalhes enviados para o seu email')
    break
else:
 print('Não foi possível realizar a compra')
  
# for loop nested
  
  #Outer loop
   #Inner loop
for numero1 in range(1,11):
  print(numero1)
  for numero2 in range(1,10):
   print(numero1 + numero2)
    
#For loop (separando strings)  

palavra = 'FANTASTICO'

for espaço in palavra:
  print(f' {espaço}' , end='')

#Criando um retangulo com for loops

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='')
  print()
#While Loops

valor = 100
dia = 1
while valor > 20:
  dia += 1
  print(f' No dia {dia} o produto sera vendido por R${valor}')
  valor -= 5

#Condições com While Loops

valor = int(input('Digite o valor do seu produto:'))

while valor > 20:
   valor = (valor * 0.10) + valor
   print(f' O valor final do seu produto é de R$ {valor}')
   break
#Funções
  #DRY - Don't repeat yourself.
def boas_vindas():
   print('Ola Lucas')
   print('Temos 5 laptops em estoque')


boas_vindas()

#Funções de soma

def somar():
  numero1 = 5
  numero2 = 10
  resultado = numero1 + numero2
  print(resultado)


def somar2():
  numero1 = 5
  numero2 = 7
  resultado = numero1 + numero2
  print(resultado)


somar()
somar2()

#Usando parametro e argumentos em funções
  #Parametro ---> Argumento

def boas_vindas(nome,quantidade):
  print(f' Ola {nome}')
  print(f'Temos {str(quantidade)} em estoque')

boas_vindas('Marcos', 5)
boas_vindas('Maria', 3)
boas_vindas('Roberta', 7)

#Default = Aquele que você define o valor no parametro
#Non-Default = Aquele que você não define o valor no parametro

#def boas_vindas((Non-Default)nome,(Default)quantidade=6):
  #print(f' Ola {nome}')
  #print(f'Temos {str(quantidade)} em estoque')

#boas_vindas('Marcos',)

#A sequência sempre será(Non-Default, Defaul).
#Sair desta sequência acaba ocorrendo erro

#Print ou Return em Funções

#Realiza uma tarefa(print)
def cliente1(nome):
  print(f' Olá {nome}')

  cliente1('Maria')

#Calcula e retorna um valor(return)
def cliente2(nome):
  return f' Olá {nome}'

  cliente2('Jose')

#Função com vários argumentos(xargs)
  #Criar uma função que soma vários números

def soma(*numeros):
  resultado = 0
  for num in numeros:
     resultado += num
  return resultado
    

x= soma(2,8,9,15)

print(x)

#Criar função que armazena números e string(dados)

def agencia(**carro):
  return carro


print(agencia(marca='Gol',cor='branca',motor=1.0,placa=1234))
print(agencia(marca='Gol',cor='azul',motor=2.0,))
print(agencia(marca='Gol',cor='preto',))

#Importando Módulo
#Exemplo(Fatorial)

import math

print(math.factorial(5))

#Listas
  #Amazenar mais de uma informação em variáveis
  #Manter a sequencia dos dados em uma variável

cidades = ['Rio de janeiro', 'São paulo', 'Salvador']
#index            0              1            2

#cidades[0] = 'Minas Gerais'
#cidades.append('Santa Catarina')
#cidades.remove('São Paulo')
#cidades.insert(1,'Florianópolis')
#cidades.pop(2)
#cidades.sort()
print(cidades)

#Concatenando listas

itens =[['item1', 'item2'], ['item3', 'item4']]

print(itens[1][1])

#Extraindo variáveis de listas

produtos = ['arroz', 'feijão', 'laranja', 'banana', 'alface', 'tomate', 'cebola']

item1, item2, item3, *outros = produtos 

#Looping dentro de listas

valores = [50, 80, 110, 150, 170]

for x in valores:
  print(f'O valor final do produto é de R${x}')

#Exemplo com listas

cores_cliente = input('Digite a cor desejada:')
cores = ['amarelo', 'verde', 'azul', 'vermelho', 'roxo', 'rosa']

if cores_cliente.lower() in cores:
  print('Temos em estoque')
else:
  print('Não temos em estoque')
  
#Agregando duas listas com o Zip

comidas = ['Pizza', 'Hambúrguer', 'sorvete', 'arroz']
posição = [1, 2 ,3, 4]
listas = zip(comidas, posição)

print(list(listas))

#Lista com dados fornecidos pelo usuario

frutas_usuario = input('Digite as frutas separadas por uma vírgula:')

print(frutas_usuario.split(', '))

#Tuples
  #Amazenar mais de uma informação em variáveis
  #Manter a sequencia dos dados em uma variável
  #Não podem ser alteradas(Immutable)

cores_list = ['Amarelo', 'Verde', 'Vermelho', 'Azul']
cores_tuple = ('Amarelo', 'Verde', 'Vermelho', 'Azul')

#Arrays
  #Similiar a listas
  #Melhor performance
from array import array

#letras = ['a', 'b', 'c', 'd']
#numeros_i = [10, 20, 30, 40, 50]
#numeros_f = [1.2, 2.2, 3.2, 4.2]

#print(letras)
#print(numeros_i)
#print(numeros_f)

letras = array('u' , ['a', 'b', 'c', 'd'])
numeros_i = array('i',[10, 20, 30, 40, 50] )
numeros_f = array('f', [1.2, 2.2, 3.2, 4.2])

print(letras)
print(numeros_i)
print(numeros_f)

#Sets(Listas)
  #Similiar a alistas
  #Evita itens duplicados
  #Não utliza index
list1 = [10, 20, 30, 40 ,50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference]
print(num1 & num2) #And
print(len(num1))

#Continuando com Sets

s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
s1.update({8, 9, 10, 11, 12})
s1.remove(12)
#remove só retira o item presente na lista
s1.discard(56)
#discadr só descarta o numero, estando presente na lista ou nao

print(s1)

#Sets com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.intersection(set3)

print(set4)

#Dicionários
  #Utilizando index no formato de Keys e Values
  #Aceita string, integer, float, boolean...

aluno = {'nome': 'Lucas', 'idade': 16, 'nota_final': 'A', 'Aprovação': True}
#o index ée no formato de key, então é preciso colocar o nome da key no print

print(aluno)

#Manipulando dados no Dicionário

#aluno = ['nome'] = 'Jose'
#aluno.update({'nome': 'Jose', 'nota_final': 'B'})
#aluno.update({'endereço': 'Rua a '})
#print(aluno.get('endereço'))
#del aluno['idade']

#Lopping dentro de Dicionários

for keys, values in aluno.items():
  print(keys, values)

#Função lambda
  #É uma função (pequena) sem nome
  #Pode ter vários argumentos mas somente 1 expressão
  #Muito utlizada dentro de outras funções
  #Codigo mais 'clean'

#def somar(x):
#  return x + 10

#print(somar(2))

somar10 = lambda x: x + 10 
print(somar10(4))

#Lambda dentro de uma função

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))

#Map Function 
  #Muito utilizado com listas
  # Aplicar uma função a um Iterable, por item. (list, tuple, dic, etc.)

lista1 = [1, 2 , 3, 4]

#def multi(x):
#  return x * 2

#lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))

#Filter Function 
  #Muito utilizado com listas
  # Aplicar uma função a um Iterable, filtrando os itens. (list, tuple, dic, etc.)

valores = [10, 12, 34, 44, 57]

#def remove20(x):
#  return x > 20

#print(list(filter(remove20, valores)))

print(list(filter(lambda x: x > 20, valores)))

#List Comprehension
  # Mais simples de se escrever
  # Utilizado quando voce precisa criaruma nova lista a partir de uma existente
  #[expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

#frutas2 = []

#for itens in frutas1:
#  if 'b' in itens:
#    frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)

#Com integers

valores = [x * 10 for x in range(6)]
print(valores)

#for x in range(6):
#  valores.append(x * 10)

#Generator Expressios
  # Uma forma mais rápida para listas, dicionários etx.
  #Valores in byte

numeros = (x * 10 for x in range(100))

#Erros
  #Excelente para testes
  #Não realiza o 'stop' no programa
  #Mensagens customizadas quando encontra um erro

try:
  letras = [1, 2, 3]
  print(letras[3])
except IndexError:
  print('Index nao existe')

#Exemplo de uso:

try:
 valor = int(input('Digite o valor do produto:'))
 print(valor)
except ValueError:
  print('Favor digitar o valor em númeoros')



#finally:
#print('Temos o produto em estoque')

#else:
#  print('O valor do seu produto é de:')
#  resultado = valor * 0.10
#  print(resultado)


#Python Object-Oriented Programming

#Classes
  #Utilizadas para criar objetos
  #Objetos são partes dentro de uma Class (instances)
  #Classes são utlizadas para agrupar dados e funções, podendo reutilizar
  #======
  #Class: Frutas
  #Objects: Abacate, Banana...

#Criar a classe
  from datetime import datetime
class Funcionario:
  def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento

  def nome_compelto(self):
    return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
     ano_atual = datetime.now().year
     self.ano_nascimento = int(ano_atual - self.ano_nascimento)
     return self.ano_nascimento
#Criar o objeto
usuario1 = Funcionario('Elena', 'Cabral', 2009)
usuario2 = Funcionario('Carol', 'Silva', 2005)

#Criar os parametro do usuario1
#usuario1.nome = 'Elena'
#usuario1.sobrenome = 'Cabral'
#usuario1.data_nascimento = '12/01/2009'

#Criar os parametro do usuario2
#usuario1.nome = 'Carol'
#usuario1.sobrenome = 'Silva'
#usuario1.data_nascimento = '15/10/2005'
#print(usuario1.nome + ' ' + usuario1.sobrenome)
#print(usuario1.nome_compelto())
print(Funcionario.nome_compelto(usuario1))

#Módulos
from funções import find_index
from Items.cadastro import registro

registro()

list1('a', 'b', 'c', 'd', 'e')

var1 = find_index(list1, 'b')
print(var1)