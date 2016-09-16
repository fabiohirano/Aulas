import random

lista_de_palavras = ["abacaxi", "banana"]
indice = random.randint(0, len(lista_de_palavras) - 1)
adivinhou = False
tentativas = 2
palavra_acumulada = ""

for i in range (len(lista_de_palavras[indice])):
	palavra_acumulada = palavra_acumulada + "?"

while not adivinhou:
	
	if tentativas == 0:
		print("Seu ruim!")
		break

	print(palavra_acumulada)	
	print("Digite uma letra:")
	letra = input()

	contagem = 0
	print ("-----")
	for i in range (len(lista_de_palavras[indice])):
		if letra == lista_de_palavras[indice][i]:
			contagem = contagem + 1
			
	if contagem == 0:
		tentativas = tentativas - 1
		
	print ("A palavra tem " + str(contagem) + " letras " + letra)
	
	print ("Você quer adivinhar a palavra?[S/N]")
	escolha = input()
	if escolha == "S":
		print ("Qual a palavra?")
		p = input()
		if p == lista_de_palavras[indice]:
			print("acertou")
			adivinhou = True
		else:
			print("errou")
