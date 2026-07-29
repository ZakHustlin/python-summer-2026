

import numpy as np

rng = np.random.default_rng(42)
data = rng.integers(0, 100, size=(5, 4))
mean = data.mean(axis=0)
print(f"Mean is {mean}")
std = data.std(axis=1)
print(f"Standard deviation is {std}")
print("Data items greater than 50 are:", data[data > 50])