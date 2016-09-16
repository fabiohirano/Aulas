import random

lista_de_palavras = ["abacaxi", "banana"]
indice = random.randint(0, len(lista_de_palavras) - 1)
adivinhou = False

while not adivinhou:
	print("Digite uma letra:")
	letra = input()

	contagem = 0
	print ("-----")
	for i in range (len(lista_de_palavras[indice])):
		if letra == lista_de_palavras[indice][i]:
			print(letra)
			contagem = contagem + 1
		else:
			print("?")
		
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
