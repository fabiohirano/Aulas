# -*- coding: utf-8 -*-

# Peso/altura*altura
#

peso = float(raw_input("Olá, digite seu peso (em kg):"))
altura = float(raw_input("Agora digite sua altura (em m):"))

imc = peso/(altura * altura)

print "Seu IMC eh: " + str(imc)

if imc > 30:
    print "Cuidado! Seu IMC está muito alto!!"
    print "Voce deveria procurar um medico"

if imc < 17: 
    print "Cuidado! Seu IMC é de magreza moderada!!"
    print "Voce deveria procurar um medico"

if imc < 16:
    print "Cuidado! Seu IMC é de magreza grave!!"
    print "Voce deveria procurar um medico"
    

    
    
