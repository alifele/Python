from landscape import generate
import numpy as np

a = np.array([1,1])
for i in range(10):
    print(generate(*a))
