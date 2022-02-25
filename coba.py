import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = np.array([[1, 2], [3, 4], [5, 6]])
plt.plot(x, y)
plt.show()
for col in range(y.shape[1]):
    print(y[:, col])
