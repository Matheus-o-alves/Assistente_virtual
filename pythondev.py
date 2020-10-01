#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
"""
Created on Tue Jun  2 21:47:43 2020

@author: matheus
"""
'''
resenha = "O filme foi \"demais\""
resenha2 = "O filme foi \n \"demais\""

print(resenha)
print(resenha2)
'''
####FOrmatação de String
'''
aluno = "Matheus"
nome_do_curso = "Fotogafia"
mensagem = f"Bem vindo ao curso de {nome_do_curso} {aluno}"
print(mensagem)
'''
'''
# Método comuns de sting
nome_do_curso = ' Edição de videos '
print(nome_do_curso.upper()) #Letras minisculas
print(nome_do_curso.lower())#Letras Maisculas
print(nome_do_curso.strip())#Tirar espaçamento direito
print(nome_do_curso.lstrip())#Tirar espaçamento esquedo
print(nome_do_curso.rstrip())#TIras espaçamento esquerdo e direito
print(nome_do_curso.find('ção'))#Procura frase
print(nome_do_curso.replace('videos','musica'))#Trocar palavras
'''
'''
#Acessando partes de uma string
mouse = 'mouse'
print(mouse[3])
descricao= "Esse é um computado que foi lançado e chegou para revolucionar o mecado atual"
print(descricao[-1])
print(descricao.index('o'))
'''
'''
link = 'facebook'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[1:])
print(link[-5:0])
print(link[:-3])
'''
'''
#Listas
site1 = 'youtub.com'
site2 = 'facebook.com'
site3='instagram.com'

sites = ['youtub.com','facebook.com','instagram']
print(sites[1])
sites.append('novositte.com')#Inserindo informação na lista
sites.remove('facebook.com')#removendo da lista
##Lista dinâmicas
pessoas = [["Matheus","23"],["Catarina","21"]]
print(pessoas[0][0])

'''
#Tuplas Diferença de lista é que não pode trocar as informações
'''
sites = ("youtub","facebook","google","instagram")
valores= (0,1,2,3)
print(sites[0], valores[0])
'''
#Dicionarios
"""
pessoas= {'Nome':'Matheus', 'idade':23, 'altura':170}
print(pessoas)
nomes = ["Matheus","Ricarod","Julio","Matheus"]
print(list(dict.fromkeys(nomes))) # Remove valores dulicados
"""
#Datas e tempo
'''
from datetime import datetime
print(datetime.now())
'''
#Loop for
#Primeiro for -  inseri informações na lista- segundo for  imprimi separadamente

'''
Qt = int (input("Insira a quantidade d filmes inicial"))
film = []
cont = 1
for filme in range (0,Qt):
    
    filmes = str(input(f"Filme  {cont}º :"))
    film.append(filmes)
    cont=cont+1
for nome in range(0, Qt):
    print(film[nome])
print(film)   
'''
#Programa que recebe 2 notas de 2 alunos
'''
alunos = []
notas = []
for aluno_nota in range(0,2):
    
    aluno = str(input("Digite o nome do aluno :"))
    nota= float(input("Digite a nota :"))
    alunos.append(aluno)
    notas.append(nota)
        
    
    
for alunos_notas in range (0,2):
    print(f'Nome :{alunos[alunos_notas]} Notas :{notas[alunos_notas]}')

'''
'''
#Comando break

estilos = ['rock','pop','pagode']
series = ['Mr Robot','Supernatural','Dark']
for estilo in estilos:
    if estilo=='pop':
        break
    print(estilo)
    
for serie in series:
    if serie=='Supernatural':
        continue
    print(serie)
    32.58
    
'''

##Classes
'''
class Somatorio():
    def incremento_par(self, v, i):
        valor = v
        incremento = i
        resultado = valor+incremento
        return resultado
   
a = Somatorio().incremento_par(23, 1)   
print(a) 
    
    
class NovoSomatorio():
    def somatorio_impar(self, x, y):
        self.nvalor= x
        self.nincremento=y
        self.nresultado = self.nvalor+self.nincremento
        return self.nresultado
    
    
b = NovoSomatorio()
n1=int(input("Digite um numero ;"))
n2=int(input("Digite um numero :"))
b.somatorio_impar(n1,n2)
print(b.nvalor)
'''
class AulaClasse():
    def __init__(self, x=10, y=1):
        self.valor = x
        self.incremento = y
        self.valor_exponencial= x
    def incremento(self):
       self.valor = self.valor+self.incremento
    def verificando(self):
        if self.valor>12:
            print("Utrapassol 12")
        else:    
            print("Abaixo de 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor **e
    def incremento_quadrado(self):
        self.incremento()
        self.exponencial(2)        


q = AulaClasse()

print(q.exponencial(2))
#print(exponencial)

#Herança

#class Calculos(NovoSomatorio):
 #   pass
    
    
    
    
    
    
    
    
    

 