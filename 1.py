x = int(input ('введите сумму вклада: '))
y = int(input ('введите процент вклада: '))
p = int(input ('введите необходимую для получения сумму: '))
year = int(0)
pers = y / 100

while x < p:
	x = x + (x * pers)
	x = int(x)
	year = year + 1
print ('Срок получения необходимой суммы в годах:', year)
