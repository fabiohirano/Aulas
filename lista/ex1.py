n = int (raw_input("aAasaaa: "))
d = int (raw_input("fhjfjkgfkjgkjg: "))

l1 = []
l2 = []

for i in range(1, n):
	if (i % d == 0):
		l1.append(i)
	else:
		l2.append(i)

print l1
print l2
