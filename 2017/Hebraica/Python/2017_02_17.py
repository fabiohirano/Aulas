import random

numero = random.randint(0,100)

acertou = False

while not acertou:
  chute = raw_input("Digite um numero:")
  chute = int(chute)
  if chute == numero:
    print "Parabains!!!"
    acertou = True
  if chute < numero:
    print "Seu chute eh menor que o numero"
  if chute > numero:
    print "Seu chute eh maior que o numero"
