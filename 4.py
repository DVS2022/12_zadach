l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
l2 = []


for i in l:
	if l.count(i) >= 2:
		l2.append(i)

l_unique = set(l2)
			
print (l)
print (l_unique)
