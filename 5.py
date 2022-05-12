from random import randint
import numpy as np

n = 5
m = [[randint(0,100) for i in range (n)] for j in range (n)]

print(m)

max_value = np.max(m)

print('Максимальное значение:',max_value)


