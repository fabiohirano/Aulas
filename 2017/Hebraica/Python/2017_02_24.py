import random

nome = raw_input("Quem é?")

#morte = raw_input("Quer morrer como?")

mortes = ["esfaqueado", "quebrando a perna e morrendo por hemorragia interna", "suicidando-se", "dormindo", "dabeando-se muito forte e arrancando sua própria cabeça", "de avc", "ouvindo axé", "na fila do show do Justin Bieber", "dançando funk", "atropelado por um trio elétrico", "atropelado por um trator da Uber", "de susto", "tropeçando num Eevee", "com ataques epiléticos"]

#mortes =["tropeçando num Eevee"]

m = mortes[random.randint(0, len(mortes) - 1)]

print "Parabains,", nome, "voce morrera em 40 segundos", m

#n = int(raw_input("Digita um numero ai, meu, pfvr, na moral"))

#for i in range(n):
 # print 
