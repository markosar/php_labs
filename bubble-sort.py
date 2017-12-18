l = []
for i in range(5):
	l.append(input('dose stoixeio '))
print l
#l = [1,7,4357438,0,6,54,-98]
n = len(l)
for i in range(n):
		for j in range(n-1,i,-1):
				if(l[j-1]> l[j]):
						tmp = l[j-1]
						l[j-1] = l[j]
						l[j] = tmp

print l

