# quantidade de notas disponiveis

c100 = 10
c50  = 20
c10  = 10
c5   = 10
c1   = 10

# numero de notas de cada tipo sacadas

n100, n50, n10, n5, n1 = 0, 0, 0, 0, 0

saque = int(raw_input("Quanto vc quer sacar, querido? "))
"""
if c100 * 100 >= saque:
  n100 = saque/100
  saque = saque - (n100 * 100)
if c50 * 50 >= saque:
  n50 = saque/50
  saque = saque - (n50 * 50)
if c10 * 10 >= saque:
  n10 = saque/10
  saque = saque - (n10 * 10)
if c5 * 5 >= saque:
  n5 = saque/5
  saque = saque - (n5 * 5)
if c1 * 1 >= saque:
  n1 = saque
  saque = saque - (n1 * 1)
"""

while c100 > 0:
  if saque < 100:
    break
  saque -= 100
  n100 += 1
  c100 -= 1

while c50 > 0:
  if saque < 50:
    break
  saque -= 50
  n50 += 1
  c50 -= 1


while c10 > 0:
  if saque < 10:
    break
  saque -= 10
  n10 += 1
  c10 -= 1

while c5 > 0:
  if saque < 5:
    break
  saque -= 5
  n5 += 1
  c5 -= 1

while c1 > 0:
  if saque < 1:
    break
  saque -= 1
  n1 += 1
  c1 -= 1

print "Sacando!", n100, "notas de 100 dinheiros"
print "Sacando!", n50, "notas de 50 dinheiros"
print "Sacando!", n10, "notas de 10 dinheiros"
print "Sacando!", n5, "notas de 5 dinheiros"
print "Sacando!", n1, "notas de 1 dinheiros"
