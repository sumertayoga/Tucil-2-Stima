from re import S
import numpy as np
import matplotlib.pyplot as plt

p1 = np.array([1, 1])
p2 = np.array([1, 4])
p3 = np.array([p1, p2])
print(p3)
p3 = np.append(p3, [p1], axis=0)
print(p3)
p3 = np.unique(p3, axis=0)
print(p3)
