#### Abrindo pagina da web via python
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import spacy
import speech_recognition as sr

Helena = ChatBot('Helena', read_only=True)
r = sr.Recognizer()

while True:

	pergunta = input("Digite uma pergunta : ")
	
	try:
	   print("Você :{}" .format(pergunta))
	   resposta = ('{}' .format (pergunta))
	   res = Helena.get_response(pergunta)
		        
	except:
	   
	   print("Não entendi o que você disse")  
  	 
	if pergunta !='':
	    print ('Helena : ', res)

	        	
	

