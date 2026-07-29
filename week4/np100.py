import numpy as np



arr = np.random.randint(1, 10, (10))
arr = arr[(arr > 2) & (arr < 9)]
print(arr)

